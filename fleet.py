from robot import Robot

class Fleet:
  def __init__(self):
    self.robots = []

  def create_fleet(self):
    i = 1
    names = ["Brutus", "Malachai", "Doedre"]
    while i <= 3:
      self.robots.append(Robot(names[i - 1]))
      i += 1

    