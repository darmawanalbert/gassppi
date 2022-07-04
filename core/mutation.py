import random

from utility.is_residue_in_interface import is_residue_in_interface
from utility.random_sampling import weighted_sample_without_replacement

def mutation(repository_dict, propensity_dict, individual, mutation_probability):
    """Mutation
    Given an individual, perform a single point mutations based on mutation probability.
    In this case, no conservative mutation is employed

    Parameters:
    repository_dict (dict{amino_acid_type: list[Residue]}): The input protein structure per amino acid type
    propensity_dict (dict{amino_acid_type: list[float]}): List of interface propensity per amino acid type
    individual (list[Residue]): Individual to be mutated
    mutation_probability (float): The probability that a mutation occurs (between 0 and 1.0)

    Returns:
    list[Residue]: Mutated individuals

    """
    rng = random.Random(10)

    # Only apply mutation if a random value is within the mutation probability
    # Otherwise, simply return the individual without performing any operation
    random_percentage = random.random()
    if random_percentage < mutation_probability:
        # Randomly determine the mutation point
        individual_size = len(individual)
        mutation_point = random.randrange(individual_size)
        mutated_residue = individual[mutation_point]

        mutation_repository_list = []
        mutation_propensity_list = []
        for i in range(len(repository_dict[mutated_residue.residue_name])):
            cur_residue = repository_dict[mutated_residue.residue_name][i]
            cur_propensity = propensity_dict[mutated_residue.residue_name][i]
            if (is_residue_in_interface(cur_residue, individual) == False):
                mutation_repository_list.append(cur_residue)
                mutation_propensity_list.append(cur_propensity)

        # Mutate the residue at the mutation point into the same amino acid types
        if len(mutation_repository_list) > 0:
            new_residue = weighted_sample_without_replacement(
                mutation_repository_list,
                mutation_propensity_list,
                1,
                rng
            )
            individual[mutation_point] = new_residue[0]

    return individual
