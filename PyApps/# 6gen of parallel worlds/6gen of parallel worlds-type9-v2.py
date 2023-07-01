import random

class ParallelWorld:
    def __init__(self, generations, worlds):
        self.generations = generations
        self.worlds = worlds
        self.decisions = {
            1: "Invest in education",
            2: "Focus on agriculture",
            3: "Embrace technology",
            4: "Governance",
            5: "Infrastructure",
            6: "Social equality",
            7: "Healthcare",
            8: "Environmental sustainability"
        }
        self.rates = {
            "Invest in education": random.uniform(0, 1),
            "Focus on agriculture": random.uniform(0, 1),
            "Embrace technology": random.uniform(0, 1),
            "Governance": random.uniform(0, 1),
            "Infrastructure": random.uniform(0, 1),
            "Social equality": random.uniform(0, 1),
            "Healthcare": random.uniform(0, 1),
            "Environmental sustainability": random.uniform(0, 1)
        }
        self.population = []
        self.death_rate = []
        self.birth_rate = []
        self.age = []
    
    def generate_world(self):
        for i in range(self.worlds):
            print(f"Parallel World {i+1}")
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
                    self.rates["Governance"] = random.uniform(0, 1)
                elif j == 2:
                    self.rates["Infrastructure"] = random.uniform(0, 1)
                elif j == 3:
                    self.rates["Social equality"] = random.uniform(0, 1)
                elif j == 4:
                    self.rates["Healthcare"] = random.uniform(0, 1)
                elif j == 5:
                    self.rates["Environmental sustainability"] = random.uniform(0, 1)
                
                decisions = []
                for k in range(1, 9):
                    decision = self.decisions[k]
                    rate = self.rates[decision]
                    if random.uniform(0, 1) < rate:
                        decisions.append(decision)
                self.population.append(population)
                self.death_rate.append(death_rate)
                self.birth_rate.append(birth_rate)
                self.age.append([age] * population)
                
                print(f"Generation {j+1}: {decisions}")
                print(f"Population: {population}, Death Rate: {death_rate:.2f}, Birth Rate: {birth_rate:.2f}, Average Age: {age:.2f}")
            print("\n")
    
    def print_population_info(self):
        print("Population and death and birth number:")
        for i in range(self.generations):
            print(f"Generation {i+1}: Population: {self.population[i]}, Death Rate: {self.death_rate[i]:.2f}, Birth Rate: {self.birth_rate[i]:.2f}")
        print("\n")
        
        print("Population and death and birth percent:")
        for i in range(self.generations):
            death_percent = (self.death_rate[i] * 100) / self.population[i]
            birth_percent = (self.birth_rate[i] * 100) / self.population[i]
            print(f"Generation {i+1}: Death Percent: {death_percent:.2f}%, Birth Percent: {birth_percent:.2f}%")
        print("\n")
    
    def print_decision_info(self):
        print("Decisions for each generation and their rates:")
        for i in range(self.generations):
            print(f"Generation {i+1}:")
            for k in range(1, 9):
                decision = self.decisions[k]
                rate = self.rates[decision]
                print(f"{decision}: {rate:.2f}")
            print("\n")
    
    def print_average_age(self):
        print("Average age of population for each generation:")
        for i in range(self.generations):
            avg_age = sum(self.age[i])/self.population[i]
            print(f"Generation {i+1}: {avg_age:.2f}")
        print("\n")
    
    def simulate_world(self):
        self.generate_world()
        self.print_population_info()
        self.print_decision_info()
        self.print_average_age()

world = ParallelWorld(6, 5)
world.simulate_world()