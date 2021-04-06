import random


class Wilson(object):
    """docstring for Wilson"""
    def on(grid):
        cell = grid.random_cell()
        unvisited = [cell for cell in grid.each_cell()]
        first = random.choice(unvisited)
        unvisited.remove(first)

        while unvisited:
            cell = random.choice(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = random.choice(cell.neighbours())
                if cell in path:
                    position = path.index(cell)
                    path = path[:position+1]
                else:
                    path.append(cell)

            for index in range(len(path)-1):
                path[index].link(path[index+1])
                unvisited.remove(path[index])

        return grid
