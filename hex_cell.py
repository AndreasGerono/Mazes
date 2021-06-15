from cell import Cell


class HexCell(Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.northwest = None
        self.northeast = None
        self.southeast = None
        self.southwest = None
        del self.west
        del self.east

    def neighbours(self):
        cells = []
        if self.north is not None:
            cells.append(self.north)
        if self.south is not None:
            cells.append(self.south)
        if self.northwest is not None:
            cells.append(self.northwest)
        if self.northeast is not None:
            cells.append(self.northeast)
        if self.southeast is not None:
            cells.append(self.southeast)
        if self.southwest is not None:
            cells.append(self.southwest)

        return cells
