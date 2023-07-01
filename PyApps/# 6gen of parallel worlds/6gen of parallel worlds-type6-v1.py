import random

class ParallelWorlds:
    def __init__(self, num_worlds, num_generations):
        self.num_worlds = num_worlds
        self.num_generations = num_generations
        self.worlds = []
        self.decisions = {
            1: ["Invest in education", "Focus on agriculture", "Embrace technology"],
            2: ["Governance"],
            3: ["Infrastructure"],
            4: ["Social equality"],
            5: ["Healthcare"],
            6: ["Environmental sustainability"]
        }
    
    def generate_worlds(self):
        for i in range(self.num_worlds):
            world = []
            for j in range(self.num_generations):
                decisions = []
                for k in range(len(self.decisions)):
                    decision = random.choice(self.decisions[k+1])
                    decisions.append(decision)
                world.append(decisions)
            self.worlds.append(world)
    
    def calculate_population_growth(self):
        for i in range(self.num_worlds):
            print(f"\nWorld {i+1}:")
            print("Generation  Decisions".ljust(40) + "Population".ljust(20) + "Growth Rate")
            print("-"*70)
            population = 1000
            prev_population = 0
            for j in range(self.num_generations):
                growth_rate = random.uniform(1, 3)
                if random.random() < 0.1:
                    growth_rate *= random.uniform(0.3, 0.7)
                if random.random() < 0.05:
                    growth_rate *= random.uniform(0.1, 0.3)
                if random.random() < 0.01:
                    growth_rate *= random.uniform(0, 0.1)
                if "War" in self.worlds[i][j] or "Epidemic" in self.worlds[i][j]:
                    growth_rate *= random.uniform(0.1, 0.5)
                population = int(population * growth_rate)
                print(f"{j+1}          {self.worlds[i][j]}".ljust(40) + str(population).ljust(20) + f"{growth_rate:.2f}")
                if prev_population > 0:
                    feedback = population - prev_population
                    if feedback > 0:
                        feedback_rate = min(feedback / prev_population, 0.1)
                        population = int(population * (1 + feedback_rate))
                prev_population = population


# =======================================

pw = ParallelWorlds(num_worlds=5, num_generations=6)
pw.generate_worlds()
pw.calculate_population_growth()