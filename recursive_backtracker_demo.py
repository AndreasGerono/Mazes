from coloredGrid import ColoredGrid

from recursive_backtracker import RecursiveBacktracker


new_grid = ColoredGrid(35, 70)
RecursiveBacktracker.on(new_grid)
middle = new_grid[int(new_grid.rows/2), int(new_grid.columns/2)]
new_grid.distances = middle.distances()
file_name = 'recursive_backtracker.png'
new_grid.to_png(file_name, cell_size=50)
print(f'No deadends: {len(new_grid.deadends())}')
