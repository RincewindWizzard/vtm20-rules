import json, os
from slugify import slugify


frontmatter = """---
name: "{}"
nickname:  "{}"
virtues:   "{}"
bearing:   "{}"
---

# Beliefs
{}

# Ethics
{}

# History
{}

# Practices
{}

# Followers
{}

# Following
{}

# Abilities
{}

# Preferred Disciplines
{}

# Sins
{}
"""


with open('VtM20_Lookup_Morality.json', 'r') as f:
  moralities = json.load(f)
  for morality in moralities:
    slug = slugify(morality['Name'])
    path = slug+'.md'


    with open(path, 'w') as md:
      md.write(frontmatter.format(
        morality['Name'],
        morality['Nickname'],
        morality['Virtues'],
        morality['Bearing'],
        morality['Beliefs'],
        morality['Ethics'],
        morality['History'],
        morality['Practices'],
        morality['Followers'],
        morality['Following'],
        morality['Abilities'],
        morality['PrefDisc'],
        morality['Sins']
      ))
     
  
