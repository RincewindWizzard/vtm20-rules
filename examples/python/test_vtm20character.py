#/usr/bin/python3
import sqlite3
import unittest
from vtm20character import VtM20Character

class TestVtM20(unittest.TestCase):
  def setUp(self):
    self.vamp = VtM20Character()

  def tearDown(self):
    del self.vamp

  def test_dotsavailable(self):
    ordering = self.vamp.attributeOrdering
    self.assertEqual(len(ordering), 3)

    self.vamp.spendDot('Strength', 'Creation', 3)
    self.assertEqual(self.vamp.attributeOrdering[0], 'Physical')

    self.vamp.spendDot('Charisma', 'Creation', 2)
    self.assertEqual(self.vamp.attributeOrdering[1], 'Social')
    self.assertEqual(self.vamp.attributeOrdering[2], 'Mental')

    for trait in self.vamp.getTraits():
      if self.vamp.getTraitType(trait) in ['Physical', 'Social', 'Mental']:
        print(trait, self.vamp.getTrait(trait), self.vamp.dotsAvailable(trait))

  def test_traits(self):
    for trait in self.vamp.getTraits():
      dots = self.vamp.getTrait(trait)
      self.vamp.spendDot(trait, 'XP', 2)
      self.assertEqual(self.vamp.getTrait(trait), dots + 2)
      self.vamp.deleteDot(trait, 'XP')
      self.assertEqual(self.vamp.getTrait(trait), dots + 1)

      with self.assertRaises(sqlite3.IntegrityError):
        self.vamp.spendDot(trait, 'Creationa')

    with self.assertRaises(ValueError):
      self.vamp.spendDot('FOOO', 'Creation')

    
if __name__ == '__main__':
    unittest.main()
