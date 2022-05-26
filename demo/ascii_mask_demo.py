from mazes.mask import Mask
from mazes.masked_grid import MaskedGrid
from mazes.recursive_backtracker import RecursiveBacktracker

new_mask = Mask(file_name='mask2.txt')
new_grid = MaskedGrid(new_mask)
RecursiveBacktracker.on(new_grid)
middle = new_grid[15, 15]
new_grid.distances = middle.distances
file_name = 'ascii_demo_grid.png'
new_grid.to_png(file_name)
