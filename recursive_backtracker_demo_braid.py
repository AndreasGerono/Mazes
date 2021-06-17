from coloredGrid import ColoredGrid
from recursive_backtracker import RecursiveBacktracker


new_grid = ColoredGrid(20, 20)
RecursiveBacktracker.on(new_grid)
middle = new_grid[0, 0]
file_name = 'recursive_backtracker_braid.png'
new_grid.braid(0.5)
new_grid.distances = middle.distances
new_grid.to_png(file_name=file_name, inset=0.2, line_thickness=4)
print(f'No deadends: {len(new_grid.deadends())}')
