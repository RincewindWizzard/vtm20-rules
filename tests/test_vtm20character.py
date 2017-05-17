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

  def test_archetypes(self):
    vamp = VtM20Character()
    archetypes = vamp.availableArchetypes
    for archetype in [
      'Cavalier', 'Capitalist', 'Deviant', 'Judge', 
      'Pedagogue', 'Curmudgeon', 'Penitent', 'Celebrant', 
      'Director', 'Eye of the Storm', 'Creep Show', 'Traditionalist', 
      'Fanatic', 'Conniver', 'Loner', 'Monster', 'Rebel', 
      'Architect', 'Sadist', 'Autocrat', 'Trickster', 'Guru', 'Competitor', 
      'Gallant', 'Child', 'Caregiver', 'Masochist', 'Rogue', 'Thrill-Seeker', 
      'Perfectionist', 'Idealist', 'Bravo', 'Soldier', 'Chameleon', 'Conformist', 
      'Bon Vivant', 'Martyr', 'Sociopath', 'Survivor', 
      'Scientist', 'Dabbler', 'Enigma', 'Visionary']:
      self.assertTrue(archetype in archetypes)

  def test_clans(self):
    vamp = VtM20Character()
    clans = vamp.availableClans
    for clan in [
      'Telyavelic Tremere', 'Lhiannan', 'Toreador', 'Brujah Antitribu', 'City Gangrel',
      'Panders', 'Lasombra Antitribu', 'Kiasyd', 'Harbingers of Skulls',
      'Angellis Ater (Potence)', 'Ahrimanes', 'Giovanni', 'Daitya', 'Gargoyles',
      'Warrior Setites', 'Tremere Antitribu', 'Lasombra', 'Caitiff',
      'Angellis Ater (Presence)', 'Cappadocians', 'Ravnos', 'Assamite Sorcerers',
      'Ventrue Antitribu (Auspex)', 'Daughters of Cacophony', 'Salubri', 'Ravnos Antitribu',
      'Malkavian Antitribu', 'Brahman', 'Wu Zao (Obeah)', 'Ventrue', 'Tremere', 'Malkavian',
      'Assamite Antitribu', 'Assamite Viziers', 'Noiad', 'Children of Osiris', 'Assamite',
      'Blood Brothers', 'Toreador Antitribu', 'Wu Zao (Valeren)', 'Followers of Set',
      'Gangrel', 'Anda', 'Mariners', 'Country Gangrel', 'Nagaraja',
      'Angellis Ater (Obtenebration)', 'Lamia', 'Salubri Antitribu', 'Dominate Malkavians',
      'Brujah', 'Baali', 'Kolduns', 'Old Clan Tzimisce', 'Tzimisce', 'Samedi', 'True Brujah',
      'Tlacique', 'Nosferatu Antitribu', 'Nosferatu', 'Ventrue Antitribu (Presence)',
      'Serpents of the Light']:
      self.assertTrue(clan in clans)

  def test_disciplines(self):
    vamp = VtM20Character()
    disciplines = vamp.availableDisciplines
    for discipline in [
      'Koldunic Sorcery', 'Daimoinon', 'Celerity', 'Animalism', 'Mytherceria', 'Vicissitude',
      'Protean', 'Obeah', 'Temporis', 'Dementation', 'Visceratika', 'Chimerstry', 'Auspex',
      'Fortitude', 'Quietus', 'Thaumaturgy', 'Countermagic', 'Obfuscate', 'Flight',
      'Obtenebration', 'Sanguinus', 'Necromancy', 'Valeren', 'Presence', 'Ogham', 'Dominate',
      'Potence', 'Bardo', 'Assamite Sorcery', 'Spiritus',
      'Thanatosis', 'Melpominee', 'Serpentis']:
      self.assertTrue(discipline in disciplines)

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
