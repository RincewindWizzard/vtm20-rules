#/usr/bin/python3
import os
import sqlite3

sql_file = os.path.join(os.path.dirname(__file__), 'sql/CharacterTemplate.sql')

BASE      = 'base'
CREATION  = 'creation'
FREEBIE   = 'freebie'
XP        = 'xp'

SOCIAL    = 'social'
MENTAL    = 'mental'
PHYSICAL  = 'physical'

TALENT    = 'talent'
SKILL     = 'skill'
KNOWLEDGE = 'knowledge'

ATTRIBUTE_CATEGORIES = (PHYSICAL, SOCIAL, MENTAL)
ABILITY_CATEGORIES = (TALENT, SKILL, KNOWLEDGE)

class VtM20Character(object):
  def __init__(self):
    self.db = sqlite3.connect(':memory:')
    with open(sql_file, 'r') as f:
      self.db.executescript(f.read())

  @property
  def availableArchetypes(self):
    return [row[0] for row in self.db.execute('SELECT * FROM Archetypes')]

  @property
  def availableClans(self):
    return [row[0] for row in self.db.execute('SELECT * FROM Clans')]

  @property
  def availableDisciplines(self):
    return [row[0] for row in self.db.execute('SELECT * FROM Disciplines')]

  @property
  def name(self):
    return [row[0] for row in self.db.execute('SELECT Name FROM Vampire')][0]

  @name.setter
  def name(self, name):
    self.db.execute('UPDATE Vampire SET Name = ?', (name,))

  @property
  def nature(self):
    return [row[0] for row in self.db.execute('SELECT Nature FROM Vampire')][0]

  @nature.setter
  def nature(self, name):
    self.db.execute('UPDATE Vampire SET Nature = ?', (name,))

  @property
  def concept(self):
    return [row[0] for row in self.db.execute('SELECT Concept FROM Vampire')][0]

  @concept.setter
  def concept(self, name):
    self.db.execute('UPDATE Vampire SET Concept = ?', (name,))

  @property
  def demeanor(self):
    return [row[0] for row in self.db.execute('SELECT Demeanor FROM Vampire')][0]

  @demeanor.setter
  def demeanor(self, name):
    self.db.execute('UPDATE Vampire SET Demeanor = ?', (name,))

  @property
  def clan(self):
    return [row[0] for row in self.db.execute('SELECT Clan FROM Vampire')][0]

  @clan.setter
  def clan(self, name):
    self.db.execute('UPDATE Vampire SET Clan = ?', (name,))



  def getTraits(self, category = None):
    if category:
      traits = []
      for row in self.db.execute('SELECT Name FROM TraitValues WHERE Type = ?', (category,)):
        traits.append(row[0])
      return traits
    else:
      traits = []
      for row in self.db.execute('SELECT Name FROM TraitValues'):
        traits.append(row[0])
      return traits

  def getTrait(self, trait):
    for row in self.db.execute('SELECT Dots FROM TraitValues WHERE Name = ?', (trait,)):
      return row[0]

  def getTraitDots(self, trait):
    dots = {
      BASE: 0,
      CREATION: 0,
      FREEBIE: 0,
      XP: 0
    }
    for row in self.db.execute(
      'SELECT Type, COUNT(Type) FROM Dots WHERE Trait = ? GROUP BY Type ORDER BY TYPE ASC',
      (trait,)):
      dots[row[0]] = row[1]
    return (dots[BASE], dots[CREATION], dots[FREEBIE], dots[XP])


  def getTraitType(self, trait):
    try:
      return list(
        self.db.execute('SELECT Type FROM Traits WHERE Name = ? LIMIT 1', (trait,))
      )[0][0]
    except IndexError:
      return None

  def dotsAvailable(self, trait, dottype = CREATION):
    if trait in ATTRIBUTE_CATEGORIES + ABILITY_CATEGORIES:
      category = trait
      trait = None
    else:
      category = self.getTraitType(trait)
      if not category: raise ValueError("Trait \"{}\" has no category!".format(trait))

    if dottype == CREATION:
      if category in ATTRIBUTE_CATEGORIES:
        return [7, 5, 3][
          self.attributeOrdering.index(category)] - self.dotsSpent(category, dottype)
      if category in ABILITY_CATEGORIES:
        available = [13, 9, 5][
          self.abilityOrdering.index(category)
        ] - self.dotsSpent(category, dottype)

        if trait:
          _, spent, _, _ = self.getTraitDots(trait)
          return max(0, min(3 - spent, available)) # cap by 3 per talent
        else:
          return available
      raise ValueError('category ({}) not found'.format(category))
    elif dottype == FREEBIE:
      #TODO: implement Freebie limits
      return 0
    else:
      raise ValueError("Unknown Dottype! ({})".format(dottype))

  def spendDot(self, trait, dottype=None, amount = 1):
    if amount > 0:
      if dottype == None:
        creation_avail = self.dotsAvailable(trait, CREATION)
        if creation_avail > 0:
          spend = min(amount, creation_avail)
          self.spendDot(trait, CREATION, spend)
          self.spendDot(trait, None, amount - spend)
        elif self.dotsAvailable(trait, FREEBIE) > 0:
          spend = min(amount, self.dotsAvailable(trait, FREEBIE))
          self.spendDot(trait, FREEBIE, spend)
          self.spendDot(trait, None, amount - spend)
        else:
          self.spendDot(trait, XP, amount)          
      else:
        if dottype in [CREATION, FREEBIE] and self.dotsAvailable(trait, dottype) < amount: 
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
      amount -= self.deleteDot(trait, XP, amount)
      amount -= self.deleteDot(trait, FREEBIE, amount)
      amount -= self.deleteDot(trait, CREATION, amount)
      return first_amount - amount

  def dotsSpent(self, category, dottype = CREATION):
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
