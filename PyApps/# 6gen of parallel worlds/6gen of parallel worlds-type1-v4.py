"""
abstract parallels world build with different decisions of people.

- this is an algorithm to make an abstract parallels world. 
these worlds have people and for 6 generation they make decision very common agreements on each generation. 
the future population need these decisions for growth rate.
"""
import random

# Define the number of parallel worlds to create
num_worlds = 5

# Define the decision points for each generation
decision_points = {
    1: ["A", "B", "C"],
    2: ["yes", "no"],
    3: ["option 1", "option 2", "option 3"],
    4: ["yes", "no"],
    5: ["option A", "option B", "option C"],
    6: ["option X", "option Y", "option Z"]
}

# Generate the first generation of people for each world
worlds = []
for i in range(num_worlds):
    world = []
    for j in range(len(decision_points)):
        decision = random.choice(decision_points[j+1])
        world.append(decision)
    worlds.append(world)

# Generate the subsequent generations for each world
for i in range(1, 6):
    for j in range(num_worlds):
        for k in range(len(decision_points)):
            decision = worlds[j][k]
            for l in range(j):
                prev_decision = worlds[l][k]
                if prev_decision != decision:
                    decision = random.choice(decision_points[k+1])
                    break
            worlds[j][k] = decision

# Display the final decisions for each parallel world in a vertical chart
for i in range(num_worlds):
    print(f"World {i+1}")
    for j in range(len(decision_points)):
        print(f"Generation {j+1}: {worlds[i][j]}")
    print()

# Display the final decisions for each parallel world in a horizontal chart
max_gen_len = max([len(f"Generation {i+1}") for i in range(len(decision_points))])
max_world_len = max([len(f"World {i+1}") for i in range(num_worlds)])
for i in range(num_worlds):
    print(f"World {i+1}:")
    for j in range(len(decision_points)):
        gen_str = f"Generation {j+1}:"
        world_str = f"World {i+1}:"
        decision_str = worlds[i][j]
        print(f"{world_str.ljust(max_world_len+2)} {gen_str.ljust(max_gen_len+2)} {decision_str}")
    print()