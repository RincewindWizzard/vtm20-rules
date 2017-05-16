#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QSizePolicy
from vtm20character import VtM20Character

class DotWidget(QWidget):
  def __init__(self, trait, vamp):
    super(DotWidget, self).__init__()
    self.trait = trait
    self.vamp = vamp
    hbox = borderless(QHBoxLayout())
    self.setLayout(hbox)
    self.trait_label = QLabel()
    self.trait_label.setText(trait)
    hbox.addWidget(self.trait_label)

    self.dot_label = QLabel()
    self.update_dots_spent()
    hbox.addWidget(self.dot_label)

    self.spinbox = QSpinBox()
    self.spinbox.valueChanged.connect(self.valueChanged)
    self.spinbox.setMinimum(self.vamp.getTraitDots(self.trait)[0])
    self.spinbox.setMaximum(10)
    self.spinbox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
    hbox.addWidget(self.spinbox)

  def update_dots_spent(self):
    self.dot_label.setText('({} + {} + {} + {})'.format(*self.vamp.getTraitDots(self.trait)))

  def valueChanged(self, value):
    delta = value - self.vamp.getTrait(self.trait)
    if delta > 0:
      self.vamp.spendDot(self.trait, None, delta)
    elif delta < 0:
      self.vamp.deleteDot(self.trait, None, -delta)
    self.update_dots_spent()

def borderless(layout):
  layout.setSpacing(0)
  layout.setContentsMargins(0, 0, 0, 0)
  return layout

class VtM20Editor(QWidget):
  def __init__(self, *args):
    super(VtM20Editor, self).__init__(*args)
    self.vamp = VtM20Character()
    self.resize(500, 500)
    self.setWindowTitle('Vampire the Masquerade 20th Character Editor')
    #self.setWindowIcon(QIcon('web.png'))

    vbox = borderless(QVBoxLayout())
    attributes_widget = QWidget()
    vbox.addWidget(attributes_widget)
    
    hbox = borderless(QHBoxLayout())
    attributes_widget.setLayout(hbox)

    self.physical_widget = QWidget()
    self.physical_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.physical_widget)

    self.social_widget = QWidget()
    self.social_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.social_widget)

    self.mental_widget = QWidget()
    self.mental_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.mental_widget)


    abilities_widget = QWidget()
    hbox = borderless(QHBoxLayout())
    abilities_widget.setLayout(hbox)

    self.talent_widget = QWidget()
    self.talent_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.talent_widget)

    self.skill_widget = QWidget()
    self.skill_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.skill_widget)

    self.knowledge_widget = QWidget()
    self.knowledge_widget.setLayout(borderless(QVBoxLayout()))
    hbox.addWidget(self.knowledge_widget)


    vbox.addWidget(abilities_widget)

    self.setLayout(vbox)
    self.addDotWdigets()

  def addDotWdigets(self):
    for trait in self.vamp.getTraits('Physical'):
      self.physical_widget.layout().addWidget(DotWidget(trait, self.vamp))

    for trait in self.vamp.getTraits('Social'):
      self.social_widget.layout().addWidget(DotWidget(trait, self.vamp))

    for trait in self.vamp.getTraits('Mental'):
      self.mental_widget.layout().addWidget(DotWidget(trait, self.vamp))

    for trait in self.vamp.getTraits('Talent'):
      self.talent_widget.layout().addWidget(DotWidget(trait, self.vamp))

    for trait in self.vamp.getTraits('Skill'):
      self.skill_widget.layout().addWidget(DotWidget(trait, self.vamp))

    for trait in self.vamp.getTraits('Knowledge'):
      self.knowledge_widget.layout().addWidget(DotWidget(trait, self.vamp))


if __name__ == '__main__':
  app = QApplication(sys.argv)

  gui = VtM20Editor()

  gui.show()
   
  sys.exit(app.exec_())
