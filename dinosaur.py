class Dinosaur:
  def __init__(self, name, attack_power):
    self.name = name
    self.health = 30
    self.attack_power = attack_power

  def attack(self, robot):
    dinosaur_attacks = ("slash", "tailwhip", "bite", "stomp")
    print("Available Dinosaur Attacks: ")
    i = 1
    for attack in dinosaur_attacks:
      print(str(i) + ". Attack Name: " + attack)
      i += 1
    
    while True:
      try:
        attack_selection = int(input("Please enter the number of the attack that you would like to use on " + robot.name))
      except ValueError:
        print("Please enter a valid number of a dinosaur attack to use.")
        continue
      if(attack_selection >= 1 and attack_selection <= len(dinosaur_attacks)):
        break
      else:
        print("Please enter a valid number of a dinosaur attack to use.")
    chosen_attack = dinosaur_attacks[attack_selection-1]
    print(self.name + " the dinosaur is currently attacking " + robot.name + " the robot with " + chosen_attack)   
    if(robot.health <= 0):
      print(robot.name + " the robot has already been defeated")
    else:
      robot.health -= self.attack_power
      if(robot.health < 0):
        robot.health = 0
      print(self.name + " the dinosaur succesfully attacked " + robot.name + " with " + chosen_attack +
        ". " + robot.name + " now has " + str(robot.health) + " health")
      if(robot.health == 0):
        print(robot.name + " the robot has died on the battlefield from the " + chosen_attack +  " attack by " + self.name + " the dinosaur")