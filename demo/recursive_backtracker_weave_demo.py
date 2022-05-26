from mazes.weave_grid import WeaveGrid
from mazes.recursive_backtracker import RecursiveBacktracker


new_grid = WeaveGrid(20, 20)
RecursiveBacktracker.on(new_grid)
new_grid.braid(0.1)
start, finish = new_grid[0, 0], new_grid[new_grid.rows-1, new_grid.columns-1]

distances = start.distances
new_start, distance = distances.max()

new_distances = new_start.distances
goal, distances = new_distances.max()

new_grid.distances = new_distances.path_to(goal)
new_grid.to_png(file_name='recursive_backtracker_weave.png', inset=0.2, cell_size=60, line_thickness=2)  # noqa: E501
print(f'No deadends: {len(new_grid.deadends())}')
print(new_start, goal. distances.max())
