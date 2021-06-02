import random


class HuntAndKill(object):
    """docstring for HuntAndKill"""
    def on(grid):
        current = grid.random_cell()

        while current is not None:
            unvisited_neighbours = [neighbour for neighbour in current.neighbours() if not neighbour.links]  # noqa: E501

            # Random walk
            if unvisited_neighbours:
                neighbour = random.choice(unvisited_neighbours)
                current.link(neighbour)
                current = neighbour

            # Hunt mode
            else:
                current = None

                for cell in grid.each_cell():
                    visited_neighbours = [neighbour for neighbour in cell.neighbours() if neighbour.links]  # noqa: E501
                    if not cell.links and visited_neighbours:
                        current = cell
                        neighbour = random.choice(visited_neighbours)
                        current.link(neighbour)
                        break
