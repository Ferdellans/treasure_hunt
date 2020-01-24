from oop import Treasure

DEFAULT_OUTPUT = [11, 55, 15, 21, 44, 32, 13, 25, 43]


class TestClass:

    # todo: assert isinstance trasure
    def setup(self):
        self.default = Treasure()
        self.random = Treasure(rows=10)

    def test_default_grid(self):
        self.default.create_grid()
        assert len(self.default.grid) == 5

    def test_random_grid(self):
        self.random.create_grid()
        assert len(self.random.grid) == 10

    def test_default_output(self):
        self.default.run()
        assert self.default.output == DEFAULT_OUTPUT
        assert len(self.default.output) == len(self.default.grid) * 2 - 1

    def test_random_output_value(self):
        self.random.run()
        coordinates = str(self.random.output[-2])
        x = int(coordinates[0]) - 1
        y = int(coordinates[1]) - 1
        treasure = self.random.grid[x][y]
        assert treasure == self.random.output[-1]


