from dinosaur import Dinosaur

class Herd:
  def __init__(self):
    self.dinosaurs = []
  
  def create_herd(self):
    names = ["Bob", "Bryan", "Chad"]
    attack_powers = [10, 10, 10]
    i = 0
    while i <= 2:
      self.dinosaurs.append(Dinosaur(names[i], attack_powers[i]))
      i += 1

  def get_herd_health_pool(self):
    total_health_pool = 0
    for dinosaur in self.dinosaurs:
      total_health_pool += dinosaur.health
    return total_health_pool