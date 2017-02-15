#!/usr/bin/python3
import os
from collections import namedtuple
import re

# third party libraries
import frontmatter
import simplejson as json

# Data types for the rules
Background = namedtuple('Background', ['name', 'levels', 'description'])
Merit = namedtuple('Merit', ['name', 'type', 'cost', 'is_multi_buy', 'description'])
Morality = namedtuple('Morality', ['name', 'nickname', 'virtues', 'bearing', 'sins', 'description'])
Sin = namedtuple('Sin', ['moral_guideline', 'rationale'])
Ability = namedtuple('Ability', ['name', 'type', 'levels', 'description'])
Archetype = namedtuple('Archetype', ['name', 'description'])
Clan = namedtuple('Clan', ['name', 'disciplines', 'weakness', 'weakness_description', 'description'])
Discipline = namedtuple('Discipline', ['name', 'sorcery', 'powers', 'description'])
Power = namedtuple('Power', ['name', 'level', 'description'])
Attribute = namedtuple('Atttribute', ['name', 'category', 'levels', 'description'])
Virtue = namedtuple('Virtue', ['name', 'levels', 'description'])
SorceryPath = namedtuple('SorceryPath', ['name', 'type', 'levels', 'description'])
Ritual = namedtuple('Ritual', ['name', 'type', 'description'])

rules_root = '../rules/'
background_path = os.path.join(rules_root, 'backgrounds')
merits_path = os.path.join(rules_root, 'merits')
morality_path = os.path.join(rules_root, 'morality')
abilities_path = os.path.join(rules_root, 'abilities')
archetypes_path = os.path.join(rules_root, 'archetypes')
clan_path = os.path.join(rules_root, 'clans')
disciplines_path = os.path.join(rules_root, 'disciplines')
attributes_path = os.path.join(rules_root, 'attributes')
virtues_path = os.path.join(rules_root, 'virtues')
sorcery_path = os.path.join(rules_root, 'sorcery_paths')
rituals_path = os.path.join(rules_root, 'sorcery_rituals')
dst_path = '../build/vtm20_rules.json'

def backgrounds():
  posts = []
  for mdfile in os.listdir(background_path):
    post = frontmatter.load(os.path.join(background_path, mdfile))
    posts.append(Background(
      name = post['Name'],
      levels = [
        post['Level1'],
        post['Level2'],
        post['Level3'],
        post['Level4'],
        post['Level5']
      ],
      description = post.content
    ))
  return posts

def merits():
  posts = []
  for mdfile in os.listdir(merits_path):
    post = frontmatter.load(os.path.join(merits_path, mdfile))
    posts.append(Merit(
      name = post['name'],
      type = post['type'],
      cost = post['cost'],
      is_multi_buy = post['is_multi_buy'],
      description = post.content
    ))
  return posts

def moralities():
  posts = []
  for mdfile in os.listdir(morality_path):
    post = frontmatter.load(os.path.join(morality_path, mdfile))

    posts.append(Morality(
      name = post['name'],
      nickname = post['nickname'],
      virtues = post['virtues'],
      bearing = post['bearing'],
      sins = dict( 
        (sin['rating'], Sin(sin['moral-guideline'], sin['rationale']))
        for sin in post['sins'] if sin 
      ) if post['sins'] else {},
      description = post.content
    ))
  return posts


def abilities():
  posts = []
  for category in os.listdir(abilities_path):
    path = os.path.join(abilities_path, category)
    for mdfile in os.listdir(path):
      post = frontmatter.load(os.path.join(path, mdfile))
      posts.append(Ability(
        name = post['Name'],
        type = category[:-1],
        levels = [
          post['Level1'],
          post['Level2'],
          post['Level3'],
          post['Level4'],
          post['Level5']
        ],
        description = post.content
      ))
  return posts

def archetypes():
  posts = []
  for mdfile in os.listdir(archetypes_path):
    post = frontmatter.load(os.path.join(archetypes_path, mdfile))

    posts.append(Archetype(
      name = post['Name'],
      description = post.content
    ))
  return posts
  

def clans():
  posts = []
  for mdfile in os.listdir(clan_path):
    post = frontmatter.load(os.path.join(clan_path, mdfile))
    posts.append(Clan(
      name = post['Name'],
      disciplines = post['disciplines'],
      weakness = post['weakness'],
      weakness_description = post['weakness_description'],
      description = post.content
    ))
  return posts

def disciplines():
  posts = []
  for discipline in os.listdir(disciplines_path):
    discipline = os.path.join(disciplines_path, discipline)
    for mdfile in os.listdir(discipline):
      if mdfile[-3:] == '.md':        
        post = frontmatter.load(os.path.join(discipline, mdfile))
        powers_path = os.path.join(discipline, 'powers')
        powers = []
        for level in os.listdir(powers_path):
          levelnum = int(level[-1:])
          level_path = os.path.join(powers_path, level)
          for mdfile in os.listdir(level_path):
            if mdfile[-3:] == '.md':
              power = frontmatter.load(os.path.join(level_path, mdfile))
              powers.append(Power(
                name = power['name'],
                level = levelnum,
                description = power.content
              ))

        posts.append(Discipline(
          name = post['name'],
          sorcery = post['is_sorcery'],
          powers = powers,
          description = post.content
        ))
      

  return posts
    
def attributes():
  posts = []
  for category in os.listdir(attributes_path):
    cat_path = os.path.join(attributes_path, category)
    for mdfile in os.listdir(cat_path):
      post = frontmatter.load(os.path.join(cat_path, mdfile))
      posts.append(Attribute(
        name = post['Name'],
        category = category,
        levels = [
          post['Level1'],
          post['Level2'],
          post['Level3'],
          post['Level4'],
          post['Level5']
        ],
        description = post.content
      ))
  return posts

def virtues():
  posts = []
  for mdfile in os.listdir(virtues_path):
    post = frontmatter.load(os.path.join(virtues_path, mdfile))

    posts.append(Virtue(
      name = post['name'],
      levels = [
        post['level1'],
        post['level2'],
        post['level3'],
        post['level4'],
        post['level5']
      ],
      description = post.content
    ))
  return posts

def sorcery_paths():
  posts = []
  rex = re.compile('# *Level \d')
  for category in os.listdir(sorcery_path):
    cat_path = os.path.join(sorcery_path, category)
    for mdfile in os.listdir(cat_path):
      post = frontmatter.load(os.path.join(cat_path, mdfile))
      levels = []
      chapters = rex.findall(post.content)
      for start, end in zip(chapters, chapters[1:]):
        start = post.content.find(start)
        end = post.content.find(end)
        levels.append(post.content[start:end])
      levels.append(post.content[post.content.find(chapters[-1]):])

      posts.append(SorceryPath(
        name = post['name'],
        type = category,
        levels = levels,
        description = post.content[:post.content.find(chapters[0])]
      ))
  return posts

def sorcery_rituals():
  posts = []
  for category in os.listdir(rituals_path):
    cat_path = os.path.join(rituals_path, category)
    for mdfile in os.listdir(cat_path):
      post = frontmatter.load(os.path.join(cat_path, mdfile))
      posts.append(Ritual(
        name = post['name'],
        type = category,
        description = post.content
      ))
  return posts

if __name__ == '__main__':
  rules = {
    'abilities': abilities(),
    'archetypes': archetypes(),
    'attributes': attributes(),
    'backgrounds': backgrounds(),
    'clans': clans(),
    'disciplines' : disciplines(),
    'merits': merits(),
    'moralities': moralities(),
    'virtues': virtues(),
    'sorcery': {
      'paths' : sorcery_paths(),
      'rituals': sorcery_rituals()
    }
  }

  with open(dst_path, 'w') as f:
    f.write(json.dumps(rules, indent=4 * ' '))
