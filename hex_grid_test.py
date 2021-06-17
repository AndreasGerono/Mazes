from recursive_backtracker import RecursiveBacktracker
from hex_grid import HexGrid


grid = HexGrid(20, 25)
RecursiveBacktracker.on(grid)
middle = grid[int(grid.rows/2), int(grid.columns/2)]
grid.distances = middle.distances
grid.to_png('pictures/hex_grid.png', 25, line_thickness=2)
