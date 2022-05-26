from mazes.coloredGrid import ColoredGrid
from mazes.wilson import Wilson


for i in range(1):
    new_grid = ColoredGrid(20, 20)
    Wilson.on(new_grid)
    middle = new_grid[0, 0]
    new_grid.distances = middle.distances
    file_name = 'wilson.png'
    new_grid.to_png(file_name)
