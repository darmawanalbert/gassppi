import random

def tournament_selection(population_list, tournament_size, number_of_tournament):
    """Tournament Selection
    Perform tournament selection towards current population list
    to select parents (for generating new generations)

    Parameters:
    population_list (list[(list[Residue], float)]): Current list of population
    tournament_size (int): Hyperparameter to determine how many random individuals in each tournament
    number_of_tournament (int): Hyperparameter to determine how many tournaments to be performed

    Returns:
    list[(list[Residue], float)]: List of parents

    """
    # Probability to choose the fittest individual in a tournament pool
    # Otherwise, choose the least fit individual in the same tournament pool
    # fittest_probability = 1.0, deterministic tournament selection
    # fittest_probability < 1.0, stochastic tournament selection
    fittest_probability = 0.8

    random.shuffle(population_list)

    parent_list = []
    # Perform n tournaments (where n is the number_of_tournament)
    for _ in range(number_of_tournament):
        # Choose random individuals to participate in the tournament
        tournament_participant_list = []
        for _ in range(tournament_size):
            random_idx = random.randrange(len(population_list))
            tournament_participant_list.append(population_list[random_idx])

        # Choose the tournament_winner from the tournament_participant_list
        # based on fittest_probability
        random_percentage = random.random()
        tournament_winner = tournament_participant_list[0]
        if random_percentage < fittest_probability:
            # Choose the fittest individual as the tournament winner
            for i in range(1, len(tournament_participant_list)):
                if tournament_participant_list[i][1] < tournament_winner[1]:
                    tournament_winner = tournament_participant_list[i]
        else:
            # Choose the least fit individual as the tournament winner
            for i in range(1, len(tournament_participant_list)):
                if tournament_participant_list[i][1] > tournament_winner[1]:
                    tournament_winner = tournament_participant_list[i]

        # Add the tournament_winner to the parent_list
        parent_list.append(tournament_winner)

    return parent_list
