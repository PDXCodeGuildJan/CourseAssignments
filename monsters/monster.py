from creature import Creature

class Monster(Creature):

   AGGRO = "aggressive"
   DEFENSE = "defensive"

   def __init__(self):
      super(Monster, self).__init__()

      self.personality = Monster.AGGRO
      self.state = Creature.ASLEEP



class Hero(Creature):

   def __init__(self):

      super(Hero, self).__init__()

      self.level = 1

class MonsterHero(Monster, Hero):

   def __init__(self):
      Monster.__init__(self)
      Hero.__init__(self)




















