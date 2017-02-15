#!/usr/bin/python3
import xml.etree.ElementTree as ET
from mdimport import rules


def backgrounds():
  bg_tree = ET.Element('backgrounds')
  for background in rules['backgrounds']:
    bg = ET.Element('background', name = background.name)
    for i, level in enumerate(background.levels):
      level_elem = ET.Element('level', number=str(i + 1))
      level_elem.text = level
      bg.append(level_elem)
    bg.text = background.description
    bg_tree.append(bg)
  return bg_tree
  
def merits():
  merits_tree = ET.Element('merits')
  for merit in rules['merits']:
    merit_xml = ET.Element('merit', {
      'name': merit.name,
      'type': merit.type,
      'cost': str(merit.cost),
      'is_multi_buy': str(merit.is_multi_buy)
    })
    merit_xml.text = merit.description
    merits_tree.append(merit_xml)
  return merits_tree
   
def moralities():
  morality_tree = ET.Element('moralities')
  for morality in rules['moralities']:
    morality_xml = ET.Element('morality', {
      'name': morality.name,
      'nickname': morality.nickname,
      'virtues': morality.virtues,
      'bearing': morality.bearing
    })
    morality_xml.text = morality.description
    for rating, sin in morality.sins.items():
      sin_xml = ET.Element('sin', {
        'rating': str(rating),
        'moral_guideline': sin.moral_guideline,
        'rationale': sin.rationale
      })
      morality_xml.append(sin_xml)

    morality_tree.append(morality_xml)
  return morality_tree
 
def archetypes():

"""
def clans():
def disciplines():
def attributes():
def virtues():
def sorcery_paths():
def sorcery_rituals():
"""

def abilities():
  ability_tree = ET.Element('abilities')
  for ability in rules['abilities']:
    ability_xml = ET.Element('ability', {
      'name': ability.name,
      'type': ability.type
    })
    ability_xml.text = "\n" + ability.description

    for i, level in enumerate(ability.levels):
      level_elem = ET.Element('level', number=str(i + 1))
      level_elem.text = level
      ability_xml.append(level_elem)

    ability_tree.append(ability_xml)
  return ability_tree


if __name__ == '__main__':
  rules_tree = ET.Element('rules')
  rules_tree.append(abilities())
  rules_tree.append(backgrounds())
  rules_tree.append(merits())
  rules_tree.append(moralities())
  ET.dump(rules_tree)



"""






rules.append(bg_tree)
ET.dump(rules)"""
