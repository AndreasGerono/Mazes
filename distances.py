
class Distances(object):
    """docstring for Disance"""
    def __init__(self, root):
        super(Distances, self).__init__()
        self.root = root
        self.cells = dict()
        self.cells[self.root] = 0

    def __getitem__(self, cell):
        return self.cells.get(cell)

    def __setitem__(self, cell, distance):
        self.cells[cell] = distance

    def cells(self):
        return self.cells.keys()

    def path_to(self, goal):
        print(goal)
        current = goal

        breadcrubs = Distances(self.root)
        breadcrubs[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrubs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    continue

        return breadcrubs

    def max(self):
        max_discance = 0
        max_cell = self.root
        for cell, distance in self.cells.items():
            if distance > max_discance:
                max_cell = cell
                max_discance = distance

        return max_cell, max_discance
