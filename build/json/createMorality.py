import json, os
from slugify import slugify


frontmatter = """---
name: "{}"
nickname:  "{}"
virtues:   "{}"
bearing:   "{}"
sins: {}
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
"""

def table_to_json(tb):
  src = tb
  repl = [
    ('<table>', '['),
    ('<tr>', '['),
    ('<th>', '"'),
    ('</th>', '", '),
    ('</tr>', '], '),
    ('<td>', '"'),
    ('</td>', '", '),
    (', ]', ']'),
    (', </table>', ']')
  ]
  
  for a, b in repl:
   tb = tb.replace(a, b)
  if tb == 'Sins':
    return None
  else:
    return json.loads(tb)

with open('VtM20_Lookup_Morality.json', 'r') as f:
  moralities = json.load(f)
  for morality in moralities:
    slug = slugify(morality['Name'])
    path = os.path.join('../markdown/morality/', slug+'.md')

    sins = morality['Sins']
    sins = table_to_json(sins)
    if sins:
      sins = list(reversed([{ 'rating': int(row[0]), 'moral-guideline' : row[1], 'rationale': row[2]} for row in sins[1:]]))

    with open(path, 'w') as md:
      md.write(frontmatter.format(
        morality['Name'],
        morality['Nickname'],
        morality['Virtues'],
        morality['Bearing'],
        sins,
        morality['Beliefs'],
        morality['Ethics'],
        morality['History'],
        morality['Practices'],
        morality['Followers'],
        morality['Following'],
        morality['Abilities'],
        morality['PrefDisc']
      ))
     
  
