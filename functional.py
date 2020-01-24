import more_itertools as mit
from pprint import pprint

grid = [
    [55, 14, 25, 52, 21],
    [44, 31, 11, 53, 43],
    [24, 13, 45, 12, 34],
    [42, 22, 43, 32, 41],
    [51, 23, 33, 54, 15]
]

output = [11]


def get_coordinates():
    coordinates = str(mit.last(output))
    x = int(coordinates[0]) - 1
    y = int(coordinates[1]) - 1
    return x, y


def run_functional():
    print(f'Run functional solution \n')
    pprint(grid)
    retry()

    print(f'OUTPUT {output}\n')


def retry():
    if len(output) < len(grid) * 2 - 1:
        x, y = get_coordinates()
        output.append(grid[x][y])
        return retry()
