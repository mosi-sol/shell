import random

DECISIONS = ["invest in education", "focus on agriculture", "embrace technology"]
GOVERNANCE_DECISIONS = ["centralized governance", "decentralized governance"]
INFRASTRUCTURE_DECISIONS = ["build more roads", "invest in public transportation"]
SOCIAL_EQUALITY_DECISIONS = ["income equality", "gender equality"]
HEALTHCARE_DECISIONS = ["universal healthcare", "private healthcare"]
ENVIRONMENTAL_DECISIONS = ["renewable energy", "fossil fuels"]
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
        elif decision == "centralized governance":
            rate = random.uniform(1.01, 1.04)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "decentralized governance":
            rate = random.uniform(1.01, 1.04)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "build more roads":
            rate = random.uniform(1.01, 1.05)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "invest in public transportation":
            rate = random.uniform(1.02, 1.06)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "income equality":
            rate = random.uniform(1.01, 1.05)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "gender equality":
            rate = random.uniform(1.01, 1.05)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "universal healthcare":
            rate = random.uniform(1.02, 1.06)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "private healthcare":
            rate = random.uniform(1.01, 1.05)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "renewable energy":
            rate = random.uniform(1.03, 1.08)
            rates.append((decision, rate))
            growth_rate *= rate
        elif decision == "fossil fuels":
            rate = random.uniform(1.01, 1.06)
            rates.append((decision, rate))
            growth_rate *= rate
    return round(growth_rate, 2), rates

def generate_decisions(generation):
    decisions = []
    if generation >= 2:
        decisions.append(random.choice(GOVERNANCE_DECISIONS))
    if generation >= 3:
        decisions.append(random.choice(INFRASTRUCTURE_DECISIONS))
    if generation >= 4:
        decisions.append(random.choice(SOCIAL_EQUALITY_DECISIONS))
    if generation >= 5:
        decisions.append(random.choice(HEALTHCARE_DECISIONS))
    if generation >= 6:
        decisions.append(random.choice(ENVIRONMENTAL_DECISIONS))
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
    simulate_world(TITLES[i],1, initial_population, initial_decisions)