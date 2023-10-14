import random

# Define the list of cities and their coordinates as (x, y) tuples
cities = {
    'A': (12, 10),
    'B': (12, 8),
    'C': (10, 9),
    'D': (12, 11),
    'E': (3, 7),
    'F': (10, 6),
    'G': (12, 9),
}

# Genetic Algorithm Parameters
population_size = 50
generations = 1000
mutation_rate = 0.01

# Function to calculate the total distance of a route
def calculate_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        distance += ((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2) ** 0.5
    return distance

# Initialize the population with random routes
population = [list(cities.keys()) for _ in range(population_size)]

# Main Genetic Algorithm Loop
for generation in range(generations):
    # Calculate fitness (inverse of total distance) for each route
    fitness = [1 / calculate_distance(route) for route in population]

    # Select parents based on fitness (roulette wheel selection)
    parents = random.choices(population, weights=fitness, k=population_size)

    # Create the next generation (crossover)
    next_generation = []
    for _ in range(population_size):
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[crossover_point:]]
        next_generation.append(child)

    # Apply mutation
    for i in range(population_size):
        if random.random() < mutation_rate:
            swap_indices = random.sample(range(len(next_generation[i])), 2)
            next_generation[i][swap_indices[0]], next_generation[i][swap_indices[1]] = (
                next_generation[i][swap_indices[1]],
                next_generation[i][swap_indices[0]],
            )

    population = next_generation

# Find the best route from the final population
best_route = min(population, key=calculate_distance) 
best_distance = calculate_distance(best_route)

# Print the best route and distance
print("Best Route:", best_route)
print("Best Distance:", best_distance)
