import base36
from grid import Grid


class DistanceGrid(Grid):
    """docstring for Grid"""
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None

    def content_of(self, cell):
        if self.distances and self.distances[cell] is not None:
            return " " + base36.dumps(self.distances[cell]).ljust(3)
        else:
            return super().content_of(cell)
