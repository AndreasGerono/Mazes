from mazes.coloredGrid import ColoredGrid
from mazes.sidewinder import Sidewinder

grid = ColoredGrid(15, 15)
# BinaryTree.on(grid)
Sidewinder.on(grid)

start = grid[0, 0]

distances = start.distances
new_start, distance = distances.max()

new_distances = new_start.distances
goal, distances = new_distances.max()
grid.distances = new_distances.path_to(goal)

print(grid)
grid.to_png()
