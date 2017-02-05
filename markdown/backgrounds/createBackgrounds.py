import json, os
from slugify import slugify

def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')


frontmatter = """---
Name: "{}"
{}
---

{}"""


with open('VtM20_Lookup_Backgrounds.json', 'r') as f:
  bgs = json.load(f)
  for bg in bgs:
    slug = slugify(bg['Name'])
    path = slug+'.md'

    levels = ''    
    for i in range(1, 10):
      level = 'Level{}'.format(i)
      if bg[level]:
        levels += '{}: "{}"\n'.format(level, bg[level])

    with open(path, 'w') as md:
      md.write(frontmatter.format(
        bg['Name'],
        levels,
        to_md(bg['Descr'])
      ))
     
  
