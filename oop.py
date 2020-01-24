import random
import more_itertools as mit
from pprint import pprint


class Treasure(object):
    """
        Treasure map allowed only 5x5 or multiplied by 5 rows vs cells ie 10x10, 15x15 etc...
        Flow:
            1. default first output value = 11, ie 1,1 row,cell
            2. run()
            3. generate grid from default 5x5 or with random values 15x15
            4. run find output from grid
            5. while len of the output list is not proper len
                5.1 get last coordinates output[-1]
                5.2 get x,y coordinates by splitting int into 2 separate numbers
                5.3 x,y minus 1 because of index of arrays, starts from 0
            6. append founded treasure into output
            7. print output
    """

    def __init__(self, rows=5):
        if rows % 5 != 0:
            raise Exception("rows must be multiplied by 5 and >= 10")

        self.rows = rows
        self.grid = list()
        self.output = [11]  # default value 1.1 eq 11

    def __repr__(self):
        if self.output:
            return f'{self.output}'
        return f'Output not found yet'

    @staticmethod
    def __default_grid() -> list:
        return [
            [55, 14, 25, 52, 21],
            [44, 31, 11, 53, 43],
            [24, 13, 45, 12, 34],
            [42, 22, 43, 32, 41],
            [51, 23, 33, 54, 15]
        ]

    def create_grid(self):
        grid = []

        if self.rows == 5:
            self.grid = self.__default_grid()
            return

        for i in range(self.rows):
            row = [self.__random_value() for _ in range(self.rows)]

            grid.append(row)

        self.grid = grid

    @staticmethod
    def __random_value():
        """ if random number will be multiplied by 10 - logic error, so + 1"""
        number = random.randrange(10, 56, 1)
        if number % 10 == 0:
            number += 1
        return number

    @property
    def coordinates(self):
        coordinates = str(mit.last(self.output))
        x = int(coordinates[0]) - 1
        y = int(coordinates[1]) - 1
        return x, y

    def __find_output(self):
        while len(self.output) < self.rows + self.rows - 1:
            x, y = self.coordinates
            self.output.append(self.grid[x][y])
        print(f'OUTPUT {self.output}\n')

    def run(self):
        message = 'OO solution'
        if self.rows == 5:
            print(f'Run static grid 5x5 {message} \n')
        else:
            print(f'Run dynamic grid {message} \n')

        self.create_grid()
        pprint(self.grid)

        self.__find_output()
