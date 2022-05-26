from mazes.mask import Mask
from mazes.masked_grid import MaskedGrid
from mazes.recursive_backtracker import RecursiveBacktracker


new_mask = Mask((20, 20))

new_mask[0, 0] = False
new_mask[8, 0] = False
new_mask[0, 8] = False
new_mask[8, 8] = False
new_mask[4, 4] = False

grid = MaskedGrid(new_mask)
RecursiveBacktracker.on(grid)
middle = grid[10, 10]
grid.distances = middle.distances
file_name = 'simple_mask_grid.png'
grid.to_png(file_name)


# +---+---+---+---+---+
# |   |   |           |
# +---+   +---+---+   +
# |   |               |
# +   +---+---+---+   +
# |       |   |   |   |
# +   +---+---+   +   +
# |   |       |       |
# +   +   +   +   +---+
# |       |       |   |
# +---+---+---+---+---+
