import json, os
from slugify import slugify
frontmatter = """---
name: {}
is_sorcery: {}
---
{}"""


def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')

with open('VtM20_Lookup_Disciplines.json', 'r') as f:
  disciplines = json.load(f)
  for disc in disciplines:
    slug = slugify(disc['Name'])
    print(slug)
    os.makedirs(slug, exist_ok=True)
    with open(os.path.join(slug, slug + '.md'), 'w') as md:
      md.write(
        frontmatter.format(
          disc['Name'],
          disc['IsSorc'] == 1,
          to_md(disc['Descr'])
        )
      )



frontmatter = """---
name: {}
---

{}"""

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

