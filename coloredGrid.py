from grid import Grid


class ColoredGrid(Grid):
    """docstring for Grid"""
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.maximum = 0

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        far, self.maximum = distances.max()

    def background_color_for_cell(self, cell):
        distance = self.distances[cell]
        color = (0, 0, 0)
        if distance is not None:
            intensity = float(self.maximum - distance) / self.maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            color = (bright, dark, dark)

        return color
