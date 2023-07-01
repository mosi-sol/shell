import random

class ParallelWorld:
    def __init__(self, num_generations, num_parallel_worlds):
        self.num_generations = num_generations
        self.num_parallel_worlds = num_parallel_worlds
        self.decisions = {
            1: ["invest in education", "focus on agriculture", "embrace technology"],
            2: ["invest in education", "focus on agriculture", "embrace technology", "good governance"],
            3: ["invest in education", "focus on agriculture", "embrace technology", "good governance", "infrastructure"],
            4: ["invest in education", "focus on agriculture", "embrace technology", "good governance", "infrastructure", "social equality"],
            5: ["invest in education", "focus on agriculture", "embrace technology", "good governance", "infrastructure", "social equality", "healthcare"],
            6: ["invest in education", "focus on agriculture", "embrace technology", "good governance", "infrastructure", "social equality", "healthcare", "environmental sustainability"]
        }
        self.decision_rates = {i: [random.randint(1, 10) for _ in range(len(self.decisions[i]))] for i in range(1, 7)}
        self.population = [[random.randint(100, 1000) for _ in range(num_parallel_worlds)] for _ in range(num_generations)]
        self.deaths = [[random.randint(0, int(0.1 * self.population[i][j])) for j in range(num_parallel_worlds)] for i in range(num_generations)]
        self.births = [[random.randint(0, int(0.2 * self.population[i][j])) for j in range(num_parallel_worlds)] for i in range(num_generations)]
        self.war_or_epidemic = [random.choice([True, False]) for _ in range(num_parallel_worlds)]
        self.avg_age = [[random.randint(18, 80) for _ in range(num_parallel_worlds)] for _ in range(num_generations)]
    
    def simulate(self):
        for i in range(1, self.num_generations):
            for j in range(self.num_parallel_worlds):
                if self.war_or_epidemic[j]:
                    self.population[i][j] = int(self.population[i-1][j] * 0.9)
                else:
                    self.population[i][j] = self.population[i-1][j] - self.deaths[i-1][j] + self.births[i-1][j]
                self.avg_age[i][j] = int((self.avg_age[i-1][j] * self.population[i-1][j] + 10 * self.births[i-1][j]) / self.population[i][j])
    
    def print_population_stats(self):
        print("Table 1: Population Statistics")
        print(f"{'Generation':<12}{'Population':<12}{'Deaths':<12}{'Births':<12}{'Death %':<12}{'Birth %':<12}")
        for i in range(self.num_generations):
            total_population = sum(self.population[i])
            total_deaths = sum(self.deaths[i])
            total_births = sum(self.births[i])
            death_percent = round(total_deaths / total_population * 100, 2)
            birth_percent = round(total_births / total_population * 100, 2)
            print(f"{i+1:<12}{total_population:<12}{total_deaths:<12}{total_births:<12}{death_percent:<12}{birth_percent:<12}")
    
    def print_decision_rates(self):
        print("\nTable 2: Decision Rates")
        for i in range(1, 7):
            print(f"Generation {i}:")
            for j in range(len(self.decisions[i])):
                print(f"{self.decisions[i][j]:<25}{self.decision_rates[i][j]:>2}")
            print("=============")
    
    def print_avg_age(self):
        print("\nTable 3: Average Age of Population")
        for i in range(self.num_generations):
            total_avg_age = sum(self.avg_age[i])
            avg_age = round(total_avg_age / self.num_parallel_worlds, 2)
            print(f"Generation {i+1}: {avg_age} years")
            print("=============")

# Example usage:
world = ParallelWorld(num_generations=6, num_parallel_worlds=5)
world.simulate()
world.print_population_stats()
world.print_decision_rates()
world.print_avg_age()