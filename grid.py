import random
from cell import Cell
import numpy as np
import cv2 as cv


BLACK = (0, 0, 0, 255)
TRANSPARENT = (0, 0, 0, 0)


class Grid(object):
    """docstring for Grid"""
    def __init__(self, rows, columns):
        super(Grid, self).__init__()
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        grid = []
        for r in range(self.rows):
            rows = []
            for c in range(self.columns):
                cell = Cell(r, c)
                rows.append(cell)
            grid.append(rows)
        return grid

    def __getitem__(self, row_col):
        row, col = row_col
        if (0 <= row < self.rows) and (0 <= col < self.columns):
            return self.grid[row][col]
        else:
            return None

    def configure_cells(self):
        for r in range(self.rows):
            for c in range(self.columns):
                cell = self[r, c]
                if cell is not None:
                    cell.north = self[r-1, c]
                    cell.south = self[r+1, c]
                    cell.west = self[r, c-1]
                    cell.east = self[r, c+1]

    def deadends(self):
        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def random_cell(self):
        row = random.randrange(self.rows)
        col = random.randrange(self.columns)

        return self[row, col]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        return (row for row in self.grid)

    def each_cell(self):
        return (cell for row in self.each_row() for cell in row)

    def content_of(self, cell):
        return "    "

    def background_color_for_cell(self, cell):
        return None

    def __str__(self):
        output = "+" + "----+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                body = self.content_of(cell)
                if cell is not None and cell.is_linked(cell.east):
                    east_boundry = " "
                else:
                    east_boundry = "|"

                top += body + east_boundry

                if cell is not None and cell.is_linked(cell.south):
                    south_boundry = "    "
                else:
                    south_boundry = "----"
                bottom += south_boundry + "+"

            output += top + "\n"
            output += bottom + "\n"

        return output

    def to_png(self, file_name='maze.pnh', cell_size=30, line_thickness=1):
        height = self.rows * cell_size
        width = self.columns * cell_size
        img = np.zeros((height, width, 4), np.uint8)
        for bg in range(2):
            for row in self.each_row():
                for cell in row:
                    if cell is None:
                        continue

                    x1 = cell.column * cell_size
                    y1 = cell.row * cell_size
                    x2 = (cell.column + 1) * cell_size
                    y2 = (cell.row + 1) * cell_size

                    if bg == 0:
                        color = self.background_color_for_cell(cell)
                        thickness = -1
                        if color is not None:
                            cv.rectangle(img, (x1, y1), (x2, y2), color, thickness)  # noqa: E501

                    else:
                        if cell.north is None:
                            cv.line(img, (x1, y1), (x2, y1), BLACK, line_thickness)  # noqa: E501
                        if cell.west is None:
                            cv.line(img, (x1, y1), (x1, y2), BLACK, line_thickness)  # noqa: E501

                        if not cell.is_linked(cell.east):
                            cv.line(img, (x2, y1), (x2, y2), BLACK, line_thickness)  # noqa: E501
                        if not cell.is_linked(cell.south):
                            cv.line(img, (x1, y2), (x2, y2), BLACK, line_thickness)  # noqa: E501

        cv.imwrite(file_name, img)
