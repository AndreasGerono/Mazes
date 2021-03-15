from grid import Grid
from wilson import Wilson

new_grid = Grid(20, 20)
new_grid = Wilson.on(new_grid)
print(new_grid)
