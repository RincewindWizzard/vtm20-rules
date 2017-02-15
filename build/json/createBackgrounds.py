import json, os
from slugify import slugify

def to_md(s):
  return s.replace('<p>', '\n').replace('</p>', '\n').replace('<br>', '\n').replace('<b>', '_').replace('</b>', '_')


frontmatter = """---
Name: "{}"
{}
---

{}"""
from collections import namedtuple
Background = namedtuple('Background', ['name', 'levels', 'description'])

backgrounds = []

print("[")
with open('VtM20_Lookup_Backgrounds.json', 'r') as f:
  for bg in json.load(f):
    levels = []   
    for i in range(1, 10):
      level = 'Level{}'.format(i)
      if bg[level]:
        levels.append("'{}'".format(bg[level]))

    #backgrounds.append(Background(bg['Name'], levels, to_md(bg['Descr'])))
    print('  Background(\n    name = "{}",\n    levels = [\n      {}\n    ],\n    description = """{}"""\n  ),'.format(bg['Name'], ',\n      '.join(levels), to_md(bg['Descr'])))

