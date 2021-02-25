from coloredGrid import ColoredGrid
from binary_tree import BinaryTree
from sidewinder import Sidewinder

grid = ColoredGrid(20, 20)
BinaryTree.on(grid)
# Sidewinder.on(grid)

start = grid[0, 0]
grid.distances = start.distances()

grid.to_png()
print(grid)