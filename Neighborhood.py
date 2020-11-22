import sys

from House import House
from Observer import Observer


class Neighborhood(Observer):

    def __init__(self):
        # Set up number of houses, location of houses, etc.
        self.num_houses = 4
        self.mon_houses = 4
        self.house_grid = [
            ['P', 'H', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['H', '.', '.', '.', 'H'],
            ['.', '.', '.', 'H', '.'],
            ['.', '.', '.', '.', '.']
        ]
        # List of house locations with (0,0) being upper left spot
        self.house_locs = [[0, 1], [2, 0], [2, 4], [3, 3]]
        self.player_loc = [0, 0]
        self.houses = []
        self.generate_houses()

    def check_houses(self):
        for house in self.houses:
            if house.is_empty():
                self.mon_houses -= 1

    def generate_houses(self):
        h1 = House()
        self.houses.append(h1)
        h1.add_observer(self)

        h2 = House()
        self.houses.append(h2)
        h2.add_observer(self)

        h3 = House()
        self.houses.append(h3)
        h3.add_observer(self)

        h4 = House()
        self.houses.append(h4)
        h4.add_observer(self)

        self.check_houses()

    def check_player_loc(self):
        return self.player_loc in self.house_locs

    def walk(self, direction):
        if direction == "north":
            self.__walk_north()
        elif direction == "south":
            self.__walk_south()
        elif direction == "east":
            self.__walk_east()
        elif direction == "west":
            self.__walk_west()

    def __walk_south(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a, b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if a < 4:
            if [a, b] in self.house_locs:
                self.house_grid[a][b] = 'H'
            else:
                self.house_grid[a][b] = '.'
            self.player_loc[0] += 1
            # if [a,b] in self.house_locs:
            # houseLocs[][] = "H"
            a, b = self.player_loc[0], self.player_loc[1]
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have moved south. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else:
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def __walk_north(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a, b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if a > 0:
            if [a, b] in self.house_locs:
                self.house_grid[a][b] = 'H'
            else:
                self.house_grid[a][b] = '.'
            self.player_loc[0] -= 1
            a, b = self.player_loc[0], self.player_loc[1]
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked north. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else:
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def __walk_east(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a, b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if b < 4:
            if [a, b] in self.house_locs:
                self.house_grid[a][b] = 'H'
            else:
                self.house_grid[a][b] = '.'
            self.player_loc[1] += 1
            a, b = self.player_loc[0], self.player_loc[1]
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked east. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else:
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def __walk_west(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a, b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if b > 0:
            if [a, b] in self.house_locs:
                self.house_grid[a][b] = 'H'
            else:
                self.house_grid[a][b] = '.'
            self.player_loc[1] -= 1
            a, b = self.player_loc[0], self.player_loc[1]
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked west. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else:
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def remove_mon_house(self):
        self.mon_houses -= 1

    def print_grid(self):
        for line in self.house_grid:
            print(*line, sep=' ')
        print('\n')

    def update(self, house):
        self.mon_houses -= 1
        if self.mon_houses > 0:
            print('This house no longer contains monsters... but there are {} houses left!\n'.format(self.mon_houses))
        if self.mon_houses <= 0:
            print('You have successfully cleansed The Neighborhood... Congratulations! Until next time... :)\n')
            game_on = False
            sys.exit(1)
