import random
import math as m
import cv2 as cv
import numpy as np
from .coloredGrid import ColoredGrid
from .polar_cell import PolarCell
from .grid import BLACK


class PolarGrid(ColoredGrid):
    def __init__(self, rows):
        super().__init__(rows, 1)

    def prepare_grid(self):
        rows = [row for row in range(self.rows)]
        row_height = 1 / self.rows
        rows[0] = [PolarCell(0, 0)]

        for row in range(1, self.rows):
            radius = row/self.rows
            circumference = 2 * m.pi * radius

            previous_cnt = len(rows[row-1])
            est_cell_width = circumference/previous_cnt
            ratio = round(est_cell_width/row_height)
            cells = previous_cnt * ratio
            rows[row] = [PolarCell(row, col) for col in range(cells)]

        return rows

    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            col = cell.column

            if row > 0:
                cell.cw = self[row, col + 1]
                cell.ccw = self[row, col - 1]
                ratio = len(self.grid[row]) / len(self.grid[row - 1])
                parent = self.grid[row - 1][int(col / ratio)]
                parent.outward.append(cell)
                cell.inward = parent

    def random_cell(self):
        row = random.randrange(self.rows)
        col = random.randrange(len(self.grid[row]))
        return self.grid[row][col]

    def __getitem__(self, row_col):
        row, col = row_col
        if (0 <= row < self.rows):
            col %= len(self.grid[row])
            return self.grid[row][col]
        else:
            return None

    def to_png(self, file_name, cell_size=30, line_thickness=1):
        img_size = 2 * self.rows * (1 + cell_size)
        img = np.zeros((img_size, img_size, 4), np.uint8)
        center = int(img_size/2)
        radius = int(self.rows * cell_size) + line_thickness
        for bg in range(2):
            for cell in self.each_cell():
                if cell.row == 0:
                    continue

                theta = 2 * m.pi / len(self.grid[cell.row])
                inner_radius = cell.row * cell_size
                outer_radius = (cell.row + 1) * cell_size
                theta_ccw = cell.column * theta
                theta_cw = (cell.column + 1) * theta

                ax = round(center + (inner_radius * m.cos(theta_ccw)))
                ay = round(center + (inner_radius * m.sin(theta_ccw)))
                bx = round(center + (outer_radius * m.cos(theta_ccw)))
                by = round(center + (outer_radius * m.sin(theta_ccw)))
                cx = round(center + (inner_radius * m.cos(theta_cw)))
                cy = round(center + (inner_radius * m.sin(theta_cw)))
                dx = round(center + (outer_radius * m.cos(theta_cw)))
                dy = round(center + (outer_radius * m.sin(theta_cw)))

                if bg == 0:
                    color = self.background_color_for_cell(cell)
                    if color is not None:
                        polygon = np.asanyarray([[[ax, ay], [bx, by], [dx, dy], [cx, cy]]])  # noqa: E501
                        cv.fillPoly(img, polygon, color, cv.LINE_AA)

                else:
                    if not cell.is_linked(cell.inward):
                        cv.line(img, (ax, ay), (cx, cy), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501

                    if not cell.is_linked(cell.cw):
                        cv.line(img, (cx, cy), (dx, dy), BLACK, line_thickness, cv.LINE_AA)  # noqa: E501

            cv.circle(img, (center, center), radius, BLACK, line_thickness+1, cv.LINE_AA)  # noqa: E501
            cv.imwrite(file_name, img)
