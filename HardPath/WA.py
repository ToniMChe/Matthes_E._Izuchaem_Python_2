import random

class Weapon:
    def __init__(self, type_of_weapon, weapon_damage, weapon_protection):
        self.name= type_of_weapon
        self.weapon_damage = weapon_damage
        self.weapon_protection = weapon_protection


class Armor:
    def __init__(self, type_of_armor, armor_protection):
        self.name = type_of_armor
        self.armor_protection = armor_protection


class Potion:
    def __init__(self, type_of_potion, potion_count):
        self.name = type_of_potion
        self.potion_count = potion_count


weapons = {'IronSword': Weapon('железный меч', 1.5, 0),
           'SteelSword': Weapon('стальной меч', 1.7, 0),
           'ElfSword': Weapon('эльфийский меч', 3, 0),
           'DefenderAxe': Weapon('защитный топор', 2, 15),
           'MagicSword': Weapon('магический меч', 10, 0)}

armors = {"Mantle": Armor('мантия', 10),
          "ChainMail": Armor('кольчуга', 50),
          "IronArmor": Armor('железная броня', 60),
          "SteelArmor": Armor('стальная броня', 80),
          "Segmental": Armor('сегментная броня', 150)}

potions = {"HealthPotion": Potion('зелье здоровья', 1),
           "ManaPotion": Potion('зелье маны', 1)}

count_of_artefact_weapon = 65
count_of_artefact_armor = 60
count_of_artefact_potion = 100

artefacts_weapon = [weapons[random.choice(list(weapons.keys()))] for i in range(count_of_artefact_weapon)]
artefacts_armor = [armors[random.choice(list(armors.keys()))] for i in range(count_of_artefact_armor)]
artefacts_potion = [potions[random.choice(list(potions.keys()))] for i in range(count_of_artefact_potion)]
