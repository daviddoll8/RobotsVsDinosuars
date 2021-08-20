from weapon import Weapon

class Robot:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.weapon = Weapon()

  def attack(self, dinosaur):
    print(self.name + " the robot is currently attacking " + dinosaur.name + " the dinosaur")
    if(dinosaur.health <= 0):
      print(dinosaur.name + " the dinosaur has already been defeated")
    else:
      dinosaur.health -= self.weapon.attack_power
      print(dinosaur.name + " the dinosuar was successfully attacked by " + self.name + 
        " the robot and now has " + str(dinosaur.health) + " health")
      if(dinosaur.health <= 0):
        print(dinosaur.name + " the dinosaur has died from the attack by " + self.name + " the robot")