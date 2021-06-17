from weighted_cell import WeightedCell
from grid import Grid


class WeightedGrid(Grid):
    def __init__(self, rows, columns):
        self.maximum = 0
        super().__init__(rows, columns)

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        _, self.maximum = distances.max()

    def prepare_grid(self):
        grid = []
        for row in range(self.rows):
            rows = []
            for col in range(self.columns):
                cell = WeightedCell(row, col)
                rows.append(cell)
            grid.append(rows)

        return grid

    def background_color_for_cell(self, cell):
        if cell.weight > 1:
            return [0, 0, 255, 255]

        distance = self.distances[cell]
        if distance is not None:
            intensity = float(self.maximum - distance) / self.maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            color = [dark, bright, dark]

            color.append(255)
            return color
