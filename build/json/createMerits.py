import json, os
from slugify import slugify


frontmatter = """---
name: "{}"
type: "{}"
cost: {}
is_multi_buy: {}
---

{}"""


with open('VtM20_Lookup_Merits.json', 'r') as f:
  merits = json.load(f)
  for merit in merits:
    slug = slugify(merit['Name'])
    path = slug+'.md'


    with open(path, 'w') as md:
      md.write(frontmatter.format(
        merit['Name'],
        merit['MType'],
        merit['Cost'],
        int(merit['IsMultiBuy']) == 1,
        merit['Descr']
      ))
     
  
