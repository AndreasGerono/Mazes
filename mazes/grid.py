import random
from .cell import Cell
import numpy as np
import cv2 as cv

BLACK = (0, 0, 0, 255)
TRANSPARENT = (0, 0, 0, 0)


class Grid(object):
    """docstring for Grid"""
    def __init__(self, rows, columns):
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

    def __getitem__(self, row_col) -> Cell:
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

    def deadends(self) -> list[Cell]:
        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def random_cell(self) -> Cell:
        row = random.randrange(self.rows)
        col = random.randrange(self.columns)

        return self[row, col]

    def size(self):
        return self.rows * self.columns

    def each_row(self) -> list[list[Cell]]:
        return (row for row in self.grid)

    def each_cell(self) -> Cell:
        return (cell for row in self.each_row() for cell in row)

    def content_of(self, cell):
        return "    "

    def background_color_for_cell(self, cell):
        return None

    def braid(self, p=1):
        deadends = self.deadends()
        random.shuffle(deadends)

        for cell in deadends:
            if len(cell.links) != 1 or random.random() > p:
                continue

            neighbours = [n for n in cell.neighbours() if not cell.is_linked(n)]  # find all not linked neighbours # noqa: E501
            # Look optimalizaion - prefer linking to deadends.
            best = [n for n in neighbours if len(n.links) == 1]
            if not best:
                best = neighbours

            neighbour = random.choice(best)
            cell.link(neighbour)

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

    def to_png(self, file_name='maze.png', cell_size=60, line_thickness=1, inset=0):  # noqa E501
        height = self.rows * cell_size + line_thickness
        width = self.columns * cell_size + line_thickness
        img = np.zeros((height, width, 4), np.uint8)
        inset = round(cell_size * inset)
        for mode in ("bg", "walls"):
            for cell in self.each_cell():
                if cell is None:
                    continue
                x = cell.column * cell_size
                y = cell.row * cell_size

                if inset > 0:
                    self._png_with_inset(img, cell, mode, cell_size, x, y, inset, line_thickness)  # noqa E501
                else:
                    self._png_without_inset(img, cell, mode, cell_size, x, y, line_thickness)  # noqa E501

        cv.imwrite(file_name, img)

    @staticmethod
    def _cell_cordinates_with_inset(x, y, cell_size, inset, line_thickness):
        x1, x4 = x - line_thickness, x + cell_size
        x2 = x1 + inset
        x3 = x4 - inset

        y1, y4 = y - line_thickness, y + cell_size
        y2 = y1 + inset
        y3 = y4 - inset
        return x1, x2, x3, x4, y1, y2, y3, y4


    def _png_with_inset(self, img, cell, mode, cell_size, x, y, inset, line_thickness):  # noqa E501
        x1, x2, x3, x4, y1, y2, y3, y4 = self._cell_cordinates_with_inset(x, y, cell_size, inset, line_thickness)  # noqa E501
        if mode == "bg":
            x2 += round(line_thickness/2)
            x3 -= round(line_thickness/2)
            y2 += round(line_thickness/2)
            y3 -= round(line_thickness/2)

            color = self.background_color_for_cell(cell)
            thickness = -1
            if color is not None:
                cv.rectangle(img, (x2, y2), (x3, y3), color, thickness)
                if cell.is_linked(cell.north) and self.background_color_for_cell(cell.north):  # noqa: E501
                    cv.rectangle(img, (x2, y2), (x3, y1), color, thickness)
                if cell.is_linked(cell.south) and self.background_color_for_cell(cell.south):  # noqa: E501
                    cv.rectangle(img, (x2, y3), (x3, y4), color, thickness)  # noqa: E501
                if cell.is_linked(cell.east) and self.background_color_for_cell(cell.east):  # noqa: E501
                    cv.rectangle(img, (x3, y2), (x4, y3), color, thickness)
                if cell.is_linked(cell.west) and self.background_color_for_cell(cell.west):  # noqa: E501
                    cv.rectangle(img, (x1, y2), (x2, y3), color, thickness)
        else:
            if cell.is_linked(cell.north):
                cv.line(img, (x2, y1), (x2, y2), BLACK, line_thickness)
                cv.line(img, (x3, y1), (x3, y2), BLACK, line_thickness)
            else:
                cv.line(img, (x2, y2), (x3, y2), BLACK, line_thickness)

            if cell.is_linked(cell.south):
                cv.line(img, (x2, y3), (x2, y4), BLACK, line_thickness)
                cv.line(img, (x3, y3), (x3, y4), BLACK, line_thickness)
            else:
                cv.line(img, (x2, y3), (x3, y3), BLACK, line_thickness)

            if cell.is_linked(cell.west):
                cv.line(img, (x1, y2), (x2, y2), BLACK, line_thickness)
                cv.line(img, (x1, y3), (x2, y3), BLACK, line_thickness)
            else:
                cv.line(img, (x2, y2), (x2, y3), BLACK, line_thickness)

            if cell.is_linked(cell.east):
                cv.line(img, (x3, y2), (x4, y2), BLACK, line_thickness)
                cv.line(img, (x3, y3), (x4, y3), BLACK, line_thickness)
            else:
                cv.line(img, (x3, y2), (x3, y3), BLACK, line_thickness)


    def _png_without_inset(self, img, cell, mode, cell_size, x, y, line_thickness):  # noqa E501
        x1, y1 = x, y
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        line_thickness = 1

        if mode == "bg":
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
