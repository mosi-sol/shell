import random

# set of decisions
decisions = [
    {'name': 'Invest in education', 'rate': 1.1},
    {'name': 'Focus on agriculture', 'rate': 1.2},
    {'name': 'Embrace technology', 'rate': 1.3},
    {'name': 'Governance', 'rate': 1.1},
    {'name': 'Infrastructure', 'rate': 1.2},
    {'name': 'Social equality', 'rate': 1.3},
    {'name': 'Healthcare', 'rate': 1.1},
    {'name': 'Environmental sustainability', 'rate': 1.2}
]

# create a generation
def create_generation(decisions):
    return [random.choice(decisions) for i in range(10)]

# calculate the growth rate for a generation
def calculate_growth_rate(generation):
    return round(sum([d['rate'] for d in generation]) / 10, 2)

# simulate a world with 6 generations
def simulate_world():
    generations = []
    for i in range(6):
        if i == 1:
            decisions.append({'name': 'Governance', 'rate': 1.1})
        elif i == 2:
            decisions.append({'name': 'Infrastructure', 'rate': 1.2})
        elif i == 3:
            decisions.append({'name': 'Social equality', 'rate': 1.3})
        elif i == 4:
            decisions.append({'name': 'Healthcare', 'rate': 1.1})
        elif i == 5:
            decisions.append({'name': 'Environmental sustainability', 'rate': 1.2})
        generation = create_generation(decisions)
        growth_rate = calculate_growth_rate(generation)
        generations.append({'generation': i+1, 'decisions': generation, 'growth_rate': growth_rate})
    return generations

# simulate 5 parallel worlds
worlds = [simulate_world() for i in range(5)]

# print the results in a vertical chart
print("".ljust(20), end="")
for i in range(5):
    print(f"World {i+1}".ljust(30), end="")
print()

for i in range(6):
    print(f"Generation {i+1}:".ljust(20), end="")
    for j in range(5):
        decisions = worlds[j][i]['decisions']
        growth_rate = worlds[j][i]['growth_rate']
        print(f"{', '.join([d['name'] + ' (' + str(d['rate']) + ')' for d in decisions])}: {growth_rate}".ljust(30), end="")
    print()

# print the results in a horizontal chart
for world in worlds:
    print(f"\nWorld {worlds.index(world)+1}:")
    for generation in world:
        decisions = generation['decisions']
        growth_rate = generation['growth_rate']
        print(f"Generation {generation['generation']}: {', '.join([d['name'] + ' (' + str(d['rate']) + ')' for d in decisions])}: {growth_rate}")