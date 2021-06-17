from cell import Cell
from distances import Distances


class WeightedCell(Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.weight = 1

    @property
    def distances(self):
        weights = Distances(self)
        pending = [self]

        while pending:
            cell = min(pending, key=lambda cell: cell.weight)
            pending.remove(cell)

            for neighbour in cell.all_links():
                total_weight = weights[cell] + neighbour.weight
                if weights[neighbour] is None or total_weight < weights[neighbour]:  # noqa E501
                    pending.append(neighbour)
                    weights[neighbour] = total_weight

        return weights
