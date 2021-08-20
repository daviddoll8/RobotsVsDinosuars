from fleet import Fleet
from herd import Herd

class Battlefield:
  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.attack_first = 0
  
  def run_game(self):
    self.fleet.create_fleet()
    self.herd.create_herd()
    self.display_welcome()
    self.battle()
    self.display_winners()

  def display_welcome(self):
    print("Welcome to Robots vs Dinosaurs\n")
    while True:
      try:
        self.attack_first = int(input("Please enter 1 for dinosaurs to attack first, and 2 if you would like robots to attack first"))
      except ValueError:
        print("Please enter the value 1 or 2 to select if robots or dinosuars attack first.")
        continue
      if(self.attack_first == 1 or self.attack_first == 2):
        break
      else:
        print("Please enter the value 1 or 2 to select if robots or dinosuars attack first.")
        continue

  def battle(self):
    if(self.attack_first == 1): #dinosaurs attack first   
      while self.fleet.get_fleet_health_pool() > 0 or self.herd.get_herd_health_pool() > 0:
        for dinosaur in self.herd.dinosaurs:
          self.dino_turn(dinosaur)
        
        if(self.fleet.get_fleet_health_pool() <= 0): #break early if the robots were all killed on the dinosaurs turn
          break

        for robot in self.fleet.robots:
          self.robo_turn(robot)
    else: #robots attack first
      while self.fleet.get_fleet_health_pool() > 0 or self.herd.get_herd_health_pool() > 0:
        for robot in self.fleet.robots:
          self.robo_turn(robot)

        if(self.herd.get_herd_health_pool() <= 0): #break early if the dinousaurs were all killed on the robots turn
          break
        
        for dinosaur in self.herd.dinosaurs:
          self.dino_turn(dinosaur)
  
  def dino_turn(self, dinosaur):
    print(dinosaur.name + "'s turn to attack. Attack power is " + str(dinosaur.attack_power) + " and health is " + str(dinosaur.health))
    self.show_dino_opponent_options()

    while True:
      try:
        robot_to_attack = int(input("Please enter the number of the robot that you would like to attack"))
      except ValueError:
        print("Please enter a valid number for which robot to attack from the above list.")
        continue
      if(robot_to_attack >= 1 and robot_to_attack <= len(self.fleet.robots)):
        break
      else:
        print("Please enter a valid number for which robot to attack from the above list.")

    dinosaur.attack(self.fleet.robots[robot_to_attack-1])
    
  def robo_turn(self, robot):
    print(robot.name + "'s turn to attack. Attack power is " + str(robot.weapon.attack_power) + " and health is " + str(robot.health))
    self.show_robo_opponent_options()

    while True:
      try:
        dinosaur_to_attack = int(input("Please enter the number of the dinosaur that you would like to attack"))
      except ValueError:
        print("Please enter a valid number for which dinosaur to attack from the above list.")
        continue
      if(dinosaur_to_attack >= 1 and dinosaur_to_attack <= len(self.herd.dinosaurs)):
        break
      else:
        print("Please enter a valid number for which robot to attack from the above list.")

    robot.attack(self.herd.dinosaurs[dinosaur_to_attack-1])

  def show_dino_opponent_options(self):
    i = 1
    for robot in self.fleet.robots:
      print(str(i) + ". Robot name: " + robot.name + " health: " + str(robot.health) + " weapon and attack power: " + robot.weapon.name + " " + str(robot.weapon.attack_power))
      i += 1

  def show_robo_opponent_options(self):
    i = 1
    for dinosaur in self.herd.dinosaurs:
      print(str(i) + ". Dinosaur name: " + dinosaur.name + " health: " + str(dinosaur.health) + " attack power: " + str(dinosaur.attack_power))
      i += 1

  def display_winners(self):
    if(self.herd.get_herd_health_pool() == 0):
      print("\nThe robots are the winners\n")
      self.show_dino_opponent_options()
    else:
      print("\nThe dinosaurs are the winners\n")
      self.show_robo_opponent_options()