import Hero
import WA
import Monsters
import World


def fight(my_hero, my_enemy):

    success_fight = True

    while my_hero.health > 0 and my_enemy.health > 0:
        print("Враг: {}".format(my_enemy.name))
        print("Здоровье врага: {}".format(my_enemy.health))
        print("Защита врага: {}".format(my_enemy.protection))
        print("Урон врага: {}".format(my_enemy.damage))
        print()
        print("Ваше здоровье: {}".format(my_hero.health))
        print("Ваша мана: {}".format(my_hero.mana))
        print("Ваша защита: {}".format(my_hero.protection))
        print("Ваш урон: {}".format(my_hero.damage))
        print("Урон атакующим заклинанием: {}".format(30))
        print("Затрата маны на атакующее заклинаине: {}".format(30))
        print("Регенерация здоровья восстанавливающим заклинанием: {}".format(100))
        print("Затрата маны на восстанавливающее заклинаине: {}".format(100))
        print("Количество зелий маны: {}".format(my_hero.quantity_mana_potions))
        print("Восстановление манны зельем: {}".format(100))
        print("Количество зелий здоровья: {}".format(my_hero.quantity_health_potions))
        print("Восстановление здрорвья зельем: {}".format(100))
        print()
        user_move = int(input("1 - удар, \n"
                              "2 - атакующее заклинаине, \n"
                              "3 - восстанавливающее заклинание, \n"
                              "4 - исопльзовать зелье маны, \n"
                              "5 - использовать зелье здорвья, \n"
                              "6 - блокировать атаку. \n"
                              "какое ваше действие: "))
        if user_move == 1:
            my_enemy.protection, my_enemy.health = my_hero.kick(my_enemy.protection, my_enemy.health)
            my_hero.protection, my_hero.health = my_enemy.kick(my_hero.protection, my_hero.health)
            my_enemy.get_ability()
            print()
        elif user_move == 2:
            my_enemy.health = my_hero.attack_spell(my_enemy.health)
            my_hero.protection, my_hero.health = my_enemy.kick(my_hero.protection, my_hero.health)
            my_enemy.get_ability()
        elif user_move == 3:
            my_hero.health = my_hero.recovery_spell(my_hero.health)
            my_hero.protection, my_hero.health = my_enemy.kick(my_hero.protection, my_hero.health)
            my_enemy.get_ability()
        elif user_move == 4:
            my_hero.drink_mana_potion()
            my_hero.protection, my_hero.health = my_enemy.kick(my_hero.protection, my_hero.health)
            my_enemy.get_ability()
        elif user_move == 5:
            my_hero.drink_health_potion()
            my_hero.protection, my_hero.health = my_enemy.kick(my_hero.protection, my_hero.health)
            my_enemy.get_ability()

        elif user_move == 6:
            my_hero.block()
            my_enemy.get_ability()

    if my_enemy.health <= 0:
        print("Вы победили")
    if my_hero.health <= 0:
        print("Вы проиграли")
        success_fight = False

    return success_fight


def get_artifact(my_hero, thing):
    take = input("Взять {}? (Y/y)".format(thing.name))
    if take.lower().strip() == 'y':
        if issubclass(type(thing), WA.Weapon):
            my_hero.weapon = thing
            my_hero.damage = 15 * my_hero.weapon.weapon_damage
            my_hero.protection = my_hero.armor.armor_protection + my_hero.weapon.weapon_protection
        elif issubclass(type(thing), WA.Armor):
            my_hero.armor = thing
            my_hero.protection = my_hero.armor.armor_protection + my_hero.weapon.weapon_protection
        elif issubclass(type(thing), WA.Potion):
            pass


def init_game():
    '''
    Инициализация игрового мира.
    '''
    game = World.World()
    game.init_topic(Monsters.mutant_dogs, 0, 33)
    game.init_topic(Monsters.monster_knights, 0, 66)
    game.init_topic(Monsters.vampires, 34, 99)
    game.init_topic(Monsters.daemons, 66, 99)
    game.init_topic(Monsters.boss, 99, 99)

    game.init_topic(WA.artefacts_armor, 0, 99)
    game.init_topic(WA.artefacts_potion, 0, 99)
    game.init_topic(WA.artefacts_weapon, 0, 99)

    return game


def intro():
    """
    Введение в игру
    """
    lets_go = True
    print("Вам нужно добраться до портала в другой мир. "
          "Игра проходит в мире площадью 100:10. Портал находится к востоку от вас."
          "У вас 300 шагов до конца игра, если не успеете или умрёто - проиграете.")
    message = input('(y/n)')

    if message.lower().strip() != 'y':
        lets_go = False

    return lets_go


def init_hero():
    """
    Инициализация главного героя.
    """
    users_choice = input(("выберите своб расу.Варианты:"
                         "Человек (H/h)(средние параметры), "
                         "Эльф (E/e)(уклон в магию),"
                         " Гном (G/g)(уклон в ближний бой): ")).lower().strip()
    if users_choice == "h":
        my_hero = Hero.Hero(Hero.human)
    elif users_choice == "e":
        my_hero = Hero.Hero(Hero.elf)
    elif users_choice == "g":
        my_hero = Hero.Hero(Hero.gnome)
    else:
        my_hero = Hero.Hero(Hero.human)

    return my_hero


def change_level(coordinate_of_location):
    """
    Оповещение о переходе на другую локацию
    """
    if coordinate_of_location == 0:
        print("Вы находитесь в лесу.")
    elif coordinate_of_location == 33:
        print("Вы перешли в пещеры.")
    elif coordinate_of_location == 66:
        print("вы перешли в подземелье.")


def game_end(why_finish_game):
    """
    Варианты конца игры
    """
    if why_finish_game == 'success':
        print("Вы победили стража портала, теперь вы покидаете этот мир.")
    elif why_finish_game == 'timeout':
        print("Вы не успели добраться до цели, вы проиграли.")
    elif why_finish_game == 'killme':
        print("Вас убили чудовища, вы проиграли.")


if intro():
    game = init_game()
    hero = init_hero()

    # Ядро игры.
    limit_moves = 125
    count_of_moves = 0
    day = 0
    why_finish_game = 'killme'

    print('Наступил день!')

    while True:

        end_of_game = False
        day += 1
        if day == game.day_to_night:
            day == 0
            game.day = not game.day
            if game.day:
                print('Наступил день!')
            else:
                print('Наступила ночь!')

        change_level(game.coordinate_hero_x)

        print('Запас ходов - {}'.format(limit_moves))
        print('w - вперед, s - назад, a - лево, d - право, m - карта, q - выход:')
        move_of_hero = input('?')

        if move_of_hero == 'm':
            game.show_map_of_world()
        elif move_of_hero == 'q':
            print('Вы вышли из игры. Возвращайтесь!')
            end_of_game = True
        else:
            move_is_completed = game.move_hero_in_world(move_of_hero)
            if move_is_completed:
                message = ''
                limit_moves -= 1

                topic_in_cell = game.map_of_world[game.coordinate_hero_x][game.coordinate_hero_y]
                if topic_in_cell == '':
                    message = 'X' * 16
                else:
                    if issubclass(type(topic_in_cell), WA.Weapon):
                        get_artifact(hero, topic_in_cell)
                        message = 'Оружие'
                    elif issubclass(type(topic_in_cell), WA.Armor):
                        get_artifact(hero, topic_in_cell)
                        message = 'Защита'
                    elif issubclass(type(topic_in_cell), WA.Potion):
                        get_artifact(hero, topic_in_cell)
                        message = 'Зелье'
                    elif issubclass(type(topic_in_cell), Monsters.Vampire) and not game.day:
                        success_fight = fight(hero, topic_in_cell)
                        if success_fight:
                            message = 'Вампир'
                        else:
                            end_of_game = True
                    elif issubclass(type(topic_in_cell), Monsters.MonsterKnight):
                        success_fight = fight(hero, topic_in_cell)
                        if success_fight:
                            message = 'Рыцарь'
                        else:
                            end_of_game = True
                    elif issubclass(type(topic_in_cell), Monsters.Daemon):
                        success_fight = fight(hero, topic_in_cell)
                        if success_fight:
                            message = 'Демон'
                        else:
                            end_of_game = True
                    elif issubclass(type(topic_in_cell), Monsters.MutantDog):
                        success_fight = fight(hero, topic_in_cell)
                        if success_fight:
                            message = 'Собака-мутант'
                        else:
                            end_of_game = True
                    elif issubclass(type(topic_in_cell), Monsters.PortalGuard):
                        success_fight = fight(hero, topic_in_cell)
                        if success_fight:
                            message = 'Страж портала'
                            end_of_game = True
                            why_finish_game = 'success'
                        else:
                            end_of_game = True

                if limit_moves == 0:
                    print("У героя закончились ходы.")
                    why_finish_game = 'timeout'
                    end_of_game = True

                if not end_of_game:
                    game.map_of_world[game.coordinate_hero_x][game.coordinate_hero_y] = message

        if end_of_game:
            end_of_game(why_finish_game)
            break
else:
    print('Если не пониматно, тогда досвиданто!')
