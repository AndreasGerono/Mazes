import png
import numpy as np

GREY = (200, 200, 200)
WHITE = (255, 255, 255)


class PNG_handler(object):
    """docstring for PNG_handler"""
    def __init__(self, width, height):
        super(PNG_handler, self).__init__()
        self.width = width+2
        self.height = height+2
        self.buffer = np.zeros((height+2, width+2, 3), dtype=int)

    def __prepare_buffer__(self):
        grid = []
        for r in range(self.height):
            rows = []
            for c in range(self.width):
                rows.append(GREY)
            grid.append(rows)
        return grid

    def __write_h_points__(self, x1, x2, y1, color=WHITE):
        for x in range(self.width):
            if (x1 <= x < x2) and y1 < self.height:
                self.buffer[y1][x] = color

    def __write_v_points__(self, y1, y2, x1, color=WHITE):
        for y in range(self.height):
            if (y1 <= y < y2) and x1 < self.width:
                self.buffer[y][x1] = color

    def write_h_line(self, x1, x2, y, height=2, color=WHITE):
        for i in range(height):
            self.__write_h_points__(x1, x2, y+i, color)

    def write_v_line(self, y1, y2, x, height=2, color=WHITE):
        for i in range(height):
            self.__write_v_points__(y1, y2, x+i, color)

    def rect(self, x, y, w, h, color):
        self.write_h_line(x, x+w, y, h, color)

    @property
    def flat_buffer(self):
        flat_buffer = []
        for row in self.buffer:
            rows = []
            for column in row:
                for rgb in column:
                    rows.append(rgb)

            flat_buffer.append(rows)

        return flat_buffer

    def to_png(self, file_name='maze.png'):
        w = png.Writer(self.width, self.height, greyscale=False)
        with open(file_name, 'wb') as f:
            w.write(f, self.flat_buffer)


def main():

    width = 100
    height = 100
    cell_size = 20

    handle = PNG_handler(width, height)

    x1 = 0
    y1 = 0
    x2 = (0+1)*cell_size
    y2 = (0+1)*cell_size

    for row in range(width):
        for col in range(height):
            x1 = row*cell_size
            y1 = col*cell_size
            x2 = (row+1)*cell_size
            y2 = (col+1)*cell_size
            handle.write_v_line(x1, x2, y2)
            handle.write_v_line(x1, x2, y1)
            handle.write_h_line(y1, y2, x1)
            handle.write_h_line(y1, y2, x2)

            # if row == rect_loc[0] and col == rect_loc[1]:

    handle.rect(1*cell_size, 4*cell_size, cell_size, cell_size, (255, 0, 0))

    handle.to_png()


if __name__ == '__main__':
    main()
