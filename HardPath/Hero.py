import WA


class Hero:
    """
    Главный герой игры.
    """
    def __init__(self, start_parameters):
        """
        Первоначальная установка характеристик героя.
        """
        self.health = start_parameters['health']
        self.mana = start_parameters['mana']
        self.weapon = start_parameters['weapon']
        self.armor = start_parameters['armor']
        self.damage = start_parameters['damage']
        self.protection = start_parameters['protection']
        self.quantity_mana_potions = start_parameters['quantity_mana_potions']
        self.quantity_health_potions = start_parameters['quantity_health_potions']

    def kick(self, enemy_protection, enemy_health):
        """
        Отработка действия 'Ударить' героя.
        """
        if self.mana >= 5 and self.health != 0:
            self.mana -= 5
            enemy_protection -= self.damage
            if enemy_protection <= 0:
                enemy_health += enemy_protection
                enemy_protection = 0
            enemy_health = 0 if enemy_health < 0 else enemy_health
        return enemy_protection,  enemy_health

    def attack_spell(self, enemy_health):
        """
        Отработка действия 'Использовать боевое заклинание' героя.
        """
        if self.mana >= 100 and self.health != 0:
            self.mana -= 30
            enemy_health -= 30
            enemy_health = 0 if enemy_health < 0 else enemy_health
        return enemy_health

    def recovery_spell(self, hero_health):
        """
        Отработка действия 'Использовать восстанавливающее заклинание' героя.
        """
        if self.mana >= 100 and self.health > 0:
            self.mana -= 100
            hero_health += 100
            hero_health = 150 if hero_health > 150 else hero_health
        return hero_health

    def drink_mana_potion(self):
        """
        Отработка действия 'Использовать зелье маны' героя.
        """
        if self.quantity_mana_potions > 0:
            self.mana += 100
            self.quantity_mana_potions -= 1
            self.mana = 150 if self.mana > 150 else self.mana

    def drink_health_potion(self):
        """
        Отработка действия 'Использовать зелье здоровья' героя.
        """
        if self.quantity_health_potions > 0:
            self.health += 100
            self.quantity_health_potions -= 1
            self.health = 150 if self.health > 150 else self.health

    def block(self):
        """
        Отработка действия 'Блокировать атаку героя' героя.
        """
        self.mana += 20
        self.mana = 150 if self.mana > 150 else self.mana


human = {
    'health': 150,
    'mana': 150,
    'weapon': WA.weapons['SteelSword'],
    'armor': WA.armors['ChainMail'],
    'damage': 10 * WA.weapons['SteelSword'].weapon_damage,
    'protection': WA.armors['ChainMail'].armor_protection + WA.weapons['SteelSword'].weapon_protection,
    'quantity_mana_potions': 2,
    'quantity_health_potions': 2}

elf = {
    'health': 100,
    'mana': 200,
    'weapon': WA.weapons['IronSword'],
    'armor': WA.armors['Mantle'],
    'damage': 5 * WA.weapons['IronSword'].weapon_damage,
    'protection': WA.armors['Mantle'].armor_protection + WA.weapons['IronSword'].weapon_protection,
    'quantity_mana_potions': 3,
    'quantity_health_potions': 1}

gnome = {
    'health': 200,
    'mana': 100,
    'weapon': WA.weapons['DefenderAxe'],
    'armor': WA.armors['IronArmor'],
    'damage': 10 * WA.weapons['DefenderAxe'].weapon_damage,
    'protection': WA.armors['IronArmor'].armor_protection + WA.weapons['DefenderAxe'].weapon_protection,
    'quantity_mana_potions': 1,
    'quantity_health_potions': 3}

heroes = {'human': Hero(human),
          'elf': Hero(elf),
          'gnome': Hero(gnome)}
