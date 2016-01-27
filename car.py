

class Car:
   """Defines the properties and methods of a Car object."""

   def __init__(self, model, make):
      self.model = model
      self.make = make
      self.tires = 4
      self.color = ""
      self.interior = "cloth"
      self.upgrade_options = {
            "interior": "Leather", 
            "stereo":"Bose", 
            "speaker": "Surround Sound",
            "rims":"Spinners",
            }

   def drive(self, speed):
      """Move the car speed amount."""

      print("Vroom" * speed)

   def __str__(self):
      return "This Car's Model is: {0}, and it's Make is: {1}".format(self.model, self.make)

   def upgrade(self):
      """Present upgrade options for user and do them."""

      for upgrade in self.upgrade_options:
         print("Option for", upgrade,":", self.upgrade_options[upgrade])
