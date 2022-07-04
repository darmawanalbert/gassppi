import random

from constant.amino_acid import amino_acid_list
from utility.random_sampling import weighted_sample_without_replacement

def generate_initial_population(repository_dict, propensity_dict, interface_template, population_size):
    """Generate Initial Population
    Given the input protein structure and its interface template, generate list
    of random individuals which constitutes the initial population.

    Each residue inside the individual needs to have the same residue_name compared to
    the interface_template, but can have different residue_sequence_position or chain_name.

    Parameters:
    repository_dict (dict{amino_acid_type: list[Residue]}): The input protein structure per amino acid type
    propensity_dict (dict{amino_acid_type: list[float]}): List of interface propensity per amino acid type
    interface_template (list[Residue]): List of Residue object which constitutes the interface template
    population_size (int): The number of random individuals to be generated

    Returns:
    list[list[Residue]]: The initial population (list of individuals)

    """
    rng = random.Random(10)

    # Map the index position of each interface residues onto a dictionary
    # (based on amino_acid_list)
    interface_residue_idx_dict = { x: [] for x in amino_acid_list }
    for i in range(len(interface_template)):
        cur_residue = interface_template[i]
        interface_residue_idx_dict[cur_residue.residue_name].append(i)

    initial_population_list = []
    # Generate the initial population
    for _ in range(population_size):
        # Generate a random individual
        random_individual_list = [None for _ in range(len(interface_template))]
        for residue_type, index_list in interface_residue_idx_dict.items():
            if (len(index_list) > 0):
                # Sampling per amino acid type (e.g. list of CYS)
                residue_sample_list = list(weighted_sample_without_replacement(
                    repository_dict[residue_type],
                    propensity_dict[residue_type],
                    len(interface_residue_idx_dict[residue_type]),
                    rng
                ))
                # Add the random sampling result to the random individual
                # adhering to the index from interface_residue_idx_dict
                for i in range(len(index_list)):
                    random_individual_list[index_list[i]] = residue_sample_list[i]

        # Add the individual to the initial population
        initial_population_list.append(random_individual_list)

    return initial_population_list
