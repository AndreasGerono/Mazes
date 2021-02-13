from grid import Grid
from binary_tree import BinaryTree

new_grid = Grid(15, 15)
BinaryTree.on(new_grid)
print(new_grid)
new_grid.to_png()
