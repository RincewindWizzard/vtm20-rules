import xml.etree.ElementTree as ET
from abilities import abilities
from backgrounds import backgrounds

rules = ET.Element('rules')

ability_tree = ET.Element('abilities')
for ability in abilities.values():
  ability_xml = ET.Element('ability', {
    'name': ability.name,
    'type': ability.type
  })
  ability_xml.text = "\n" + ability.description + '\n'
  for i, level in enumerate(ability.levels):
    level_elem = ET.Element('level', number=str(i))
    level_elem.text = level
    ability_xml.append(level_elem)

  ability_tree.append(ability_xml)
rules.append(ability_tree)

bg_tree = ET.Element('backgrounds')
for background in backgrounds.values():
  bg = ET.Element('background', name = background.name)
  for i, level in enumerate(background.levels):
    level_elem = ET.Element('level', number=str(i))
    level_elem.text = level
    bg.append(level_elem)
  bg.text = background.description
  bg_tree.append(bg)

rules.append(bg_tree)
ET.dump(rules)
