import random
from weighted_grid import WeightedGrid
from recursive_backtracker import RecursiveBacktracker


new_grid = WeightedGrid(20, 20)
RecursiveBacktracker.on(new_grid)
new_grid.braid(0.7)
start, finish = new_grid[0, 0], new_grid[new_grid.rows-1, new_grid.columns-1]
new_grid.distances = start.distances.path_to(finish)
new_grid.to_png(file_name='pictures/weighted_original.png', inset=0.2, cell_size=60, line_thickness=2)  # noqa: E501
lava = random.choice(new_grid.distances.cells)
lava.weight = 50
new_grid.distances = start.distances.path_to(finish)
new_grid.to_png(file_name='pictures/weighted_rerouter.png', inset=0.2, cell_size=60, line_thickness=2)  # noqa: E501
print(f'No deadends: {len(new_grid.deadends())}')
