"""
abstract parallels world build with different decisions of people.

- this is an algorithm to make an abstract parallels world. 
these worlds have people and for 6 generation they make decision very common agreements on each generation. 
the future population need these decisions for growth rate.
"""
import random

# Define the number of worlds and generations
num_worlds = 5
num_generations = 6

# Define the list of decisions for each generation
decisions = ["invest in education", "focus on agriculture", "embrace technology"]

# Create a list to store the population of each world for each generation
populations = [[0 for i in range(num_generations)] for j in range(num_worlds)]

# For each world
for world in range(num_worlds):
    # Initialize the population for the first generation
    populations[world][0] = 1000
    
    # For each generation
    for generation in range(1, num_generations):
        # Randomly select decisions from the list of decisions for the generation
        decision1, decision2, decision3 = random.sample(decisions, 3)
        
        # Evaluate the decisions and calculate the population growth rate based on the decisions
        if decision1 == "invest in education":
            growth_rate1 = 1.1
        else:
            growth_rate1 = 0.9
            
        if decision2 == "focus on agriculture":
            growth_rate2 = 1.2
        else:
            growth_rate2 = 0.8
            
        if decision3 == "embrace technology":
            growth_rate3 = 1.3
        else:
            growth_rate3 = 0.7
        
        # Apply the population growth rate to the current population to get the population for the next generation
        population = populations[world][generation-1]
        population = int(population * growth_rate1 * growth_rate2 * growth_rate3)
        
        # Store the population for the current generation in the list of populations for the world
        populations[world][generation] = population

        # Print the decisions for the current generation
        print(f"World {world+1}, Generation {generation}: {decision1}, {decision2}, {decision3}")

        # Print the population and growth rate for the current generation
        print(f"World {world+1}, Generation {generation}: Population = {population}, Growth Rate = {growth_rate1 * growth_rate2 * growth_rate3}\n")

# Display the population data for each world in a vertical and horizontal chart
print("Population data for each world:")
for world in range(num_worlds):
    print(f"World {world+1}: {populations[world]}")
    
print("\nPopulation data in a horizontal chart:")
for generation in range(num_generations):
    print(f"Generation {generation+1}: ", end="")
    for world in range(num_worlds):
        print(f"{populations[world][generation]:5d} ", end="")
    print()

print("\nPopulation data in a vertical chart:")
for world in range(num_worlds):
    print(f"World {world+1}:")
    for generation in range(num_generations):
        print(f"Generation {generation+1}: {populations[world][generation]:5d}")
    print()