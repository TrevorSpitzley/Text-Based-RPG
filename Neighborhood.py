import random

class Neighborhood():

    def __init__(self):
        # Set up number of houses, location of houses, etc.
        self.num_houses = 4
        self.house_grid = [
                ['P', 'H', '.', '.', '.'],
                ['.', '.', '.', '.', '.'],
                ['H', '.', '.', '.', 'H'],
                ['.', '.', '.', 'H', '.'],
                ['.', '.', '.', '.', '.']
                ]
        # List of house locations with (0,0) being upper left spot
        self.house_locs = [(0, 1), (2, 0), (2, 4), (3, 3)]
        self.player_loc = [0, 0]
        self.houses = []
        self.generate_houses()

    def generate_houses(self):
        h1 = House()
        self.houses.append(h1)

    def check_player_loc(self):
        if self.player_loc in self.house_locs:
            return True
        else: 
            return False

    def walk_south(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a,b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if a < 4:
            self.house_grid[a][b] = '.'
            self.player_loc[0] += 1
            a,b = self.player_loc[0], self.player_loc[1]
            if self.house_grid[a][b] == 'H':
                self.num_houses -= 1
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have moved south. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else: 
            print('You can never leave the Neighborhood... Try another direction :)\n')
   
    def walk_north(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a,b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if a > 0:
            self.house_grid[a][b] = '.'
            self.player_loc[0] -= 1
            a,b = self.player_loc[0], self.player_loc[1]
            if self.house_grid[a][b] == 'H':
                self.num_houses -= 1
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked north. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else: 
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def walk_east(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a,b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if b < 4:
            self.house_grid[a][b] = '.'
            self.player_loc[1] += 1
            a,b = self.player_loc[0], self.player_loc[1]
            if self.house_grid[a][b] == 'H':
                self.num_houses -= 1
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked east. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else: 
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def walk_west(self):
        # Keep in mind, 'a' is the which list you want
        # and 'b' is the spot in the list
        a,b = self.player_loc[0], self.player_loc[1]

        # Error checking so no out of bounds error
        if b > 0:
            self.house_grid[a][b] = '.'
            self.player_loc[1] -= 1
            a,b = self.player_loc[0], self.player_loc[1]
            if self.house_grid[a][b] == 'H':
                self.num_houses -= 1
            self.house_grid[a][b] = 'P'
            # Print the locations in reverse order to make sense as coordiantes
            print('You have walked west. You are now at ({}, {}) in the Neighborhood!\n'.format(b, a))
        else: 
            print('You can never leave the Neighborhood... Try another direction :)\n')

    def remove_mon_house(self):
        self.mon_houses -= 1

    def print_grid(self):
        for line in self.house_grid:
            print(*line, sep= ' ')
        print('\n')

    def update(self):
        # Decrement mon_house
        # Check if 0, game over

