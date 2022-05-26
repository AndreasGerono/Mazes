from mazes.grid import Grid
from mazes.sidewinder import Sidewinder

new_grid = Grid(20, 20)
Sidewinder.on(new_grid)
print(new_grid)
new_grid.to_png()
