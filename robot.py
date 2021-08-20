from weapon import Weapon

class Robot:
  def __init__(self, name):
    self.name = name
    self.health = 30
    self.weapon = Weapon()

  def attack(self, dinosaur):
    print(self.name + " the robot is currently attacking " + dinosaur.name + " the dinosaur")
    if(dinosaur.health <= 0):
      print(dinosaur.name + " the dinosaur has already been defeated")
    else:
      dinosaur.health -= self.weapon.attack_power
      if(dinosaur.health < 0):
        dinosaur.health = 0
      print(dinosaur.name + " the dinosuar was successfully attacked by " + self.name + 
        " the robot and now has " + str(dinosaur.health) + " health")
      if(dinosaur.health <= 0):
        print(dinosaur.name + " the dinosaur has died on the battlefield from the attack by " + self.name + " the robot")
  
  def select_weapon(self):
    print("Now selecting " + self.name + "'s Weapon")
    weapon_dict = {
      "Sword" : 10,
      "Spear" : 12,
      "Gun" : 14,
      "Laser" : 16,
      "Grenade" : 18
    }
    print("Available Weapons: ")
    i = 1
    for weapon in weapon_dict:
      print(str(i) + ". Weapon: " + weapon + " Attack Power: " + str(weapon_dict[weapon]))
      i += 1
    
    while True:
      try:
        weapon_selection = int(input("Please enter the number of the weapon that you would like to equip to " + self.name))
      except ValueError:
        print("Please enter a valid number of a weapon to equip to " + self.name)
        continue
      if(weapon_selection >= 1 and weapon_selection <= len(weapon_dict)):
        break
      else:
        print("Please enter a valid number for which robot to attack from the above list.")
    weapon_list = list(weapon_dict)
    self.weapon.name = weapon_list[weapon_selection-1]
    self.weapon.attack_power = weapon_dict[self.weapon.name]