from fleet import Fleet
from herd import Herd

class Battlefield:
  def __init__(self):
    fleet = Fleet().create_fleet()
    herd = Herd().create_herd()
    attack_first = 0
  
  def run_game(self):
    self.display_welcome()
    pass

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
      pass
    else: #robots attack first
      pass
  
  def dino_turn(self, dinosaur):
    pass
  
  def robo_turn(self, robot):
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robo_opponent_options(self):
    pass

  def display_winners(self):
    pass