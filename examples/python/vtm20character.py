#/usr/bin/python3
import sqlite3

sql_file = '../sqlite/CharacterCreation.sql'


class VtM20Character(object):
  def __init__(self):
    self.db = sqlite3.connect(':memory:')
    with open(sql_file, 'r') as f:
      self.db.executescript(f.read())
  
  def getTraits(self):
    traits = []
    for row in self.db.execute('SELECT Name FROM Traits'):
      traits.append(row[0])
    return traits

  def getTrait(self, trait):
    for row in self.db.execute('SELECT Dots FROM Traits WHERE Name = ?', (trait,)):
      return row[0]

  def getTraitType(self, trait):
    try:
      return list(
        self.db.execute('SELECT Type FROM TraitCategories WHERE Name = ?', (trait,))
      )[0][0]
    except IndexError:
      return None

  def dotsAvailable(self, trait, dottype = 'Creation'):
    category = self.getTraitType(trait)
    if category in ['Physical', 'Social', 'Mental']:
      return [7, 5, 3][self.attributeOrdering.index(category)] - self.dotsSpent(category, dottype)
    return 0;

  def spendDot(self, trait, dottype, amount = 1):
    if dottype in ['Creation', 'Freebie'] and self.dotsAvailable(trait, dottype) < amount: 
      raise ValueError("Not enough dots available! {} < {}".format(
        self.dotsAvailable(trait, dottype), amount))

    for i in range(amount):
      self.db.execute('INSERT INTO Dots (Type, Trait) VALUES (?, ?)', (dottype, trait))

  def deleteDot(self, trait, dottype, amount = 1):
    return self.db.execute(
      'DELETE FROM Dots WHERE Type = ? AND Trait = ? LIMIT ?', 
      (dottype, trait, amount)
    ).rowcount == 1

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

  def __del__(self):
    self.db.close()
