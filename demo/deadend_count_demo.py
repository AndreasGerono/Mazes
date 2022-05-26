from mazes.hunt_and_kill import HuntAndKill
from mazes.wilson import Wilson
from mazes.aldous_broder import AldousBroder
from mazes.sidewinder import Sidewinder
from mazes.binary_tree import BinaryTree
from mazes.recursive_backtracker import RecursiveBacktracker
from mazes.grid import Grid

algorithms = [BinaryTree, Sidewinder, AldousBroder, Wilson, HuntAndKill, RecursiveBacktracker]  # noqa: E501
tries = 100
size = 20

averages = {}

for algorithm in algorithms:
    deadends_counds = 0
    for i in range(tries):
        grid = Grid(size, size)
        algorithm.on(grid)
        deadends_counds += len(grid.deadends())

    averages[algorithm] = deadends_counds/tries

print(f'Average dead ends per {size}x{size} maze ({size*size}):')
sorted_avg = sorted(averages.items(), key=lambda elem: elem[1], reverse=True)
for elem in sorted_avg:
    fraction = elem[1] / (size*size)
    print(f'{elem[0]}, {elem[1]:.0f}/{size*size} ({fraction:.0%})')
