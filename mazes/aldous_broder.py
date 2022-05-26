import random


class AldousBroder(object):
    """docstring for AldousBroder"""
    def on(grid):
        cell = grid.random_cell()
        unvisited = grid.size() - 1

        while (unvisited > 0):

            neighbor = random.choice(cell.neighbours())

            if not neighbor.links:
                cell.link(neighbor)
                unvisited -= 1
            cell = neighbor

        return grid
