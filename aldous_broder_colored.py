from coloredGrid import ColoredGrid
from aldous_broder import AldousBroder


for i in range(1):
    new_grid = ColoredGrid(20, 20)
    AldousBroder.on(new_grid)
    middle = new_grid[0, 0]
    new_grid.distances = middle.distances()
    file_name = f'aldous_broder.png'
    new_grid.to_png(file_name)
