import json, os
from slugify import slugify


frontmatter = """---
name: "{}"
---

{}

#  Level 1
{}

# Level 2
{}

# Level 3
{}

# Level 4
{}

# Level 5
{}
"""

for d in ['assamite', 'koldunic', 'necromanty', 'thaumaturgy']:
  os.makedirs(d, exist_ok=True)

with open('VtM20_Lookup_Sorcery_Paths.json', 'r') as f:
  sorpaths = json.load(f)
  for spath in sorpaths:
    slug = slugify(spath['Name'])

    content = frontmatter.format(
      spath['Name'],
      spath['Descr'],
      spath['Level1'],
      spath['Level2'],
      spath['Level3'],
      spath['Level4'],
      spath['Level5']
    )
    if spath['IsAssam'] == "1":
      path = os.path.join('assamite', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if spath['IsKoldu'] == "1":
      path = os.path.join('koldunic', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if spath['IsAssam'] == "1":
      path = os.path.join('necromanty', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if spath['IsAssam'] == "1":
      path = os.path.join('thaumaturgy', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)
