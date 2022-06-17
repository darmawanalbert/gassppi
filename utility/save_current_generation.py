from constant.directory_constant import repository_path

def save_current_generation(file_name, current_population_list):
    """Save Current Generation
    Given the current population list, generate .log file for development purposes

    Parameters:
    file_name (str): Log file name (without the extension)
    current_population_list (list[(list[Residue], float)]): Current list of individuals to be logged

    Returns:
    None

    """
    target_path = repository_path + "/development-logs/" + file_name + ".log"
    buffer = ""
    ranking = 1
    for individual, fitness_score in current_population_list:
        # Convert the individual into a string
        stringified_individual = ""
        for i in range(len(individual)):
            if i > 0:
                stringified_individual += " - "
            stringified_individual += individual[i].residue_name
            stringified_individual += " "
            stringified_individual += str(individual[i].residue_sequence_position)
            stringified_individual += " "
            stringified_individual += individual[i].chain_name

        # Add all information onto the buffer
        buffer += str(ranking)
        buffer += " | "
        buffer += stringified_individual
        buffer += " | "
        buffer += str(fitness_score)
        buffer += "\n"
        ranking += 1

    # Write the buffer into a file
    with open(target_path, "w") as fp:
        fp.write(buffer)
