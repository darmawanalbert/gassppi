import numpy as np

from benchmark.dbd_sanity_test import dbd_sanity_test

def run_grid_search(pdb_id_list, templates_dict):
    """Run Grid Search

    Parameters:
    pdb_id_list (list[str]): List of PDB ID available in Docking Benchmark 5
    templates_dict (dict{pdb_id: list[Residue]}): Dictionary of PPI templates for each PDB ID

    Returns:
    None

    """
    population_size_list = [300, 500]
    number_of_generations_list = [200, 300, 500]
    crossover_probability_list = [0.5, 0.7, 0.9]
    mutation_probability_list = [0.3, 0.7, 0.9]
    tournament_size_list = [2, 3]
    number_of_tournament_list = [50, 100]

    # Keep track of the current optimal value
    optimal_population_size = population_size_list[0]
    optimal_number_of_generations = number_of_generations_list[0]
    optimal_crossover_probability = crossover_probability_list[0]
    optimal_mutation_probability = mutation_probability_list[0]
    optimal_tournament_size = tournament_size_list[0]
    optimal_number_of_tournament = number_of_tournament_list[0]

    optimal_precision = 0.0
    optimal_recall = 0.0
    optimal_auc_roc = 0.0
    optimal_auc_pr = 0.0
    optimal_mcc = 0.0
    optimal_specificity = 0.0
    optimal_npv = 0.0

    for population_size in population_size_list:
        for number_of_generations in number_of_generations_list:
            for crossover_probability in crossover_probability_list:
                for mutation_probability in mutation_probability_list:
                    for tournament_size in tournament_size_list:
                        for number_of_tournament in number_of_tournament_list:
                            print("Running sanity test with population_size:", population_size, ", number_of_generations:", number_of_generations, ", crossover_probability:", crossover_probability, ", mutation_probability:", mutation_probability, ", tournament_size:", tournament_size, ", number_of_tournament:", number_of_tournament)
                            _, precision_list, recall_list, auc_roc_list, auc_pr_list, mcc_list, specificity_list, npv_list = dbd_sanity_test(pdb_id_list, templates_dict, ranking_size=100, verbose=False, iteration_per_protein=1, population_size=population_size, number_of_generations=number_of_generations, crossover_probability=crossover_probability, mutation_probability=mutation_probability, tournament_size=tournament_size, number_of_tournament=number_of_tournament)
                            avg_auc_roc = np.mean(auc_roc_list)
                            print("Mean AUC-ROC:", avg_auc_roc)
                            if avg_auc_roc > optimal_auc_roc:
                                optimal_population_size = population_size
                                optimal_number_of_generations = number_of_generations
                                optimal_crossover_probability = crossover_probability
                                optimal_mutation_probability = mutation_probability
                                optimal_tournament_size = tournament_size
                                optimal_number_of_tournament = number_of_tournament

                                optimal_precision = np.mean(precision_list)
                                optimal_recall = np.mean(recall_list)
                                optimal_auc_roc = avg_auc_roc
                                optimal_auc_pr = np.mean(auc_pr_list)
                                optimal_mcc = np.mean(mcc_list)
                                optimal_specificity = np.mean(specificity_list)
                                optimal_npv = np.mean(npv_list)
    print("")
    print("Optimal GA Parameters")
    print("Population Size:", optimal_population_size)
    print("Number of Generations:", optimal_number_of_generations)
    print("Crossover Probability:", optimal_crossover_probability)
    print("Mutation Probability:", optimal_mutation_probability)
    print("Tournament Size:", optimal_tournament_size)
    print("Number of Tournament:", optimal_number_of_tournament)

    print("which produced below metrics:")
    print("Mean precision:", optimal_precision)
    print("Mean recall:", optimal_recall)
    print("Mean AUC-ROC:", optimal_auc_roc)
    print("Mean AUC-PR:", optimal_auc_pr)
    print("Mean MCC:", optimal_mcc)
    print("Mean Specificity:", optimal_specificity)
    print("Mean NPV:", optimal_npv)
