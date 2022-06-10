import numpy as np

from benchmark.evaluate_ppi_population import evaluate_ppi_population
from core.validation import can_run_gass_ppi
from core.gassppi import gass_ppi
from utility.load_pdb import load_pdb

def dbd_sanity_test(pdb_id_list, templates_dict, dbd_path, pdb_parser, lha_dict, ranking_size=100, verbose=False, iteration_per_protein=1, population_size=300, number_of_generations=300, crossover_probability=0.5, mutation_probability=0.7, tournament_size=3, number_of_tournament=50):
    """DBD Sanity Test
    Given a list of PDB ID available in Docking Benchmark Dataset and precomputed PPI templates,
    execute GASS-PPI on each protein complexes using its own template

    Parameters:
    pdb_id_list (list[str]): List of PDB ID available in Docking Benchmark 5
    templates_dict (dict{pdb_id: list[Residue]}): Dictionary of PPI templates for each PDB ID
    dbd_path (str): Absolute path to access the PDB file
    pdb_parser (Bio.PDB.PDBParser.PDBParser): Bio.PDB Parser
    lha_dict (dict{residue_name: atom_name}): Corresponding Last Heavy Atom for each amino acids
    ranking_size (int): Number of individuals to be evaluated (from individual #0 to #ranking_size-1)
    verbose (bool): True for additional logs, False otherwise
    iteration_per_protein (int): Number of iteration performed for each protein (1 by default, 30 for statistical confidence)
    population_size (int): Total number of individuals inside the population
    number_of_generations (int): Number of iterations run in the genetic algorithm
    crossover_probability (float): Probability value between 0-1 which governs the likelihood that crossover is performed
    mutation_probability (float): Probability value between 0-1 which governs the likelihood that mutation is performed
    tournament_size (int): The number of individuals inside a particular tournament
    number_of_tournament (int): Number of tournaments to be performed

    Returns:

    """
    # Initialise returned list
    individual_ranking_list = []
    precision_list = []
    recall_list = []
    auc_roc_list = []
    auc_pr_list = []
    mcc_list = []
    specificity_list = []
    npv_list = []

    # For each PDB ID, evaluate both its corresponding ligand and receptor
    for pdb_id in pdb_id_list:
        for monomer_pdb_id in [pdb_id + "_l_u", pdb_id + "_r_u"]:
            # Step 1: Load the monomeric protein structure and PPI template
            monomer_pdb_structure = load_pdb(monomer_pdb_id, dbd_path, pdb_parser, lha_dict, "lha")
            interface_template = templates_dict[monomer_pdb_id]

            for _ in range(iteration_per_protein):
                # Step 2: GASS-PPI
                if can_run_gass_ppi(monomer_pdb_structure, interface_template):
                    # if verbose:
                    #     print("Currently evaluating:", monomer_pdb_id, ", with template size:", len(interface_template))

                    predicted_population_list = gass_ppi(monomer_pdb_structure, interface_template, population_size=population_size, number_of_generations=number_of_generations, crossover_probability=crossover_probability, mutation_probability=mutation_probability, tournament_size=tournament_size, number_of_tournament=number_of_tournament, verbose=False)

                    # Step 3: Evaluation
                    individual_ranking, precision, recall, auc_roc, auc_pr, mcc, specificity, npv = evaluate_ppi_population(interface_template, predicted_population_list, monomer_pdb_structure, ranking_size)
                    # TODO: Remove this later, for debugging only
                    # if verbose:
                    #     print_interface_info(predicted_population_list[individual_ranking][0])

                    individual_ranking_list.append(individual_ranking)
                    precision_list.append(precision)
                    recall_list.append(recall)
                    auc_roc_list.append(auc_roc)
                    auc_pr_list.append(auc_pr)
                    mcc_list.append(mcc)
                    specificity_list.append(specificity)
                    npv_list.append(npv)
                else:
                    print("Cannot run GASS-PPI on ", monomer_pdb_id)
                    precision_list.append(0)
                    recall_list.append(0)
                    auc_roc_list.append(0)
                    auc_pr_list.append(0)
                    mcc_list.append(0)
                    specificity_list.append(0)
                    npv_list.append(0)

    # Additional logs for development purposes
    if verbose:
        print("Individual Ranking List")
        print(individual_ranking_list)
        print("Mean Precision: ", np.mean(precision_list))
        print("Mean Recall: ", np.mean(recall_list))
        print("Mean AUC-ROC Score: ", np.mean(auc_roc_list))
        print("Mean AUC-PR Score: ", np.mean(auc_pr_list))
        print("Mean MCC: ", np.mean(mcc_list))
        print("Mean Specificity: ", np.mean(specificity_list))
        print("Mean NPV: ", np.mean(npv_list))
