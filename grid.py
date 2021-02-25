import random
from cell import Cell
from png_handler import PNG_handler


class Grid(object):
    """docstring for Grid"""
    def __init__(self, rows, columns):
        super(Grid, self).__init__()
        self.rows = rows
        self.columns = rows
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
                row, col = cell.row, cell.column
                self[r, c].north = self[row-1, col]
                self[r, c].south = self[row+1, col]
                self[r, c].west = self[row, col-1]
                self[r, c].east = self[row, col+1]

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
        return False

    def __str__(self):
        output = "+" + "----+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                body = self.content_of(cell)
                if cell.is_linked(cell.east):
                    east_boundry = " "
                else:
                    east_boundry = "|"

                top += body + east_boundry

                if cell.is_linked(cell.south):
                    south_boundry = "    "
                else:
                    south_boundry = "----"
                bottom += south_boundry + "+"

            output += top + "\n"
            output += bottom + "\n"

        return output

    def to_png(self, cell_size=50):

        handler = PNG_handler(self.columns*cell_size, self.rows*cell_size)  # noqa: E501

        for bg in range(2):
            for row in self.each_row():
                for cell in row:
                    x1 = cell.column * cell_size
                    y1 = cell.row * cell_size
                    x2 = (cell.column + 1) * cell_size
                    y2 = (cell.row + 1) * cell_size

                    if (bg == 0):
                        color = self.background_color_for_cell(cell)
                        if color is not None:
                            handler.rect(x1, y1, cell_size, cell_size, color)

                    else:
                        if cell.north is None:
                            handler.write_v_line(x1, x2, y1)    # North wall

                        if cell.west is None:
                            handler.write_h_line(y1, y2, x1)    # west wall

                        if not cell.is_linked(cell.east):
                            handler.write_h_line(y1, y2, x2)    # east wall

                        if not cell.is_linked(cell.south):
                            handler.write_v_line(x1, x2, y2)    # south wall
            handler.to_png()
