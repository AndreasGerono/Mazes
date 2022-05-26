from mazes.polar_grid import PolarGrid
from mazes.recursive_backtracker import RecursiveBacktracker

grid = PolarGrid(20)
RecursiveBacktracker.on(grid)
middle = grid[int(grid.rows/2), int(grid.rows/2)]
grid.distances = middle.distances
grid.to_png("polar_grid_demo.png", cell_size=30)
