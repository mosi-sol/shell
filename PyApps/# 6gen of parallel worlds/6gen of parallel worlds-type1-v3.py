"""
abstract parallels world build with different decisions of people.

- this is an algorithm to make an abstract parallels world. 
these worlds have people and for 6 generation they make decision very common agreements on each generation. 
the future population need these decisions for growth rate.
"""
import random

# Define the size of the map
MAP_SIZE = (10, 10)

# Generate a random map using Perlin noise
def generate_map():
    # Generate a grid of random noise values
    grid = [[random.random() for y in range(MAP_SIZE[1])] for x in range(MAP_SIZE[0])]

    # Smooth the noise
    def smooth(grid):
        for x in range(1, MAP_SIZE[0] - 1):
            for y in range(1, MAP_SIZE[1] - 1):
                neighbors = [grid[x - 1][y - 1], grid[x][y - 1], grid[x + 1][y - 1],
                             grid[x - 1][y], grid[x][y], grid[x + 1][y],
                             grid[x - 1][y + 1], grid[x][y + 1], grid[x + 1][y + 1]]
                grid[x][y] = sum(neighbors) / len(neighbors)
        return grid

    # Smooth the noise using multiple passes
    for i in range(5):
        grid = smooth(grid)

    # Normalize the grid to values between 0 and 1
    grid_min = min(min(row) for row in grid)
    grid_max = max(max(row) for row in grid)
    grid = [[(value - grid_min) / (grid_max - grid_min) for value in row] for row in grid]

    return grid

# Generate the map and display it as a simple tree chart
map = generate_map()
for y in range(MAP_SIZE[1]):
    for x in range(MAP_SIZE[0]):
        value = map[x][y]
        if value > 0.8:
            print("X", end="")
        elif value > 0.6:
            print("O", end="")
        elif value > 0.4:
            print("-", end="")
        elif value > 0.2:
            print(".", end="")
        else:
            print(" ", end="")
    print()