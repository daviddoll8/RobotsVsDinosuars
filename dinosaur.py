class Dinosaur:
  def __init__(self, name, attack_power):
    self.name = name
    self.health = 30
    self.attack_power = attack_power

  def attack(self, robot):
    print(self.name + " the dinosaur is currently attacking " + robot.name + " the robot")
    if(robot.health <= 0):
      print(robot.name + " the robot has already been defeated")
    else:
      robot.health -= self.attack_power
      if(robot.health < 0):
        robot.health = 0
      print(robot.name + " the robot was successfully attacked by " + self.name + 
        " the dinosaur and now has " + str(robot.health) + " health")
      if(robot.health == 0):
        print(robot.name + " the robot has died on the battlefield from the attack by " + self.name + " the dinosaur")