### Binary tree
    - From every cell randomly carve north or east
    - usually start from southwest and goes east
    - must visit every cell

### Sidewinder algorythm
    - start at west most column (usually soutwest cell)
    - 0 - carvs east
    - 1 - carvs north in randomly selected cell from recent run (path created by recntly joined cells)
    - must visit every cell

### The Aldous-Broder Algorithm
    - start anywhere
    - choose a random neighbor and move to in
    - link to prior cell
    - repeat until every cell has been visited
    - it is just a random walk
    - time consuming!

### Wilsons Algorithm
    - start anywhere
    - loop-erased random walk