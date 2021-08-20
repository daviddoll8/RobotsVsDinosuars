from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
#from dinosaur import Dinosaur
from robot import Robot

if __name__ == "__main__":
  robot = Robot("Brutus")
  dinosaur = Dinosaur("Chad", 15)
  robot.attack(dinosaur)