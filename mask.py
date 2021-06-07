import random
import png


class Mask(object):
    """docstring for Mask"""
    def __init__(self, size=None, file_name=None, img_name=None):
        if file_name:
            self.bits = self.from_file(file_name)
        elif img_name:
            self.bits = self.from_png(img_name)

        else:
            self.rows = size[0]
            self.columns = size[1]
            self.bits = self.prepare_grid()

    def from_file(self, file_name):
        with open(file_name) as file:
            lines = [line.strip() for line in file]
            self.rows = len(lines)
            self.columns = len(lines[0])
            grid = []
            for row in range(self.rows):
                rows = []
                for col in range(self.columns):
                    rows.append(False if lines[row][col] == 'X' else True)
                grid.append(rows)

            return grid

    def from_png(self, img_name):
        data = png.Reader(filename=img_name).read()
        img_rows = data[2]
        self.rows = data[1]
        self.columns = data[0]

        grid = []
        for img_row in img_rows:
            row = []
            col_rgba = [img_row[i:i + 4] for i in range(0, len(img_row), 4)]
            for rgba in col_rgba:
                row.append(True if rgba[0] else False)
            grid.append(row)

        return grid

    def prepare_grid(self):
        grid = []
        for r in range(self.rows):
            rows = []
            for c in range(self.columns):
                rows.append(True)
            grid.append(rows)
        return grid

    def __getitem__(self, row_col):
        row, col = row_col
        if (0 <= row < self.rows) and (0 <= col < self.columns):
            return self.bits[row][col]
        else:
            return None

    def __setitem__(self, row_col, is_on):
        row, col = row_col
        if (0 <= row < self.rows) and (0 <= col < self.columns):
            self.bits[row][col] = is_on
        else:
            print("Index out of range!")

    def count(self):
        count = 0
        for row in range(self.rows):
            for col in range(self.columns):
                count += 1 if self.bits[row][col] else 0

        return count

    def random_location(self):
        while True:
            row = random.randrange(self.rows)
            col = random.randrange(self.columns)
            if self.bits[row][col]:
                return (row, col)
