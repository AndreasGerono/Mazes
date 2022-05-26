import random


class RecursiveBacktracker(object):
    """docstring for RecursiveBacktracker"""
    def on(grid, current=None):
        if current is None:
            current = grid.random_cell()
        stack = [current]
        while stack:
            unvisited_neighbours = [neighbour for neighbour in current.neighbours() if not neighbour.links]  # noqa: E501
            if unvisited_neighbours:
                neighbour = random.choice(unvisited_neighbours)
                current.link(neighbour)
                current = neighbour
                stack.append(current)

            else:
                current = stack.pop()
