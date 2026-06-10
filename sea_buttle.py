
import os
import random

class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships
        self.grid = []
        self.ships_alive = ships
        for i in range(size):
            self.grid.append([0]*(size))

    def displayOld(self, show_ships=False):
        print('    A B C D E F G H I J ')

        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                # проверка, что ячейка пустая
                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10: # вывод ноликов и квадратиков
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

    def display(self, show_ships=False):
        print('    A B C D E F G H I J ')

        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                # проверка, что ячейка пустая
                if cell == 0:
                    display_row += "O "
                elif cell == 'S' and not show_ships:
                    display_row += "O "
                elif cell == 'S' and show_ships:
                    display_row += "■ "
                elif cell == 'X':
                    display_row += "X "
                else:
                    display_row += "* "
            if i + 1 != 10: # вывод ноликов и квадратиков
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)
    def place_ships_randomly(self, field, num_ships):
        for i in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False
        return True

    def play(self):
        cheatCode = False
        self.place_ships_randomly(self.computer_field, self.ships)
        self.place_ships_randomly(self.player_field, self.ships)
        # print(self.computer_field.grid)

        while True:


            print("Расстановка кораблей компьютера:")
            self.computer_field.display(show_ships=cheatCode)

            print("Ваша расстановка кораблей:")
            self.player_field.display(show_ships=True)

            x , y = input('Введите координаты XY: ')
            y = int(y)

            if x + str(y) == '67':
                cheatCode = True
                print('чит-код использован')
                os.system('cls')
                continue
            self.player_turn(x, y)
            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены")
                break

            # input('Нажмите *Enther*')
            os.system('cls')

    def player_turn(self, x, y):

        x = "ABCDEFGHIJ".index(x)
        y -= 1
        if self.computer_field.grid[y][x] == "S":
            print("Вы попали!")
            self.computer_field.ships_alive -= 1
            self.computer_field.grid[y][x] = "X"
        else:
            print('Промах!')
            self.computer_field.grid[y][x] = "*"

    def computer_turn(self):
        x = random.randint(0, self.size -1)
        y = random.randint(0, self.size -1)
        if self.player_field.grid[y][x] == "S":
            print("Компьютер попал!")
            self.player_field.ships_alive -= 1
            self.player_field.grid[y][x] = "X"
        else:
            print('Компьютер промахнулся!')
            self.player_field.grid[y][x] = "*"



game = BattleshipGame()
game.play()