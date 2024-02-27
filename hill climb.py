import random

def generate_random_solution(problem_size):
    return [random.randint(0, 1) for _ in range(problem_size)]

def evaluate_solution(solution):
    return sum(solution)

def hill_climbing(problem_size, max_iterations):
    current_solution = generate_random_solution(problem_size)
    current_value = evaluate_solution(current_solution)
    
    for _ in range(max_iterations):
        neighbor = current_solution[:]
        index = random.randint(0, problem_size - 1)
        neighbor[index] = 1 - neighbor[index]  # Flipping the bit
        
        neighbor_value = evaluate_solution(neighbor)
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
    
    return current_solution, current_value

if __name__ == "__main__":
    problem_size = 10
    max_iterations = 1000
    best_solution, best_value = hill_climbing(problem_size, max_iterations)
    print("Best Solution:", best_solution)
    print("Best Value:", best_value)
