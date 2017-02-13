#!/usr/bin/python3
import os
from collections import namedtuple

# third party libraries
import frontmatter
import simplejson as json

# Data types for the rules
Background = namedtuple('Background', ['name', 'levels', 'description'])
Merit = namedtuple('Merit', ['name', 'type', 'cost', 'is_multi_buy', 'description'])


rules_root = '../markdown/'
background_path = os.path.join(rules_root, 'backgrounds')
merits_path = os.path.join(rules_root, 'merits')

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

if __name__ == '__main__':
  rules = {
    'backgrounds': backgrounds(),
    'merits': merits()
  }

  print(json.dumps(rules, indent=4 * ' '))
