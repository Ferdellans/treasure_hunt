from functional import run_functional
from oop import Treasure


def main():
    print("Treasure hunt \n")

    run_functional()

    treasure = Treasure()  # static grid solution
    treasure.run()

    treasure = Treasure(rows=15)  # dynamic grid solution
    treasure.run()


if __name__ == '__main__':
    main()
