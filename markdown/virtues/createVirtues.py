import json, os
from slugify import slugify

frontmatter = """---
name: "{}"
{}
---

{}"""


with open('VtM20_Lookup_Virtues.json', 'r') as f:
  virtues = json.load(f)
  for virtue in virtues:
    slug = slugify(virtue['Name'])
    path = slug+'.md'

    levels = ''
    for level in range(1, 11):
      if virtue['Level' + str(level)]:
        levels += 'level{}: "{}"\n'.format(level, virtue['Level' + str(level)])

    with open(path, 'w') as md:
      md.write(frontmatter.format(
        virtue['Name'],
        levels,
        virtue['Descr']
      ))

