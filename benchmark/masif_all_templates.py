import numpy as np

from benchmark.evaluate_ppi_population import evaluate_ppi_population
from core.validation import can_run_gass_ppi
from core.gassppi import gass_ppi
from utility.print_interface_info import print_interface_info
from utility.load_pdb import load_pdb

def masif_all_templates(pdb_id_list, templates_dict, masif_path, pdb_parser, lha_dict, verbose=False):
    """MaSIF All Templates
    Given a list of PDB ID available in MaSIF Dataset and precomputed PPI templates,
    execute GASS-PPI on each protein complexes using all other templates

    Parameters:
    pdb_id_list (list[str]): List of PDB ID available in MaSIF Dataset
    templates_dict (dict{pdb_id: list[Residue]}): Dictionary of PPI templates for each PDB ID
    masif_path (str): Absolute path to access the PDB file
    pdb_parser (Bio.PDB.PDBParser.PDBParser): Bio.PDB Parser
    lha_dict (dict{residue_name: atom_name}): Corresponding Last Heavy Atom for each amino acids
    verbose (bool): True for additional logs, False otherwise

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

    # For each monomeric PDB ID, evaluate using all templates
    for monomer_pdb_id in pdb_id_list:
        # Step 1: Load the monomeric protein structure and PPI template
        monomer_pdb_structure = load_pdb(monomer_pdb_id, masif_path, pdb_parser, lha_dict, "lha")
        aggregated_population_list = []

        if verbose:
            print("Currently evaluating:", monomer_pdb_id)

        # Step 2: GASS-PPI with all templates except its own
        for template_pdb_id, interface_template in templates_dict.items():
            if (monomer_pdb_id != template_pdb_id):
                if (can_run_gass_ppi(monomer_pdb_structure, interface_template) and len(interface_template) > 1):
                    template_size = len(interface_template)
                    # if verbose:
                    #     print("use template of ", template_pdb_id, "with template size:", template_size)
                    #     print_interface_info(interface_template)
                    current_population_list = gass_ppi(monomer_pdb_structure, interface_template, verbose=False)
                    # normalised_population_list = [(individual[0], individual[1] / template_size) for individual in current_population_list]
                    # aggregated_population_list += normalised_population_list
                    aggregated_population_list += current_population_list

        aggregated_population_list.sort(key = lambda x: x[1])
        # aggregated_population_list = aggregated_population_list[:ranking_size]
        if verbose:
            for i in range(5):
                print("Ranking", i+1, "with fitness score =", aggregated_population_list[i][1])
                print_interface_info(aggregated_population_list[i][0])

        # Step 3: Evaluation
        actual_interface = templates_dict[monomer_pdb_id]
        individual_ranking, precision, recall, auc_roc, auc_pr, mcc, specificity, npv = evaluate_ppi_population(actual_interface, aggregated_population_list, monomer_pdb_structure, len(aggregated_population_list))
        individual_ranking_list.append(individual_ranking)
        precision_list.append(precision)
        recall_list.append(recall)
        auc_roc_list.append(auc_roc)
        auc_pr_list.append(auc_pr)
        mcc_list.append(mcc)
        specificity_list.append(specificity)
        npv_list.append(npv)

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
