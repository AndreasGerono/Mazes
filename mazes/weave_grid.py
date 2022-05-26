import cv2 as cv
from .over_cell import OverCell
from .grid import BLACK
from .coloredGrid import ColoredGrid
from .under_cell import UnderCell


class WeaveGrid(ColoredGrid):
    def __init__(self, rows, columns):
        self.under_cells: list[UnderCell] = []
        super().__init__(rows, columns)

    def prepare_grid(self):
        grid = []
        for row in range(self.rows):
            rows = []
            for col in range(self.columns):
                cell = OverCell(row, col, self)
                rows.append(cell)
            grid.append(rows)
        return grid

    def tunnel_under(self, over_cell: OverCell):
        under_cell = UnderCell(over_cell)
        self.under_cells.append(under_cell)

    def each_cell(self):
        for cell in super().each_cell():
            yield cell
        for cell in self.under_cells:
            yield cell

    def to_png(self, file_name, cell_size=30, line_thickness=2, inset=0.1):
        super().to_png(file_name=file_name, cell_size=cell_size,
                       line_thickness=line_thickness, inset=inset)

    def _png_with_inset(self, img, cell, mode, cell_size, x, y, inset, line_thickness):  # noqa: E501
        if isinstance(cell, OverCell):
            super()._png_with_inset(img, cell, mode, cell_size, x, y, inset, line_thickness)  # noqa: E501
        else:
            x1, x2, x3, x4, y1, y2, y3, y4 = self._cell_cordinates_with_inset(x, y, cell_size, inset, line_thickness)  # noqa: E501
            if mode == "bg":
                color = self.background_color_for_cell(cell)
                if color is not None:
                    thickness = -1
                    if cell.vertical_passage():
                        pass
                        cv.rectangle(img, (x2, y1), (x3, y2), color, thickness)
                        cv.rectangle(img, (x2, y3), (x3, y4), color, thickness)
                    else:
                        pass
                        cv.rectangle(img, (x1, y2), (x2, y3), color, thickness)
                        cv.rectangle(img, (x3, y2), (x4, y3), color, thickness)
            else:
                if cell.vertical_passage():
                    cv.line(img, (x2, y1), (x2, y2), BLACK, line_thickness)
                    cv.line(img, (x3, y1), (x3, y2), BLACK, line_thickness)
                    cv.line(img, (x2, y3), (x2, y4), BLACK, line_thickness)
                    cv.line(img, (x3, y3), (x3, y4), BLACK, line_thickness)
                else:
                    cv.line(img, (x1, y2), (x2, y2), BLACK, line_thickness)
                    cv.line(img, (x1, y3), (x2, y3), BLACK, line_thickness)
                    cv.line(img, (x3, y2), (x4, y2), BLACK, line_thickness)
                    cv.line(img, (x3, y3), (x4, y3), BLACK, line_thickness)
