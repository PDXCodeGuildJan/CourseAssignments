"""Defines the Creature class, the base class of all 
living things in our game."""

class Creature:

   # Constants for the states of creatures
   NORMAL = "normal"
   ASLEEP = "asleep"
   UNCONS = "unconscious"
   POISONED = "poisoned"
   WEAKENED = "weakened"


   def __init__(self):
      self.name = ""
      self.state = Creature.NORMAL
      self.health = 20
      self.max_health = 20
      self.attack_points = 2
      self.weapon = None
      self.special_abilities = {}
      self.stats = {}

   def attack(self):
      pass

   def heal(self, heal_amount):
      pass

   def defend(self, attack_amount):
      pass

   def take_damage(self, damage):
      pass

   def change_weapon(self, new_weapon):
      pass

   def change_state(self, new_state):
      pass