from .cell import Cell


class PolarCell(Cell):

    def __init__(self, row, column):
        self.outward = []
        self.cw = None
        self.ccw = None
        self.inward = None
        super().__init__(row, column)

    def neighbours(self):
        cells = []
        if self.cw:
            cells.append(self.cw)
        if self.ccw:
            cells.append(self.ccw)
        if self.inward:
            cells.append(self.inward)

        cells.extend(self.outward)

        return cells
