from coloredGrid import ColoredGrid

from hunt_and_kill import HuntAndKill


new_grid = ColoredGrid(20, 20)
HuntAndKill.on(new_grid)
middle = new_grid[10, 10]
new_grid.distances = middle.distances()
file_name = 'hunt_and_kill.png'
new_grid.to_png(file_name)
print(f'No deadends: {len(new_grid.deadends())}')
