from dinosaur import Dinosaur

class Herd:
  def __init__(self):
    self.dinosaurs = []
  
  def create_herd(self):
    names = ["Bob", "Bryan", "Chad"]
    attack_powers = [8, 10, 15]
    i = 1
    while i <= 3:
      self.dinosaurs.append(Dinosaur(names[i-1], attack_powers[i-1]))
      i += 1