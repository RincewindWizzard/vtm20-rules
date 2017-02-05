import json, os
from slugify import slugify

def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')


frontmatter = """---
Name: {}
Level1: "{}"
Level2: "{}"
Level3: "{}"
Level4: "{}"
Level5: "{}"
---

{}"""


with open('VtM20_Lookup_Attributes.json', 'r') as f:
  abilities = json.load(f)
  for ability in abilities:
    slug = slugify(ability['Name'])
    path = os.path.join(slugify(ability['AType']), slug+'.md')
    with open(path, 'w') as md:
      md.write(frontmatter.format(
        ability['Name'],
        ability['Level1'],
        ability['Level2'],
        ability['Level3'],
        ability['Level4'],
        ability['Level5'],
        to_md(ability['Descr'])
      ))
     
  
