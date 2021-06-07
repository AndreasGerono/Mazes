import png
import numpy as np

GREY = (200, 200, 200, 128)
WHITE = (255, 255, 255, 128)
BLACK = (0, 0, 0, 255)


class PNG_handler(object):
    """docstring for PNG_handler"""
    def __init__(self, width, height):
        super(PNG_handler, self).__init__()
        self.width = width+4
        self.height = height+4
        self.buffer = np.zeros((self.height, self.width, 4), dtype=np.uint8)

    def write_h_line(self, x1, x2, y, height=4, color=BLACK):
        self.buffer[y:y+height, x1:x2] = color

    def write_v_line(self, y1, y2, x, height=4, color=BLACK):
        self.buffer[y1:y2, x: x+height] = color

    def rect(self, x, y, w, h, color=WHITE):
        self.write_h_line(x, x+w, y, h, color)

    @property
    def flat_buffer(self):
        flat = np.reshape(self.buffer, (self.height, -1))
        return flat.tolist()

    def to_png(self, file_name='maze.png'):
        w = png.Writer(self.width, self.height, alpha='RGBA', greyscale=False)
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

    handle.rect(1*cell_size, 4*cell_size, cell_size, cell_size, (255, 0, 0, 128))  # noqa: E501

    handle.to_png()


if __name__ == '__main__':
    main()
