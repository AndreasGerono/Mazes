import png

WHITE = 255
BLACK = 0


class PNG_handler(object):
    """docstring for PNG_handler"""
    def __init__(self, width, height):
        super(PNG_handler, self).__init__()
        self.width = width
        self.height = height
        self.buffer = self.__prepare_buffer__()

    def __prepare_buffer__(self):
        grid = []
        for r in range(self.height):
            rows = []
            for c in range(self.width):
                rows.append(WHITE)
            grid.append(rows)
        return grid

    def __write_v_points__(self, x1, x2, y1):
        for y in range(self.height):
            for x in range(self.width):
                if (x1 <= x < x2) and y == y1:
                    self.buffer[y][x] = BLACK

    def __write_h_points__(self, y1, y2, x1):
        for y in range(self.height):
            for x in range(self.width):
                if (y1 <= y < y2) and x == x1:
                    self.buffer[y][x] = BLACK

    def write_v_line(self, x1, x2, y, height=2):
        for i in range(height):
            self.__write_v_points__(x1, x2, y+i)

    def write_h_line(self, y1, y2, x, height=2):
        for i in range(height):
            self.__write_h_points__(y1, y2, x+i)

    def to_png(self):
        w = png.Writer(self.width, self.height, greyscale=True)
        with open('maze.png', 'wb') as f:
            w.write(f, self.buffer)


def main():

    width = 100
    height = 100
    cell_size = 10

    handle = PNG_handler(width, height)

    x1 = 0
    y1 = 0
    x2 = (0+1)*cell_size
    y2 = (0+1)*cell_size

    for row in range(10):
        for col in range(5):
            x1 = row*cell_size
            y1 = col*cell_size
            x2 = (row+1)*cell_size
            y2 = (col+1)*cell_size
            handle.write_v_line(x1, x2, y2)
            handle.write_v_line(x1, x2, y1)
            handle.write_h_line(y1, y2, x1)
            handle.write_h_line(y1, y2, x2)

    handle.to_png()


if __name__ == '__main__':
    main()
