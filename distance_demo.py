from distancegrid import DistanceGrid
from sidewinder import Sidewinder

new_grid = DistanceGrid(5, 5)
Sidewinder.on(new_grid)

start = new_grid[0, 0]
distances = start.distances()
new_grid.distances = distances
print(new_grid)
new_grid.distances = distances.path_to(new_grid[new_grid.rows-1, 2])  # noqa: E501
print(new_grid)
