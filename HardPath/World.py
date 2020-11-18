import random

class World:
    """
    Характеристики мира.
    """
    def __init__(self):
        self.height = 100
        self.width = 10
        self.day_to_night = 10
        self.map_of_world = [[''] * self.width for i in range(self.height)]
        self.coordinate_hero_x = 0
        self.coordinate_hero_y = 0
        self.day = True

    def init_topic(self, topics, board_from, board_to):
        """
        Инициализация монстров и артефактов в мире.
        """
        if board_to == board_from:
            for coordinate_y in range(self.width):
                self.map_of_world[board_from][coordinate_y] = topics
        else:
            for topic in topics:
                coordinate_x = random.randint(board_from, board_to)
                coordinate_y = random.randint(0, self.width - 1)
                self.map_of_world[coordinate_x][coordinate_y] = topic

    def show_map_of_world(self):
        """
        Показать карту мира.
        """
        index_of_step = 0
        for step in self.map_of_world:
            message = ''
            index_of_position = 0
            for position in step:
                part_of_message = ' '
                if isinstance(position, str):
                    part_of_message = position
                if self.coordinate_hero_x == index_of_step and self.coordinate_hero_y == index_of_position:
                    part_of_message = 'Ты здесь'
                message = message + '|' + part_of_message.ljust(16) + '|'
                index_of_position += 1

            print(message)
            index_of_step += 1

    def move_hero_in_world(self, move_of_hero):
        """
        Учет движений героя по координатам мира.
        """
        move_completed = False
        change_coordinate_x = 0
        change_coordinate_y = 0

        new_coordinate_x = self.coordinate_hero_x
        new_coordinate_y = self.coordinate_hero_y

        message = 'Не-а. Там болото!'

        if move_of_hero == 'w':
            change_coordinate_x = 1
        elif move_of_hero == 's':
            change_coordinate_y = -1
        elif move_of_hero == 'a':
            change_coordinate_y = -1
        elif move_of_hero == 'd':
            change_coordinate_y = 1

        if change_coordinate_y != 0:
            new_coordinate_y = self.coordinate_hero_y + change_coordinate_y

        if change_coordinate_x != 0:
            new_coordinate_x = self.coordinate_hero_x + change_coordinate_x

        if 0 <= new_coordinate_x < self.height:
            self.coordinate_hero_x = new_coordinate_x
            move_completed = True

        if 0 <= new_coordinate_y < self.width:
            self.coordinate_hero_y = new_coordinate_y
            move_completed = True

        if not move_completed:
            print(message)

        return move_completed
