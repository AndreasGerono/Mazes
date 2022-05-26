import math as m
import cv2 as cv
import numpy as np
from .coloredGrid import ColoredGrid
from .hex_cell import HexCell
from .grid import BLACK


class HexGrid(ColoredGrid):
    def prepare_grid(self):
        grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                cell = HexCell(r, c)
                row.append(cell)
            grid.append(row)
        return grid

    def configure_cells(self):
        for cell in self.each_cell():
            if cell is not None:
                r, c = cell.row, cell.column

                if c % 2 == 0:
                    n_diag = r - 1
                    s_diag = r
                else:
                    n_diag = r
                    s_diag = r + 1

                cell.south = self[r+1, c]
                cell.north = self[r-1, c]
                cell.northwest = self[n_diag, c-1]
                cell.northeast = self[n_diag, c+1]
                cell.southwest = self[s_diag, c-1]
                cell.southeast = self[s_diag, c+1]

    def to_png(self, file_name, cell_size=20, line_thickness=1):
        a_size = cell_size/2.0
        b_size = cell_size*m.sqrt(3)/2
        height = b_size*2
        img_width = round(3*a_size*self.columns+a_size+0.5) + 2*line_thickness
        img_height = round(height*self.rows + b_size+0.5) + 2*line_thickness
        img = np.zeros((img_height, img_width, 4), np.uint8)

        for bg in range(0, 2):
            for cell in self.each_cell():
                if cell is None:
                    continue

                cx = cell_size + 3*cell.column * a_size
                cy = b_size + cell.row * height
                if cell.column % 2 != 0:
                    cy += b_size

                x_fw = round(cx-cell_size)
                x_nw = round(cx-a_size)
                x_ne = round(cx+a_size)
                x_fe = round(cx+cell_size)

                y_n = round(cy-b_size)
                y_m = round(cy)
                y_s = round(cy+b_size)

                if bg == 0:
                    color = self.background_color_for_cell(cell)
                    if color is not None:
                        points = np.asanyarray([[[x_fw, y_m], [x_nw, y_n], [x_ne, y_n],  # noqa: E501
                                                [x_fe, y_m], [x_ne, y_s], [x_nw, y_s]]])  # noqa: E501
                        cv.fillPoly(img, [points], color, cv.LINE_AA)

                else:
                    if cell.southwest is None:
                        cv.line(img, (x_fw, y_m), (x_nw, y_s), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501
                    if cell.northwest is None:
                        cv.line(img, (x_fw, y_m), (x_nw, y_n), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501
                    if cell.north is None:
                        cv.line(img, (x_nw, y_n), (x_ne, y_n), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501
                    if not cell.is_linked(cell.northeast):
                        cv.line(img, (x_ne, y_n), (x_fe, y_m), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501
                    if not cell.is_linked(cell.southeast):
                        cv.line(img, (x_fe, y_m), (x_ne, y_s), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501
                    if not cell.is_linked(cell.south):
                        cv.line(img, (x_ne, y_s), (x_nw, y_s), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501

        cv.imwrite(file_name, img)
