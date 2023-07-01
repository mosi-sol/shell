import random

class ParallelWorld:
    
    def __init__(self, generations, worlds):
        self.generations = generations
        self.worlds = worlds
        self.decisions = {1: "Education", 2: "Transportation", 3: "Agriculture", 4: "Energy", 5: "Water", 6: "Waste", 7: "Housing", 8: "Employment"}
        self.rates = {decision: 0.5 for decision in self.decisions.values()}
        self.population = []
        self.death_rate = []
        self.birth_rate = []
        self.age = []
        
    def generate_world(self):
        for i in range(self.worlds):
            print(f"Parallel World {i+1}")
            print("Table 1: Population and death/birth numbers and percentages")
            print("Generation\tPopulation\tBirths\tDeaths\tBirth Rate\tDeath Rate\tBirth %\tDeath %")
            for j in range(self.generations):
                if j == 0:
                    population = random.randint(1000, 10000)
                    death_rate = random.uniform(0, 0.05)
                    birth_rate = random.uniform(0, 0.1)
                    age = random.uniform(0, 100)
                else:
                    death_rate = random.uniform(0, 0.1)
                    birth_rate = random.uniform(0, 0.15)
                    population = int(self.population[-1] + (self.population[-1] * (birth_rate - death_rate)))
                    age = sum(self.age[-1])/len(self.age[-1]) + random.uniform(-2, 2)
                
                if j == 1:
                    self.rates["Governance"] = random.uniform(0.4, 0.6)
                elif j == 2:
                    self.rates["Infrastructure"] = random.uniform(0.4, 0.6)
                elif j == 3:
                    self.rates["Social equality"] = random.uniform(0.3, 0.5)
                elif j == 4:
                    self.rates["Healthcare"] = random.uniform(0.5, 0.7)
                elif j == 5:
                    self.rates["Environmental sustainability"] = random.uniform(0.6, 0.8)
                
                decisions = []
                for k in range(1, 9):
                    decision_rate = random.uniform(0, 1)
                    if decision_rate > self.rates[self.decisions[k]]:
                        decisions.append(self.decisions[k])
                self.population.append(population)
                self.death_rate.append(death_rate)
                self.birth_rate.append(birth_rate)
                self.age.append([age] * population)
                
                birth_num = int(population * birth_rate)
                death_num = int(population * death_rate)
                birth_percent = birth_rate * 100
                death_percent = death_rate * 100
                print(f"{j+1}\t\t{population}\t\t{birth_num}\t{death_num}\t{birth_rate:.2f}\t\t{death_rate:.2f}\t\t{birth_percent:.2f}\t\t{death_percent:.2f}")
                
                if j == self.generations - 1:
                    print("\nTable 3: Average age of population")
                    print(f"Generation\tAverage Age")
                    for g in range(j + 1):
                        print(f"{g+1}\t\t{sum(self.age[g])/len(self.age[g]):.2f}")
                
                if j == 0:
                    print(f"\nTable 2: Decisions and Rates for Generation {j+1}")
                    print("Decision\t\tRate")
                    for decision, rate in self.rates.items():
                        print(f"{decision}\t{rate:.2f}")
                elif j == self.generations - 1:
                    print(f"\nTable 2: Decisions and Rates for Generation {j+1}")
                    print("Decision\t\tRate")
                    for decision, rate in self.rates.items():
                        print(f"{decision}\t\t{rate:.2f}")
                
                decisions_str = ", ".join(decisions) if decisions else "None"
                print(f"Decisions:\t{decisions_str}")
                print(f"Population:\t{population}\tDeath Rate:\t{death_rate:.2f}\tBirth Rate:\t{birth_rate:.2f}\tAverage Age:\t{age:.2f}")
            
            print("\n")
        
# ======================================

ParallelWorld(6, 3).generate_world()

# pw = ParallelWorld(generations=6, worlds=3)
# pw.generate_world()

# pw.print_population_info()
# pw.print_decision_info()
# pw.print_average_age()