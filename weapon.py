class Weapon:
  def __init__(self):
    self.name = "Sword"
    self.attack_power = 10
  
  def select_weapon(self):
    weapon_list = ['sword', 'gun', 'laser', 'grenade', 'spear']
    print("Weapon Selection: ")
    i = 1
    for weapon in weapon_list:
      print(str(i) + ". " + weapon)
    

