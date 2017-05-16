#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import QObject, Qt
from .vtm20character import VtM20Character
from .vtm20character import PHYSICAL, MENTAL, SOCIAL, TALENT, SKILL, KNOWLEDGE
ui_file = os.path.join(os.path.dirname(__file__), 'ui/charactersheet.ui')

def borderless(layout):
  layout.setSpacing(0)
  layout.setContentsMargins(0, 0, 0, 0)
  return layout

class DotWidget(object):
  def __init__(self, parent, trait, vamp, debug=False):
    self.parent = parent
    self.trait = trait
    self.vamp = vamp
    self.debug = debug


    self.trait_label = QLabel()
    self.trait_label.setText(trait)


    self.spinbox = QSpinBox()
    self.spinbox.valueChanged.connect(lambda v: self.valueChanged(v))
    self.spinbox.setMinimum(self.vamp.getTraitDots(self.trait)[0])
    self.spinbox.setMaximum(10)
    self.spinbox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

    self.trait_label.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
    self.spinbox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
    parent.addRow(self.trait_label, self.spinbox)
    self.update_dots_spent()

  def update_dots_spent(self):
    if self.debug:
      self.trait_label.setText('{} ({} + {} + {} + {})'.format(
        self.trait,
        *self.vamp.getTraitDots(self.trait))
      )
    else:
      self.trait_label.setText(self.trait)

  def valueChanged(self, value):
    delta = value - self.vamp.getTrait(self.trait)
    if delta > 0:
      self.vamp.spendDot(self.trait, None, delta)
    elif delta < 0:
      self.vamp.deleteDot(self.trait, None, -delta)
    self.update_dots_spent()

class VtM20Editor(object):
  def __init__(self, *args):
    #super(VtM20Editor, self).__init__(*args)
    self.vamp = VtM20Character()
    #self.resize(500, 500)
    #self.setWindowTitle('Vampire the Masquerade 20th Character Editor')
    #self.setWindowIcon(QIcon('web.png'))
    self.ui = uic.loadUi(ui_file)
    self.addDotWidgets()

  def addDotWidgets(self):
    self.ui.widget_physical_container.layout().setAlignment(
      self.ui.widget_physical, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(PHYSICAL):
      DotWidget(self.ui.widget_physical.layout(), trait, self.vamp)

    self.ui.widget_social_container.layout().setAlignment(
      self.ui.widget_social, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(SOCIAL):
      DotWidget(self.ui.widget_social.layout(), trait, self.vamp)

    self.ui.widget_mental_container.layout().setAlignment(
      self.ui.widget_mental, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(MENTAL):
      DotWidget(self.ui.widget_mental.layout(), trait, self.vamp)

    self.ui.widget_talent_container.layout().setAlignment(
      self.ui.widget_talent, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(TALENT):
      DotWidget(self.ui.widget_talent.layout(), trait, self.vamp)

    self.ui.widget_skill_container.layout().setAlignment(
      self.ui.widget_skill, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(SKILL):
      DotWidget(self.ui.widget_skill.layout(), trait, self.vamp)

    self.ui.widget_knowledge_container.layout().setAlignment(
      self.ui.widget_knowledge, 
      Qt.AlignHCenter
    )
    for trait in self.vamp.getTraits(KNOWLEDGE):
      DotWidget(self.ui.widget_knowledge.layout(), trait, self.vamp)

  def show(self):
    self.ui.show()


def main(argv):
  app = QApplication(argv)
  gui = VtM20Editor()
  gui.show()
  sys.exit(app.exec_())
  

if __name__ == '__main__':
  main(sys.argv)
