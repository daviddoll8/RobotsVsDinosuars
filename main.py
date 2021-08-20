from fleet import Fleet
from herd import Herd
#from dinosaur import Dinosaur
from robot import Robot

if __name__ == "__main__":
  robot_fleet = Fleet()
  dinosaur_herd = Herd()
  robot1 = Robot("Brutus", 100)
  robot_fleet.addRobot(robot1)
  print(robot_fleet.robots[0].name)
  for obj in robot_fleet.robots:
    print(obj.name)