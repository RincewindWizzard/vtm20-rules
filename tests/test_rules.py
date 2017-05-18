#/usr/bin/python3
import unittest
import os
import sys
import timeit
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vtm20.rules import VtM20Rules, rules

class TestVtM20Rules(unittest.TestCase):
  def test_backgrounds(self):
    rules = VtM20Rules()
    self.assertTrue(
      timeit.timeit(
        'rules.backgrounds', 
        number=100000, 
        globals={'rules': rules}) < 10)

  def test_archetypes(self):
    archetypes = rules.archetypes
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
      self.assertTrue(archetype in [a.name for a in archetypes])

  def test_clans(self):
    clans = rules.clans
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
      self.assertTrue(clan in [c.name for c in clans])

  def test_disciplines(self):
    disciplines = rules.disciplines
    for discipline in [
      'Koldunic Sorcery', 'Daimoinon', 'Celerity', 'Animalism', 'Mytherceria', 'Vicissitude',
      'Protean', 'Obeah', 'Temporis', 'Dementation', 'Visceratika', 'Chimerstry', 'Auspex',
      'Fortitude', 'Quietus', 'Thaumaturgy', 'Countermagic', 'Obfuscate', 'Flight',
      'Obtenebration', 'Sanguinus', 'Necromancy', 'Valeren', 'Presence', 'Ogham', 'Dominate',
      'Potence', 'Bardo', 'Assamite Sorcery', 'Spiritus',
      'Thanatosis', 'Melpominee', 'Serpentis']:
      self.assertTrue(discipline in [ d.name for d in disciplines], msg=discipline)

if __name__ == '__main__':
  unittest.main()
