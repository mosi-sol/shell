"""
abstract parallels world build with different decisions of people.

- this is an algorithm to make an abstract parallels world. 
these worlds have people and for 6 generation they make decision very common agreements on each generation. 
the future population need these decisions for growth rate.
"""
import random

# Define the decision options
decision_options = ["invest in education", "focus on agriculture", "embrace technology"]

# Define the population size
population_size = 10

# Define the number of generations
num_generations = 6

# Define the weights for each decision option based on its impact on population growth
decision_weights = {
    "invest in education": 1,
    "focus on agriculture": 0.5,
    "embrace technology": 2
}

# Define the amount of randomness to introduce in each generation
decision_noise = 0.1
growth_rate_noise = 0.1

# Define the sensitivity factor for each decision option
sensitivity_factors = {
    "invest in education": [1, 1, 1, 1, 1, 1],
    "focus on agriculture": [1, 1, 1, 1, 1, 1],
    "embrace technology": [0, 1, 1, 1, 1, 1]
}

# Initialize the matrix to store the decisions made by each generation
decisions_matrix = [[0 for _ in range(len(decision_options))] for _ in range(num_generations)]

# Generate the initial population
population = [[random.choice(decision_options) for _ in range(len(decision_options))] for _ in range(population_size)]

# Loop through each generation
for generation in range(num_generations):
    # Introduce some randomness by allowing individuals to randomly change their decisions, starting from the second generation
    if generation > 0:
        for individual_idx in range(population_size):
            if random.random() < decision_noise:
                decision_idx = random.randint(0, len(decision_options)-1)
                population[individual_idx][decision_idx] = random.choice(decision_options)
    # Loop through each individual in the population
    for individual_idx in range(population_size):
        # Calculate the weights for each decision option based on the previous generation's decisions, with some sensitivity to the decisions made by previous generations
        weights = {option: 0 for option in decision_options}
        for decision in population[individual_idx]:
            sensitivity_factor = sensitivity_factors[decision][generation]
            weights[decision] += sensitivity_factor * (1 + random.uniform(-decision_noise, decision_noise))
        # Make a decision based on the weights, with some randomness
        decision = max(weights, key=lambda x: weights[x] + random.uniform(-decision_noise, decision_noise))
        # Record the decision in the matrix
        decisions_matrix[generation][decision_options.index(decision)] += 1
    # Calculate the growth rate based on the decisions made in this generation, with some randomness
    growth_rate = sum([decision_weights[option] * (decisions_matrix[generation][idx] + random.uniform(-decision_noise, decision_noise)) for idx, option in enumerate(decision_options)])
    growth_rate += random.uniform(-growth_rate_noise, growth_rate_noise)
    print(f"Generation {generation+1}: Growth rate = {growth_rate}")
    
# Print the decisions matrix in a vertical chart
print("Decisions Matrix:")
for i in range(len(decision_options)):
    print(f"{decision_options[i]}: {' '.join([str(decisions_matrix[j][i]) for j in range(num_generations)])}")

# Print the decisions matrix in a horizontal chart
print("Decisions Matrix:")
for i in range(num_generations):
    print(f"Generation {i+1}: {' '.join([str(decisions_matrix[i][j]) for j in range(len(decision_options))])}")