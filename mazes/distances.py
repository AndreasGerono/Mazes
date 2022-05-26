from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cell import Cell


class Distances(object):
    """docstring for Disance"""
    def __init__(self, root):
        super(Distances, self).__init__()
        self.root = root
        self._cells = dict()
        self._cells[self.root] = 0

    def __getitem__(self, cell):
        return self._cells.get(cell, None)

    def __setitem__(self, cell, distance):
        self._cells[cell] = distance

    @property
    def cells(self) -> list[Cell]:
        return list(self._cells)

    def path_to(self, goal: Cell):
        current = goal

        breadcrubs = Distances(self.root)
        breadcrubs[current] = self._cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self._cells[neighbor] < self._cells[current]:
                    breadcrubs[neighbor] = self._cells[neighbor]
                    current = neighbor
        return breadcrubs

    def max(self) -> tuple[Cell, int]:
        max_discance = 0
        max_cell = self.root
        for cell, distance in self._cells.items():
            if distance > max_discance:
                max_cell = cell
                max_discance = distance

        return max_cell, max_discance
