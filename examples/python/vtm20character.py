#/usr/bin/python3
import sqlite3

sql_file = '../sqlite/CharacterCreation.sql'


class VtM20Character(object):
  ATTRIBUTE_CATEGORIES = ['Physical', 'Social', 'Mental']
  ABILITY_CATEGORIES = ['Talent', 'Skill', 'Knowledge']
  def __init__(self):
    self.db = sqlite3.connect(':memory:')
    with open(sql_file, 'r') as f:
      self.db.executescript(f.read())
  
  def getTraits(self, category = None):
    if category:
      traits = []
      for row in self.db.execute('SELECT Name FROM Traits WHERE Type = ?', (category,)):
        traits.append(row[0])
      return traits
    else:
      traits = []
      for row in self.db.execute('SELECT Name FROM Traits'):
        traits.append(row[0])
      return traits

  def getTrait(self, trait):
    for row in self.db.execute('SELECT Dots FROM Traits WHERE Name = ?', (trait,)):
      return row[0]

  def getTraitDots(self, trait):
    dots = {
      'Base': 0,
      'Creation': 0,
      'Freebie': 0,
      'XP': 0
    }
    for row in self.db.execute(
      'SELECT Type, COUNT(Type) FROM Dots WHERE Trait = ? GROUP BY Type ORDER BY TYPE ASC',
      (trait,)):
      dots[row[0]] = row[1]
    return (dots['Base'], dots['Creation'], dots['Freebie'], dots['XP'])


  def getTraitType(self, trait):
    try:
      return list(
        self.db.execute('SELECT Type FROM TraitCategories WHERE Name = ?', (trait,))
      )[0][0]
    except IndexError:
      return None

  def dotsAvailable(self, trait, dottype = 'Creation'):
    if trait in VtM20Character.ATTRIBUTE_CATEGORIES + VtM20Character.ABILITY_CATEGORIES:
      category = trait
      trait = None
    else:
      category = self.getTraitType(trait)

    if dottype == 'Creation':
      if category in VtM20Character.ATTRIBUTE_CATEGORIES:
        return [7, 5, 3][
          self.attributeOrdering.index(category)] - self.dotsSpent(category, dottype)
      if category in VtM20Character.ABILITY_CATEGORIES:
        
        available = [13, 9, 5][
          self.abilityOrdering.index(category)
        ] - self.dotsSpent(category, dottype)

        if trait:
          _, spent, _, _ = self.getTraitDots(trait)
          return max(0, min(3 - spent, available)) # cap by 3 per talent
        else:
          return available
      raise ValueError('category not found')
    elif dottype == 'Freebie':
      #TODO: implement Freebie limits
      return 0
    else:
      raise ValueError("Unknown Dottype!")

  def spendDot(self, trait, dottype=None, amount = 1):
    if amount > 0:
      if dottype == None:
        creation_avail = self.dotsAvailable(trait, 'Creation')
        if creation_avail > 0:
          spend = min(amount, creation_avail)
          self.spendDot(trait, 'Creation', spend)
          self.spendDot(trait, None, amount - spend)
        elif self.dotsAvailable(trait, 'Freebie') > 0:
          spend = min(amount, self.dotsAvailable(trait, 'Freebie'))
          self.spendDot(trait, 'Freebie', spend)
          self.spendDot(trait, None, amount - spend)
        else:
          self.spendDot(trait, 'XP', amount)          
      else:
        if dottype in ['Creation', 'Freebie'] and self.dotsAvailable(trait, dottype) < amount: 
          raise ValueError("Not enough dots available! {} < {}".format(
            self.dotsAvailable(trait, dottype), amount))

        for i in range(amount):
          self.db.execute('INSERT INTO Dots (Type, Trait) VALUES (?, ?)', (dottype, trait))

  def deleteDot(self, trait, dottype, amount = 1):
    if dottype:
      return self.db.execute(
        'DELETE FROM Dots WHERE Type = ? AND Trait = ? LIMIT ?', 
        (dottype, trait, amount)
      ).rowcount
    else:
      first_amount = amount
      amount -= self.deleteDot(trait, 'XP', amount)
      amount -= self.deleteDot(trait, 'Freebie', amount)
      amount -= self.deleteDot(trait, 'Creation', amount)
      return first_amount - amount

  def dotsSpent(self, category, dottype = 'Creation'):
    rows = list(
      self.db.execute(
        'SELECT Sum(Dots) FROM DotsSpent WHERE DotType = ? AND TraitType = ? GROUP BY TraitType', (dottype, category))
    )
    if len(rows) == 0: return 0
    return rows[0][0]

  @property
  def attributeOrdering(self):
    rows = []
    for row in self.db.execute('SELECT * FROM AttributeOrder'):
      rows.append(row[0])
    return rows

  @property
  def abilityOrdering(self):
    rows = []
    for row in self.db.execute('SELECT * FROM AbilityOrder'):
      rows.append(row[0])
    return rows

  def __del__(self):
    self.db.close()
