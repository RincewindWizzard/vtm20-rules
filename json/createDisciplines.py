import json, os
from collections import namedtuple
import pprint
from slugify import slugify
frontmatter = """---
name: {}
is_sorcery: {}
---
{}"""

pp = pprint.PrettyPrinter(indent=4)
def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')

Discipline = namedtuple('Discipline', ['name', 'sorcery', 'powers', 'description'])
Power = namedtuple('Power', ['name', 'discipline', 'level', 'description'])

ds = {}
with open('VtM20_Lookup_Disciplines.json', 'r') as f:
  disciplines = json.load(f)
  for disc in disciplines:
    slug = disc['Name'].lower()
    ds[slug] = Discipline(disc['Name'], disc['IsSorc'] == 1, [], to_md(disc['Descr']))
    #disc['Name'],
    #disc['IsSorc'] == 1,
    #to_md(disc['Descr'])

with open('VtM20_Lookup_Disciplines_Powers.json', 'r') as f:
  powers = json.load(f)
  for power in powers:
    discipline = ds[power['Discipline'].lower()]
    power = Power(power['Name'], power['Discipline'].lower(), power['Level'], to_md(power['Descr']))
    discipline.powers.append(power)

def power_str(power):
  return "Power(\n        name='{}',\n        discipline='{}',\n        level={},\n        description=\"\"\"{}\"\"\"\n      )".format(power.name, power.discipline, power.level, power.description)

print("Discipline = namedtuple('Discipline', ['name', 'sorcery', 'powers', 'description']")
print("Power = namedtuple('Power', ['name', 'discipline', 'level', 'description'])")
print("disciplines = [")
for k in ds:
  d = ds[k]
  pwstr = ',\n      '.join(power_str(p) for p in d.powers)
  print("  Discipline(\n    name='{}',\n    sorcery={},\n    powers= [\n      {}\n    ],\n    description=\"\"\"{}\"\"\"\n  ),".format(d.name, d.sorcery, pwstr, d.description))
print("]")


frontmatter = """---
name: {}
---

{}"""
"""
with open('VtM20_Lookup_Disciplines_Powers.json', 'r') as f:
  powers = json.load(f)
  for power in powers:
    slug = slugify(power['Discipline'])
    level = power['Level']

    path = os.path.join(slug, 'powers', 'level-{}'.format(level))
    powermd = os.path.join(path, slugify(power['Name'])+'.md')
    os.makedirs(path, exist_ok=True)
    with open(powermd, 'w') as pf:
      pf.write(frontmatter.format(
        power['Name'],
        to_md(power['Descr'])
      ))
"""
