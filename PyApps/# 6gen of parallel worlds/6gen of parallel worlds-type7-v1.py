import random

class ParallelWorlds:
    def __init__(self, num_of_worlds=5, num_of_generations=6):
        self.num_of_worlds = num_of_worlds
        self.num_of_generations = num_of_generations
        self.decisions = ["Invest in education", "Focus on agriculture", "Embrace technology"]
        self.worlds = []
        self.population_growth_rates = []
        self.death_rates = []
        self.birth_rates = []
        
    def generate_worlds(self):
        for i in range(self.num_of_worlds):
            world = []
            for j in range(self.num_of_generations):
                generation = {}
                generation["Decisions"] = {}
                for decision in self.decisions:
                    generation["Decisions"][decision] = round(random.uniform(0, 1), 2)
                if j == 1:
                    generation["Decisions"]["Governance"] = round(random.uniform(0, 1), 2)
                elif j == 2:
                    generation["Decisions"]["Infrastructure"] = round(random.uniform(0, 1), 2)
                elif j == 3:
                    generation["Decisions"]["Social equality"] = round(random.uniform(0, 1), 2)
                elif j == 4:
                    generation["Decisions"]["Healthcare"] = round(random.uniform(0, 1), 2)
                elif j == 5:
                    generation["Decisions"]["Environmental sustainability"] = round(random.uniform(0, 1), 2)
                generation["War or Epidemic"] = random.choice([True, False])
                world.append(generation)
            self.worlds.append(world)
    
    def calculate_population_growth_rates(self):
        for i in range(self.num_of_worlds):
            world_population = []
            world_death_rates = []
            world_birth_rates = []
            for j in range(self.num_of_generations):
                generation_population = round(random.uniform(1000, 10000))
                if j > 0:
                    previous_population = world_population[j-1]
                    if previous_population != 0:
                        death_rate = round(random.uniform(0.01, 0.05), 2)
                        birth_rate = round(random.uniform(0.05, 0.15), 2)
                        deaths = int(previous_population * death_rate)
                        births = int(previous_population * birth_rate)
                        generation_population = previous_population + births - deaths
                        world_death_rates.append(death_rate)
                        world_birth_rates.append(birth_rate)
                    else:
                        world_death_rates.append(0)
                        world_birth_rates.append(0)
                else:
                    world_death_rates.append(0)
                    world_birth_rates.append(0)
                world_population.append(generation_population)
            self.population_growth_rates.append(world_population)
            self.death_rates.append(world_death_rates)
            self.birth_rates.append(world_birth_rates)
    
    def display_results(self):
        for i in range(self.num_of_worlds):
            print(f"World {i+1}")
            print("Generation\tDecisions\t\t\t\t\t\tWar or Epidemic")
            for j in range(self.num_of_generations):
                decisions = self.worlds[i][j]["Decisions"]
                decisions_text = "\t\t\t\t".join([f"{k}: {v}" for k, v in decisions.items()])
                war_or_epidemic = "Yes" if self.worlds[i][j]["War or Epidemic"] else "No"
                print(f"{j+1}\t\t{decisions_text}\t\t{war_or_epidemic}")
            print("\nPopulation Growth Rates")
            print("Generation\tPopulation\t\tBirth Rate\t\tDeath Rate")
            for j in range(self.num_of_generations):
                population = self.population_growth_rates[i][j]
                birth_rate = self.birth_rates[i][j]
                death_rate = self.death_rates[i][j]
                print(f"{j+1}\t\t{population}\t\t{birth_rate}\t\t\t{death_rate}")
            print("\n")
            
            
# ====================================

pw = ParallelWorlds()
pw.generate_worlds()
pw.calculate_population_growth_rates()
pw.display_results()