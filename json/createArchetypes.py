import json, os
from slugify import slugify

def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')


frontmatter = """---
Name: "{}"
---

{}"""


with open('VtM20_Lookup_Archetypes.json', 'r') as f:
  abilities = json.load(f)
  for ability in abilities:
    slug = slugify(ability['Name'])
    path = slug+'.md'
    with open(path, 'w') as md:
      md.write(frontmatter.format(
        ability['Name'],
        to_md(ability['Descr'])
      ))
     
  
