#/usr/bin/python3
import sqlite3
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vtm20.vtm20character import VtM20Character
from vtm20.vtm20character import FREEBIE, CREATION, PHYSICAL, SOCIAL, MENTAL, XP, TALENT, SKILL, KNOWLEDGE

class TestVtM20(unittest.TestCase):
  def setUp(self):
    ...

  def tearDown(self):
    ...

  def test_attr_dotsavailable(self):
    vamp = VtM20Character()
    ordering = vamp.attributeOrdering
    self.assertEqual(len(ordering), 3)

    vamp.spendDot('Strength', CREATION, 3)
    self.assertEqual(vamp.attributeOrdering[0], PHYSICAL)

    vamp.spendDot('Charisma', CREATION, 2)
    self.assertEqual(vamp.attributeOrdering[1], SOCIAL)

    vamp.spendDot('Wits', CREATION, 1)
    self.assertEqual(vamp.attributeOrdering[2], MENTAL)

    self.assertEqual(vamp.attributeOrdering, [PHYSICAL, SOCIAL, MENTAL])

    self.assertEqual(vamp.dotsAvailable(PHYSICAL), 4)
    self.assertEqual(vamp.dotsAvailable(SOCIAL), 3)
    self.assertEqual(vamp.dotsAvailable(MENTAL), 2)

  def test_ability_dotsavailable(self):
    vamp = VtM20Character()
    vamp.spendDot('Alertness', CREATION, 3)
    vamp.spendDot('Animal Ken', CREATION, 2)
    vamp.spendDot('Academics', CREATION, 1)
    self.assertEqual(vamp.abilityOrdering, [TALENT, SKILL, KNOWLEDGE])
    vamp.spendDot('Computer', CREATION, 2)
    self.assertTrue(vamp.dotsAvailable(KNOWLEDGE) >= 2)
    self.assertEqual(vamp.dotsAvailable('Computer'), 1)
    vamp.spendDot('Computer', CREATION, 1)
    self.assertEqual(vamp.abilityOrdering, [KNOWLEDGE, TALENT, SKILL])

    self.assertEqual(
      [9, 6, 3], 
      [vamp.dotsAvailable(x) for x in [KNOWLEDGE, TALENT, SKILL]]
    )

  def test_spending_algorithm(self):
    vamp = VtM20Character()
    vamp.spendDot('Brawl', amount=100)
    self.assertEqual(vamp.getTrait('Brawl'), 100)
    self.assertEqual(vamp.dotsAvailable('Brawl', CREATION), 0)
    self.assertEqual(vamp.dotsAvailable('Brawl', FREEBIE), 0)
    base, creation, freebie, xp = vamp.getTraitDots('Brawl')

    self.assertEqual((base, creation, freebie, xp), (0, 3, 0, 97))

  def test_traits(self):
    vamp = VtM20Character()
    for trait in vamp.getTraits():
      dots = vamp.getTrait(trait)
      vamp.spendDot(trait, XP, 2)
      self.assertEqual(vamp.getTrait(trait), dots + 2)
      vamp.deleteDot(trait, XP)
      self.assertEqual(vamp.getTrait(trait), dots + 1)

      with self.assertRaises(sqlite3.IntegrityError):
        vamp.spendDot(trait, 'Creationa')

    with self.assertRaises(ValueError):
      vamp.spendDot('FOOO', CREATION)

  def test_update_functions(self):
    vamp = VtM20Character()
    name = 'Guybrush Threepwood, mighty pirate'

    self.assertEqual('', vamp.name)
    vamp.name = name
    self.assertEqual(name, vamp.name)

    self.assertEqual('Architect', vamp.nature)
    vamp.nature = vamp.availableArchetypes[-1]
    self.assertEqual(vamp.availableArchetypes[-1], vamp.nature)

    self.assertEqual('Architect', vamp.concept)
    vamp.concept = vamp.availableArchetypes[-1]
    self.assertEqual(vamp.availableArchetypes[-1], vamp.concept)

    self.assertEqual('Architect', vamp.demeanor)
    vamp.demeanor = vamp.availableArchetypes[-10]
    self.assertEqual(vamp.availableArchetypes[-10], vamp.demeanor)

    self.assertEqual('Ventrue', vamp.clan)
    vamp.clan = vamp.availableClans[-1]
    self.assertEqual(vamp.availableClans[-1], vamp.clan)

    vamp.clan = 'fo'

    
if __name__ == '__main__':
    unittest.main()
