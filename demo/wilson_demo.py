from mazes.grid import Grid
from mazes.wilson import Wilson

new_grid = Grid(20, 20)
new_grid = Wilson.on(new_grid)
print(new_grid)
