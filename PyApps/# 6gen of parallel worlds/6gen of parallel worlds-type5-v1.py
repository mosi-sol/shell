import random

def generate_decisions(num_generations):
    decisions = []
    for i in range(num_generations):
        if i == 0:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology'])
        elif i == 1:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology', 'governance'])
        elif i == 2:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology', 'governance', 'infrastructure'])
        elif i == 3:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology', 'governance', 'infrastructure', 'social equality'])
        elif i == 4:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology', 'governance', 'infrastructure', 'social equality', 'healthcare'])
        elif i == 5:
            decisions.append(['invest in education', 'focus on agriculture', 'embrace technology', 'governance', 'infrastructure', 'social equality', 'healthcare', 'environmental sustainability'])
    return decisions

def generate_population(numbers, decisions):
    population = []
    for i in range(numbers):
        generation = []
        for j in range(len(decisions)):
            decision = random.choice(decisions[j])
            generation.append(decision)
        population.append(generation)
    return population

def calculate_growth_rate(population):
    growth_rates = []
    for i in range(1, len(population)):
        previous_pop = set(population[i-1])
        current_pop = set(population[i])
        intersection = previous_pop.intersection(current_pop)
        growth_rate = len(intersection) / len(previous_pop)
        growth_rates.append(round(growth_rate, 2))
    return growth_rates

def generate_worlds(num_worlds, num_generations, num_population):
    worlds = []
    for i in range(num_worlds):
        decisions = generate_decisions(num_generations)
        population = generate_population(num_population, decisions)
        growth_rates = calculate_growth_rate(population)
        worlds.append({
            'decisions': decisions,
            'population': population,
            'growth_rates': growth_rates
        })
    return worlds

def print_worlds(worlds):
    for i in range(len(worlds)):
        print(f"World {i+1}")
        print("Decisions:")
        for j in range(len(worlds[i]['decisions'])):
            print(f"  Generation {j+1}: {', '.join(worlds[i]['decisions'][j])}")
        print("Population:")
        for j in range(len(worlds[i]['population'])):
            print(f"  Generation {j+1}: {', '.join(worlds[i]['population'][j])}")
        print("Growth Rates:")
        for j in range(len(worlds[i]['growth_rates'])):
            print(f"  Generation {j+2}: {worlds[i]['growth_rates'][j]}")
        print()

worlds = generate_worlds(5, 6, 10)
print_worlds(worlds)