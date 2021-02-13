class Cell(object):
    """docstring for Cell"""
    def __init__(self, row, column):
        super(Cell, self).__init__()
        self.row = row
        self.column = column
        self.links = dict()
        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def all_links(self):
        return self.links.keys()

    def is_linked(self, cell):
        return cell in self.links

    def neighbours(self):
        neighbours = []
        if self.north is not None:
            neighbours.append(self.north)
        if self.south is not None:
            neighbours.append(self.south)
        if self.west is not None:
            neighbours.append(self.west)
        if self.east is not None:
            neighbours.append(self.east)

        return neighbours

    def __str__(self):
        return f'({self.row} {self.column})'
