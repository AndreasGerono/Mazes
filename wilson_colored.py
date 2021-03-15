from distancegrid import DistanceGrid
from coloredGrid import ColoredGrid

from wilson import Wilson


for i in range(1):
    # new_grid = DistanceGrid(10, 10)
    new_grid = ColoredGrid(20, 20)
    Wilson.on(new_grid)
    middle = new_grid[0, 0]
    new_grid.distances = middle.distances()
    file_name = f'maze_{i}.png'
    new_grid.to_png(file_name)
    print(new_grid)