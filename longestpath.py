from distancegrid import DistanceGrid
from binary_tree import BinaryTree
from sidewinder import Sidewinder

grid = DistanceGrid(15, 15)
# BinaryTree.on(grid)
Sidewinder.on(grid)

start = grid[0, 0]

distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distances = new_distances.max()

grid.distances = new_distances.path_to(goal)

print(grid)
grid.to_png()
