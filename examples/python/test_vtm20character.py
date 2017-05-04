#/usr/bin/python3
import sqlite3
import unittest
from vtm20character import VtM20Character

class TestVtM20(unittest.TestCase):
  def setUp(self):
    ...

  def tearDown(self):
    ...

  def test_attr_dotsavailable(self):
    vamp = VtM20Character()
    ordering = vamp.attributeOrdering
    self.assertEqual(len(ordering), 3)

    vamp.spendDot('Strength', 'Creation', 3)
    self.assertEqual(vamp.attributeOrdering[0], 'Physical')

    vamp.spendDot('Charisma', 'Creation', 2)
    self.assertEqual(vamp.attributeOrdering[1], 'Social')

    vamp.spendDot('Wits', 'Creation', 1)
    self.assertEqual(vamp.attributeOrdering[2], 'Mental')

    self.assertEqual(vamp.attributeOrdering, ['Physical', 'Social', 'Mental'])

    self.assertEqual(vamp.dotsAvailable('Physical'), 4)
    self.assertEqual(vamp.dotsAvailable('Social'), 3)
    self.assertEqual(vamp.dotsAvailable('Mental'), 2)

  def test_ability_dotsavailable(self):
    vamp = VtM20Character()
    vamp.spendDot('Alertness', 'Creation', 3)
    vamp.spendDot('Animal Ken', 'Creation', 2)
    vamp.spendDot('Academics', 'Creation', 1)
    self.assertEqual(vamp.abilityOrdering, ['Talent', 'Skill', 'Knowledge'])
    vamp.spendDot('Computer', 'Creation', 2)
    self.assertTrue(vamp.dotsAvailable('Knowledge') >= 2)
    self.assertEqual(vamp.dotsAvailable('Computer'), 1)
    vamp.spendDot('Computer', 'Creation', 1)
    self.assertEqual(vamp.abilityOrdering, ['Knowledge', 'Talent', 'Skill'])

    self.assertEqual(
      [9, 6, 3], 
      [vamp.dotsAvailable(x) for x in ['Knowledge', 'Talent', 'Skill']]
    )

  def test_spending_algorithm(self):
    vamp = VtM20Character()
    vamp.spendDot('Brawl', amount=100)
    self.assertEqual(vamp.getTrait('Brawl'), 100)
    self.assertEqual(vamp.dotsAvailable('Brawl', 'Creation'), 0)
    self.assertEqual(vamp.dotsAvailable('Brawl', 'Freebie'), 0)
    base, creation, freebie, xp = vamp.getTraitDots('Brawl')

    self.assertEqual((base, creation, freebie, xp), (0, 3, 0, 97))

  def test_traits(self):
    vamp = VtM20Character()
    for trait in vamp.getTraits():
      dots = vamp.getTrait(trait)
      vamp.spendDot(trait, 'XP', 2)
      self.assertEqual(vamp.getTrait(trait), dots + 2)
      vamp.deleteDot(trait, 'XP')
      self.assertEqual(vamp.getTrait(trait), dots + 1)

      with self.assertRaises(sqlite3.IntegrityError):
        vamp.spendDot(trait, 'Creationa')

    with self.assertRaises(ValueError):
      vamp.spendDot('FOOO', 'Creation')

    
if __name__ == '__main__':
    unittest.main()
