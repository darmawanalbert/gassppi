from core.initial_population import generate_initial_population
from core.fitness import calculate_normalised_fitness_score
from core.selection import deterministic_tournament_selection
from core.mutation import mutation
from core.crossover import crossover
from utility.save_current_generation import save_current_generation

def gass_ppi(input_protein_structure, interface_template, population_size=300, number_of_generations=300, crossover_probability=0.5, mutation_probability=0.7, tournament_size=3, number_of_tournament=50, verbose=False):
    """GASS-PPI Method
    Given the input protein structure and the interface template, perform genetic algorithms
    to search the most likely interface

    Parameters:
    input_protein_structure (list[Residue]): List of Residue which constitutes the entire protein structure
    interface_template (list[Residue]): List of Residue which is used as a template for the genetic algorithms
    population_size (int): Total number of individuals inside the population
    number_of_generations (int): Number of iterations run in the genetic algorithm
    crossover_probability (float): Probability value between 0-1 which governs the likelihood that crossover is performed
    mutation_probability (float): Probability value between 0-1 which governs the likelihood that mutation is performed
    tournament_size (int): The number of individuals inside a particular tournament
    number_of_tournament (int): Number of tournaments to be performed
    verbose (bool): Draw plot and additional statistics (for analysis only). Default is False.

    Returns:
    list[(list[Residue], float)]: The final population generated from the genetic algorithms.
                                  Each tuple consists of the individual and its correspondings fitness score

    """
    eps = 0.000001
    protein_structure = [residue for residue in input_protein_structure]

    # Initial Population
    population_list_no_fitness = generate_initial_population(protein_structure, interface_template, population_size)
    population_list = [(individual, calculate_normalised_fitness_score(individual, interface_template)) for individual in population_list_no_fitness]

    # Development Logs
    if verbose:
        save_current_generation("generation_0", population_list)

    # Evolutionary Steps
    for i in range(number_of_generations):
        # Selection
        parent_list = deterministic_tournament_selection(population_list, tournament_size, number_of_tournament)

        for j in range(0, len(parent_list), 2):
            # Crossover
            new_individual_1, new_individual_2 = crossover(list(population_list[j][0]), list(population_list[j+1][0]), crossover_probability)

            # Mutation
            mutated_new_individual_1 = mutation(protein_structure, list(new_individual_1), mutation_probability)
            mutated_new_individual_2 = mutation(protein_structure, list(new_individual_2), mutation_probability)

            # Fitness Evaluation
            fitness_score_1 = calculate_normalised_fitness_score(mutated_new_individual_1, interface_template)
            fitness_score_2 = calculate_normalised_fitness_score(mutated_new_individual_2, interface_template)

            # Add 2 new individuals into the population_list
            population_list.append((mutated_new_individual_1, fitness_score_1))
            population_list.append((mutated_new_individual_2, fitness_score_2))

        # Population Management (steady-state)
        population_list.sort(key = lambda x: x[1])
        population_list = population_list[:population_size]

        if verbose:
            save_current_generation("generation_" + str(i+1), population_list)
        # If the fitness score already 0, stop the evolutionary steps as it already converges towards the most optimal solution
        if population_list[0][1] <= eps:
            break

    return population_list
