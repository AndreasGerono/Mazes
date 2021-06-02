from coloredGrid import ColoredGrid

from recursive_backtracker import RecursiveBacktracker


new_grid = ColoredGrid(20, 20)
RecursiveBacktracker.on(new_grid)
middle = new_grid[0, 0]
new_grid.distances = middle.distances()
file_name = 'recursive_backtracker.png'
new_grid.to_png(file_name)
print(f'No deadends: {len(new_grid.deadends())}')
