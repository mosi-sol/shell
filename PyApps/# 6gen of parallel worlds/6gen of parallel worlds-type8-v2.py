import random

class ParallelWorlds:
    def __init__(self):
        self.worlds = []
        self.decisions = ["invest in education", "focus on agriculture", "embrace technology"]
        self.generation_stats = []
        self.generation_stats.append(["Generation", "Decision", "Birth Rate", "Death Rate", "Population Growth Rate"])
    
    def generate_worlds(self, num_worlds):
        for i in range(num_worlds):
            self.worlds.append(self.generate_world())
    
    def generate_world(self):
        world = []
        for i in range(6):
            generation = []
            if i == 1:
                generation.append("Governance")
            elif i == 2:
                generation.append("Infrastructure")
            elif i == 3:
                generation.append("Social Equality")
            elif i == 4:
                generation.append("Healthcare")
            elif i == 5:
                generation.append("Environmental Sustainability")
            else:
                generation.append("None")
            for j in range(3):
                generation.append(random.uniform(0.01, 0.1))
            world.append(generation)
        return world
    
    def run_simulation(self):
        for i in range(len(self.worlds)):
            self.generation_stats.append(["World " + str(i+1), "", "", "", ""])
            self.run_world_simulation(self.worlds[i], i+1)
            
    def run_world_simulation(self, world, world_num):
        for i in range(len(world)):
            generation = world[i]
            decision = random.choice(self.decisions)
            generation.append(decision)
            birth_rate = generation[1] * (1 - generation[2])
            death_rate = generation[1] * generation[2]
            population_growth_rate = round((birth_rate - death_rate) * random.uniform(0.9, 1.1), 2)
            generation.append(round(birth_rate, 2))
            generation.append(round(death_rate, 2))
            generation.append(population_growth_rate)
            self.generation_stats.append(["", "Generation " + str(i+1), generation[1], generation[2], population_growth_rate])
            world[i] = generation
            
        for i in range(len(world)):
            if i == 0:
                world[i][1] += world[i][5] # feedback loop
            else:
                world[i][1] += world[i-1][5] # feedback loop
        
        print(f"\nWorld {world_num} Results:\n")
        self.plot_results(world, world_num)
    
    def plot_results(self, world, world_num):
        print("Decision\tBirth Rate\tDeath Rate\tPopulation Growth Rate")
        for i in range(len(world)):
            generation = world[i]
            print(f"{generation[3]}\t\t{generation[1]}\t\t{generation[2]}\t\t{generation[5]}")
        
        print("\n")
        print("-"*70)
        print("\n")
    
    def print_generation_stats(self):
        for i in range(len(self.worlds)):
            print(f"\nWorld {i+1} Results:\n")
            world_stats = self.generation_stats[i*7:(i+1)*7]
            print("{:<18} {:<18} {:<18} {:<18} {:<18}".format(*world_stats[0]))
            for row in world_stats[1:]:
                print("{:<18} {:<18} {:<18} {:<18} {:<18}".format("", *row))
            
# ==================================
pw = ParallelWorlds()
pw.generate_worlds(5)
pw.run_simulation()
pw.print_generation_stats()
