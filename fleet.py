from robot import Robot

class Fleet:
  def __init__(self):
    self.robots = []

  def create_fleet(self):
    i = 1
    names = ["Brutus", "Malachai", "Doedre"]
    while i <= 3:
      robot = Robot(names[i-1])
      robot.select_weapon()
      self.robots.append(robot)
    
      i += 1

  def get_fleet_health_pool(self):
    total_health_pool = 0
    for robot in self.robots:
      total_health_pool += robot.health
    return total_health_pool

    