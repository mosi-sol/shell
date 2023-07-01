import random

DECISIONS = ["invest in education", "focus on agriculture", "embrace technology"]
TITLES = ["World 1", "World 2", "World 3", "World 4", "World 5"]
GENERATIONS = 6

def generate_population():
    return random.randint(1000000, 1500000)

def calculate_growth_rate(decisions):
    growth_rate = 1
    rates = []
    for decision in decisions:
        if decision == "invest in education":
            rate = random.uniform(1.01, 1.05)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "focus on agriculture":
            rate = random.uniform(1.02, 1.08)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "embrace technology":
            rate = random.uniform(1.03, 1.10)
            rates.append((decision, rate))
            growth_rate *= rate
    return round(growth_rate, 2), rates

def generate_decisions(generation):
    decisions = []
    if generation >= 2:
        decisions.append(random.choice(["centralized governance", "decentralized governance"]))
    if generation >= 3:
        decisions.append(random.choice(["build more roads", "invest in public transportation"]))
    if generation >= 4:
        decisions.append(random.choice(["income equality", "gender equality"]))
    if generation >= 5:
        decisions.append(random.choice(["universal healthcare", "private healthcare"]))
    if generation >= 6:
        decisions.append(random.choice(["renewable energy", "fossil fuels"]))
    decisions.append(random.choice(DECISIONS))
    decisions.append(random.choice(DECISIONS))
    return decisions

def simulate_world(title, generation, population, decisions):
    if generation > GENERATIONS:
        return
    growth_rate, rates = calculate_growth_rate(decisions)
    new_population = round(population * growth_rate)
    print(f"{title} - Generation {generation}: {new_population} ({growth_rate})")
    print(f"{' '*len(title)}   Decisions:")
    for decision_rate in rates:
        print(f"{' '*len(title)}   - {decision_rate[0]}: {decision_rate[1]}")
    simulate_world(title, generation+1, new_population, generate_decisions(generation+1))

for i in range(len(TITLES)):
    print(f"\n{TITLES[i]}")
    initial_population = generate_population()
    initial_decisions = generate_decisions(1)
    simulate_world(TITLES[i], 1, initial_population, initial_decisions)