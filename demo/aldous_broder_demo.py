from mazes.grid import Grid
from mazes.aldous_broder import AldousBroder

new_grid = Grid(5, 5)
AldousBroder.on(new_grid)

print(new_grid)
