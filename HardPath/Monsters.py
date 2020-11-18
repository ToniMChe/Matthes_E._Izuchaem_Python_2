class Monster:
    """
    Монстры, встречающиеся в игре.
    """
    def __init__(self, parameters_of_monster):
        """
        Установка первоначальных параметров монстра.
        """
        self.name = parameters_of_monster['name']
        self.health = parameters_of_monster['health']
        self.protection = parameters_of_monster['protection']
        self.damage = parameters_of_monster['damage']
        self.area = parameters_of_monster['area']
        self.time = parameters_of_monster['time']

    def kick(self, hero_protection, hero_health):
        """
        Базовое действие 'Ударить' монстра.
        """
        if self.health != 0:
            hero_protection -= self.damage
            if hero_protection < 0:
                hero_health += hero_protection
                hero_protection = 0
            hero_health = 0 if hero_health < 0 else hero_health
        return hero_protection, hero_health


class MutantDog(Monster):
    """
    Монстр - собака-мутант.
    """
    def get_ability(self):
        """
        Действие 'Использовать уникальную способность' монстра.
        """
        if 0 < self.health <= 20:
            self.health += 5


class MonsterKnight(Monster):
    """
    Монстр - монстр-рыцарь.
    """
    def get_ability(self):
        """
        Действие 'Использовать уникальную способность' монстра.
        """
        if 0 < self.health <= 30:
            self.health += 5
            self.protection += 1


class Vampire(Monster):
    """
    Монстр - вампир.
    """
    def kick(self, human_protection):
        """
        Уникальное действие 'Ударить' монстра.
        """
        if human_protection <= self.damage:
            return human_protection - self.damage

    def get_ability(self):
        """
         Действие 'Использовать уникальную способность' монстра.
         """
        if 0 < self.health <= 10:
            self.health += 5


class Daemon(Monster):
    """
    Монстр - демон.
    """
    def kick(self, hero_protection, hero_health):
        """
        Уникальное действие 'Ударить' монстра.
        """
        if self.health != 0:
            hero_health -= self.damage
        return hero_protection, hero_health

    def get_ability(self):
        """
          Действие 'Использовать уникальную способность' монстра.
        """
        if 0 < self.health <= 40:
            self.health += 10


class PortalGuard(Monster):
    """
    Главный босс игры.
    """

    def kick(self, hero_protection, hero_health):
        """
        Уникальное действие 'Ударить' монстра.
        """
        if self.health != 0:
            hero_protection -= self.damage
            if hero_protection < 0:
                hero_health += hero_protection
                hero_protection = 0
            hero_health = 0 if hero_health < 0 else hero_health
        return hero_protection, hero_health

    def get_ability(self):
        """
        Действие 'Использовать уникальную способность' монстра.
         """
        if self.health > 0:
            self.health += 10
            self.protection += 5


# Инициализация монстров - собаки-мутанты.
count_of_mutant_dogs = 30
params_of_mutant_dogs = {
            'name': 'собака-мутант',
            'health': 50,
            'protection': 0,
            'damage': 10,
            'area': 'forest',
            'time': 'day'
        }
mutant_dogs = [MutantDog(params_of_mutant_dogs) for i in range(count_of_mutant_dogs)]

# Инициализация монстров - монстры-рыцари.
count_of_monster_knights = 50
params_of_monster_knights = {
            'name': 'монстр-рыцарь',
            'health': 60,
            'protection': 20,
            'damage': 15,
            'area': 'forestcaves',
            'time': 'anytime'
        }
monster_knights = [MonsterKnight(params_of_monster_knights) for i in range(count_of_monster_knights)]

# Инициализация монстров - вампиры.
count_of_vampires = 20
params_of_vampires = {
            'name': 'вампир',
            'health': 50,
            'protection': 0,
            'damage': 30,
            'area': 'caveschurch',
            'time': 'night'
        }
vampires = [Vampire(params_of_vampires) for i in range(count_of_vampires)]

# Инициализация монстров - демоны.
count_of_daemons = 10
params_of_daemons = {
            'name': 'демон',
            'health': 100,
            'protection': 0,
            'damage': 30,
            'area': 'church',
            'time': 'anytime'
        }
daemons = [Daemon(params_of_daemons) for i in range(count_of_daemons)]

# Инициализация босса.
boss = PortalGuard({
            'name': 'защитник портала',
            'health': 300,
            'protection': 100,
            'damage': 50,
            'area': 'church',
            'time': 'anytime'
        })
