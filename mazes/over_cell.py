from .cell import Cell


class OverCell(Cell):
    def __init__(self, row, column, grid):
        super().__init__(row, column)
        self.grid = grid

    def link(self, cell, bidi=True):
        neighbour: OverCell = None
        if self.north and self.north is cell.south:
            neighbour = self.north
        elif self.south and self.south is cell.north:
            neighbour = self.south
        elif self.east and self.east is cell.west:
            neighbour = self.east
        elif self.west and self.west is cell.east:
            neighbour = self.west

        if neighbour:
            self.grid.tunnel_under(neighbour)
        else:
            super().link(cell, bidi)

    def neighbours(self) -> list[Cell]:
        cells = super().neighbours()
        if self.can_tunnel_north():
            cells.append(self.north.north)
        if self.can_tunnel_south():
            cells.append(self.south.south)
        if self.can_tunnel_east():
            cells.append(self.east.east)
        if self.can_tunnel_west():
            cells.append(self.west.west)

        return cells

    def can_tunnel_north(self):
        return self.north and self.north.north \
            and self.north.horizontal_passage()

    def can_tunnel_south(self):
        return self.south and self.south.south \
            and self.south.horizontal_passage()

    def can_tunnel_east(self):
        return self.east and self.east.east \
            and self.east.vertical_passage()

    def can_tunnel_west(self):
        return self.west and self.west.west \
            and self.west.vertical_passage()

    def horizontal_passage(self):
        return self.is_linked(self.east) and self.is_linked(self.west) \
            and not self.is_linked(self.north) \
            and not self.is_linked(self.south)

    def vertical_passage(self):
        return self.is_linked(self.north) and self.is_linked(self.south) \
            and not self.is_linked(self.west) \
            and not self.is_linked(self.east)
