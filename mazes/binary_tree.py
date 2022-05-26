import random


class BinaryTree(object):
    """docstring for BinaryTree"""
    def on(grid):
        for cell in grid.each_cell():
            neighbours = []
            if cell.south:
                neighbours.append(cell.south)
            if cell.west:
                neighbours.append(cell.west)

            if neighbours:
                neighbour = random.choice(neighbours)
                cell.link(neighbour)

        return grid
