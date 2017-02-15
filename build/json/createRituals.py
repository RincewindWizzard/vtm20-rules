import json, os
from slugify import slugify


frontmatter = """---
name: "{}"
---

{}
"""

for d in ['assamite', 'koldunic', 'necromanty', 'thaumaturgy']:
  os.makedirs(d, exist_ok=True)

with open('VtM20_Lookup_Sorcery_Rituals.json', 'r') as f:
  rituals = json.load(f)
  for ritual in rituals:
    slug = slugify(ritual['Name'])

    content = frontmatter.format(
      ritual['Name'],
      ritual['Descr'],
    )
    if ritual['IsAssam'] == "1":
      path = os.path.join('assamite', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if ritual['IsKoldu'] == "1":
      path = os.path.join('koldunic', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if ritual['IsAssam'] == "1":
      path = os.path.join('necromanty', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)

    if ritual['IsAssam'] == "1":
      path = os.path.join('thaumaturgy', slug+'.md')
      with open(path, 'w') as md:
        md.write(content)
