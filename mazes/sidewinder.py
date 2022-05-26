import random


class Sidewinder(object):
    """docstring for Sidewinder"""
    def on(grid):
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)

                should_close_out = False

                if cell.east is None:
                    should_close_out = True

                if cell.north and random.randrange(2) == 0:
                    should_close_out = True

                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                        run.clear()
                else:
                    cell.link(cell.east)

        return grid
