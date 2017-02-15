#!/usr/bin/python3
import unittest
import vampire
from vampire import Vampire
from abilities import abilities, Ability
from disciplines import disciplines
from backgrounds import backgrounds

class TestVampire(unittest.TestCase):
  def test_prop(self):
    v = Vampire()
    v.generation = 10
    self.assertEqual(v.strength, 1)

    for i in range(1, 6):
      v.strength = i
      v.dexterity = i
      v.stamina = i
      v.charisma = i
      v.manipulation = i
      v.appearance = i
      v.perception = i
      v.intelligence = i
      v.wits = i
      self.assertEqual(v.strength, i)
      self.assertEqual(v.dexterity, i)
      self.assertEqual(v.stamina, i)

      self.assertEqual(v.charisma, i)
      self.assertEqual(v.manipulation, i)
      self.assertEqual(v.appearance, i)

      self.assertEqual(v.appearance, i)
      self.assertEqual(v.perception, i)
      self.assertEqual(v.intelligence, i)

    def foo(): v.strength = 6
    self.assertRaises(ValueError, foo)


    v.generation = 1
    for i in range(1, 11):
      v.strength = i
      self.assertEqual(v.strength, i)

    def foo(): v.strength = 11
    self.assertRaises(ValueError, foo)

  def test_generation(self): 
    v = Vampire()
    v.generation = 1
    v.strength = v.stat_max
    v.dexterity = v.stat_max
    v.stamina = v.stat_max
    v.charisma = v.stat_max
    v.manipulation = v.stat_max
    v.appearance = v.stat_max
    v.perception = v.stat_max
    v.intelligence = v.stat_max
    v.wits = v.stat_max

    for i in range(1, 16):
      v.generation = i
      self.assertEqual(v.strength, v.stat_max)
      self.assertEqual(v.dexterity, v.stat_max)
      self.assertEqual(v.stamina, v.stat_max)
      self.assertEqual(v.charisma, v.stat_max)
      self.assertEqual(v.manipulation, v.stat_max)
      self.assertEqual(v.appearance, v.stat_max)
      self.assertEqual(v.perception, v.stat_max)
      self.assertEqual(v.intelligence, v.stat_max)
      self.assertEqual(v.wits, v.stat_max)

  def test_abilities(self):
    v = Vampire()
    value = 3
    alertness = abilities['Alertness']

    v.abilities[alertness] = value
    self.assertEqual(v.abilities[alertness], value)

    for ability in abilities.values():
      v.abilities[ability] = 1

    def foo(): v.abilities[alertness] = 6
    self.assertRaises(ValueError, foo)

    def foo(): v.abilities[Ability("foo", '', [], '')] = 1
    self.assertRaises(ValueError, foo)

  def test_disciplines(self):
    v = Vampire()
    presence = disciplines['Presence']
    value = 6
    v.disciplines[presence] = value
    self.assertEqual(v.disciplines[presence], value)

    def foo(): v.disciplines[presence] = 11
    self.assertRaises(ValueError, foo)

  def test_backgrounds(self):
    v = Vampire()
    allies = backgrounds['Allies']
    value = 5
    v.backgrounds[allies] = value
    self.assertEqual(v.backgrounds[allies], value)

    def foo(): v.backgrounds[allies] = 6
    self.assertRaises(ValueError, foo)

if __name__ == '__main__':
    unittest.main()
