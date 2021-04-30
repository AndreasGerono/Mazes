import random


class HountAndKill(object):
    """docstring for HountAndKill"""
    def on(grid):
        cell = grid.random_cell()
        visited = list()
        visited.append(cell)

        while (len(visited) < grid.size()-1):
            neighbor = random.choice(cell.neighbours())

            while (neighbor in visited):
                neighbor = random.choice(cell.neighbours())

            if not neighbor.links:
                cell.link(neighbor)
                visited.update(cell)

            cell = neighbor
