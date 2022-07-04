import random

def crossover(individual_1, individual_2, crossover_probability):
    """Crossover
    Given two individuals, perform a two point crossover based on crossover probability

    Parameters:
    individual_1 (list[Residue]): First parent
    individual_2 (list[Residue]): Second parent
    crossover_probability (float): The probability that a crossover occurs (between 0 and 1.0)

    Returns:
    list[Residue]: Individual 1 after crossover
    list[Residue]: Individual 2 after crossover

    """
    # Only apply crossover if a random value is within the crossover probability
    # Otherwise, simply return these individuals without performing any operation
    random_percentage = random.random()
    if random_percentage < crossover_probability:
        # Randomly determine the starting and ending crossover point
        n = len(individual_1)
        start_point = random.randrange(n-1)
        end_point = random.randrange(start_point+1, n)

        # Swap residues between two individuals, starting from the crossover point
        for i in range(start_point, end_point+1):
            individual_1[i], individual_2[i] = individual_2[i], individual_1[i]

    return (individual_1, individual_2)
