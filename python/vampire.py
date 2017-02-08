#!/usr/bin/python3
from collections import namedtuple

from abilities import abilities, Ability
from disciplines import disciplines, Discipline
from backgrounds import backgrounds

# rules for each generation
Generation = namedtuple('Generation', ['number', 'blood_pool', 'stat_max', 'blood_per_turn'])
default_generation = 13
generation_rules = {
  1:  Generation(number=1,  blood_pool=500, stat_max=10, blood_per_turn=50), 
  2:  Generation(number=2,  blood_pool=250, stat_max=10, blood_per_turn=20), 
  3:  Generation(number=3,  blood_pool=100, stat_max=10, blood_per_turn=15), 
  4:  Generation(number=4,  blood_pool=50,  stat_max=9,  blood_per_turn=10), 
  5:  Generation(number=5,  blood_pool=40,  stat_max=8,  blood_per_turn=8), 
  6:  Generation(number=6,  blood_pool=30,  stat_max=7,  blood_per_turn=6), 
  7:  Generation(number=7,  blood_pool=20,  stat_max=6,  blood_per_turn=4), 
  8:  Generation(number=8,  blood_pool=15,  stat_max=5,  blood_per_turn=3), 
  9:  Generation(number=9,  blood_pool=14,  stat_max=5,  blood_per_turn=2), 
  10: Generation(number=10, blood_pool=13,  stat_max=5,  blood_per_turn=1), 
  11: Generation(number=11, blood_pool=12,  stat_max=5,  blood_per_turn=1), 
  12: Generation(number=12, blood_pool=11,  stat_max=5,  blood_per_turn=1), 
  13: Generation(number=13, blood_pool=10,  stat_max=5,  blood_per_turn=1), 
  14: Generation(number=14, blood_pool=10,  stat_max=5,  blood_per_turn=1), 
  15: Generation(number=15, blood_pool=10,  stat_max=5,  blood_per_turn=1)
}




class BoundedInt(property):
  """
  * This class behaves like a int property, which is checked against the lower and upper bound
  """
  def __init__(self, lower, upper, doc=None):
    property.__init__(self, self.fget, self.fset, doc=doc)
    self.min = lower
    self.max = upper
    self._value = lower

  def fget(self, container):
    return self._value

  def fset(self, container, v):
    if (self.min and v < self.min) or (self.max and v > self.max):
      raise ValueError("{} is out of bounds! [{},{}]".format(v, self.min, self.max))
    self._value = v

class CharacterAttribute(BoundedInt):
  def __init__(self, doc=None):
    BoundedInt.__init__(self, 1, None, doc)

  def fset(self, vampire, value):
    if value > vampire.stat_max:
      raise ValueError("{} is to high for attribute!".format(value))
    BoundedInt.fset(self, vampire, value)
    

class CheckedDict(dict):
  def __init__(self, valid_keys, valid_values):
    dict.__init__(self)
    self._valid_keys   = valid_keys
    self._valid_values = valid_values
    default = min(valid_values)
    for key in valid_keys:
      self[key] = default

  def __getitem__(self, key):
    key = key.name if hasattr(key, 'name') else key
    return dict.__getitem__(self, key)

  def __setitem__(self, key, value):
    key = key.name if hasattr(key, 'name') else key
    if not key in self._valid_keys:
      raise ValueError("Unknown Key!")
    if not value in self._valid_values:
      raise ValueError("Value out of range!")
    dict.__setitem__(self, key, value)

class Vampire(object):

  attributes = [
    'strength', 'dexterity', 'stamina', 
    'charisma', 'manipulation', 'appearance',
    'perception', 'intelligence', 'wits'
  ]

  # virtues
  conscience   = BoundedInt(1, 5, "Conscience of your Character")
  self_control = BoundedInt(1, 5, "Self-control of your Character")
  courage      = BoundedInt(1, 5, "Courage of your Character")


  def __init__(self, *kwargs):
    self._generation     = default_generation
    for attr in Vampire.attributes:
      setattr(Vampire, attr, CharacterAttribute(attr + " of your character"))

    self._humanity       = 0
    self._willpower      = 0
    self._blood_pool     = 0
    self._blood_pool_max = 0

    self.abilities   = CheckedDict(abilities.keys(), range(6))
    self.disciplines = CheckedDict(disciplines.keys(), range(11))
    self.backgrounds = CheckedDict(backgrounds.keys(), range(6))

  @property
  def stat_max(self):
    return generation_rules[self.generation].stat_max

  @property
  def blood_per_turn(self):
    return generation_rules[self.generation].blood_per_turn

  @property
  def blood_pool_max(self):
    return generation_rules[self.generation].blood_pool

  @property
  def blood_pool(self):
    return self._blood_pool

  @blood_pool.setter
  def blood_pool(self, value):
    if value > self.blood_pool_max:
      raise ValueError("Not enough blood capacity! {} > {}".format(value, self.blood_pool_max))
    elif value < 0:
      raise ValueError("Negative blood pool is impossible!")
    self._blood_pool = value

  @property
  def generation(self):
    return self._generation

  @generation.setter
  def generation(self, value):
    """Set generation of vampire and adjust all stats, that are too high"""
    self._generation = value

    for attr in Vampire.attributes:
      setattr(self, attr, min(getattr(self, attr), self.stat_max))

    self.blood_pool = min(self.blood_pool_max, self.blood_pool)




