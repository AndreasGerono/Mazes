from coloredGrid import ColoredGrid
from cell import Cell


class MaskedGrid(ColoredGrid):
    """docstring for MaskedGrid"""
    def __init__(self, mask):
        self.mask = mask
        super().__init__(mask.rows, mask.columns)

    def prepare_grid(self):
        grid = []
        for r in range(self.rows):
            rows = []
            for c in range(self.columns):
                cell = Cell(r, c) if self.mask[r, c] else None
                rows.append(cell)
            grid.append(rows)
        return grid

    def random_cell(self):
        row, col = self.mask.random_location()
        return self[row, col]

    def size(self):
        self.mask.count()
