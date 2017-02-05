import json, os
from slugify import slugify

discipline_ids = {1: 'animalism', 2: 'auspex', 3: 'celerity', 4: 'chimerstry', 5: 'dementation', 6: 'dominate', 7: 'fortitude', 8: 'necromancy', 9: 'obfuscate', 10: 'obtenebration', 11: 'potence', 12: 'presence', 13: 'protean', 14: 'quietus', 15: 'serpentis', 16: 'thaumaturgy', 17: 'vicissitude', 18: 'assamite-sorcery', 19: 'bardo', 20: 'daimoinon', 21: 'flight', 22: 'koldunic-sorcery', 23: 'melpominee', 24: 'mytherceria', 25: 'obeah', 26: 'ogham', 27: 'sanguinus', 28: 'spiritus', 29: 'temporis', 30: 'thanatosis', 31: 'valeren', 32: 'visceratika', 33: 'countermagic', 99: 'any'}

def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')


frontmatter = """---
Name: "{}"
disciplines: {}
weakness: "{}"
weakness_description: "{}"
---

{}"""


with open('VtM20_Lookup_Clans.json', 'r') as f:
  clans = json.load(f)
  for clan in clans:
    slug = slugify(clan['Name'])
    path = slug+'.md'

    disciplines = [ 
      discipline_ids[int(clan[dkey])]
      for dkey in ['ClanDiscID1', 'ClanDiscID2', 'ClanDiscID3', 'ClanDiscID4']
      if clan[dkey]
    ]

    with open(path, 'w') as md:
      md.write(frontmatter.format(
        clan['Name'],
        disciplines,
        clan['WeaknessShort'],
        clan['WeaknessLong'],
        clan['Descr']
      ))
     
  
