import numpy as np

from utility.euclidean_distance import euclidean_distance

def calculate_normalised_fitness_score(individual, interface_template):
    """Calculate Normalised Fitness Score
    Adhering to the original GASS, calculate the distance between an individual and the interface template
    Essentially, it's the standard version of RMSD

    Parameters:
    individual (list[Residue]): The individual that needs to be evaluated
    interface_template (list[Residue]): The interface template, used as a reference

    Returns:
    float: The fitness score of an individual

    """
    n = len(individual)

    # Fitness Score 1: Spatial Distance Score
    individual_coordinates_list = [residue.atom_coordinates for residue in individual]
    individual_distance_list = [euclidean_distance(individual_coordinates_list[i], individual_coordinates_list[j]) for i in range(n-1) for j in range(i+1, n)]

    template_coordinates_list = [residue.atom_coordinates for residue in interface_template]
    template_distance_list = [euclidean_distance(template_coordinates_list[i], template_coordinates_list[j]) for i in range(n-1) for j in range(i+1, n)]

    # use this for other fitness scoring as well
    # becoming typical RMSD
    distance_size = len(individual_distance_list)

    spatial_distance_score = float(np.sqrt(np.sum([(abs(x[0] - x[1]) ** 2) for x in zip(individual_distance_list, template_distance_list)]) / distance_size))

    # Fitness Score 2: Depth Distance Score
    individual_depth_list = [residue.residue_depth for residue in individual]
    individual_depth_distance_list = [abs(individual_depth_list[i] - individual_depth_list[j]) for i in range(n-1) for j in range(i+1, n)]

    template_depth_list = [residue.residue_depth for residue in interface_template]
    template_depth_distance_list = [abs(template_depth_list[i] - template_depth_list[j]) for i in range(n-1) for j in range(i+1, n)]

    depth_distance_score = float(np.sqrt(np.sum([(abs(x[0] - x[1]) ** 2) for x in zip(individual_depth_distance_list, template_depth_distance_list)]) / distance_size))

    # Fitness Score 3 (experiment): SASA score
    individual_sasa_list = [residue.residue_sasa for residue in individual]
    individual_sasa_distance_list = [abs(individual_sasa_list[i] - individual_sasa_list[j]) for i in range(n-1) for j in range(i+1, n)]

    template_sasa_list = [residue.residue_sasa for residue in interface_template]
    template_sasa_distance_list = [abs(template_sasa_list[i] - template_sasa_list[j]) for i in range(n-1) for j in range(i+1, n)]

    sasa_distance_score = float(np.sqrt(np.sum([(abs(x[0] - x[1]) ** 2) for x in zip(individual_sasa_distance_list, template_sasa_distance_list)]) / distance_size))

    # Total Fitness Score
    fitness_score = spatial_distance_score + depth_distance_score + sasa_distance_score
    return fitness_score
