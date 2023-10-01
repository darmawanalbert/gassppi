from Bio.PDB import *

from utility.load_ppi_templates import load_ppi_templates
from utility.execute_with_elapsed_time import execute_with_elapsed_time
from constant.directory_constant import dbd5_path, templates_path
from constant.last_heavy_atom import lha_dict
from constant.dbd3_dataset import dbd3_all_list
from constant.dbd5_dataset import dbd5_all_list
from benchmark.dbd_sanity_check import dbd_sanity_check

pdb_parser = PDBParser()

# Docking Benchmark 5: Load PPI Templates (5A)
# Load DBD5 PPI template dictionary from .json files (to be used in the main program)
dbd5_a_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_a_templates_5a.json")
dbd5_ei_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_ei_templates_5a.json")
dbd5_er_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_er_templates_5a.json")
dbd5_es_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_es_templates_5a.json")
dbd5_ab_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_ab_templates_5a.json")
dbd5_og_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_og_templates_5a.json")
dbd5_ox_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_ox_templates_5a.json")
dbd5_or_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_or_templates_5a.json")

dbd5_all_templates_5a_dict = {**dbd5_a_templates_5a_dict, **dbd5_ei_templates_5a_dict, **dbd5_er_templates_5a_dict,
                      **dbd5_es_templates_5a_dict, **dbd5_ab_templates_5a_dict, **dbd5_og_templates_5a_dict,
                      **dbd5_ox_templates_5a_dict, **dbd5_or_templates_5a_dict}

# Docking Benchmark 3: Load PPI Templates (5A)
# Load DBD3 PPI template dictionary from .json files (to be used in the main program)
dbd3_e_templates_5a_dict = load_ppi_templates(templates_path, "dbd3_e_templates_5a.json")
dbd3_a_templates_5a_dict = load_ppi_templates(templates_path, "dbd3_a_templates_5a.json")
dbd3_ab_templates_5a_dict = load_ppi_templates(templates_path, "dbd3_ab_templates_5a.json")
dbd3_o_templates_5a_dict = load_ppi_templates(templates_path, "dbd3_o_templates_5a.json")

dbd3_all_templates_5a_dict = {**dbd3_e_templates_5a_dict, **dbd3_a_templates_5a_dict, **dbd3_ab_templates_5a_dict,
                      **dbd3_o_templates_5a_dict}


print("DBD3: All Complexes")
execute_with_elapsed_time(dbd_sanity_check,
                        pdb_id_list=dbd3_all_list,
                        templates_dict=dbd3_all_templates_5a_dict,
                        dbd_path=dbd5_path,
                        pdb_parser=pdb_parser,
                        lha_dict=lha_dict,
                        ranking_size=100,
                        verbose=True,
                        iteration_per_protein=1,
                        population_size=300,
                        number_of_generations=300,
                        crossover_probability=0.5,
                        mutation_probability=0.7,
                        tournament_size=3,
                        number_of_tournament=50)

print("DBD5: All Complexes")
execute_with_elapsed_time(dbd_sanity_check,
                        pdb_id_list=dbd5_all_list,
                        templates_dict=dbd5_all_templates_5a_dict,
                        dbd_path=dbd5_path,
                        pdb_parser=pdb_parser,
                        lha_dict=lha_dict,
                        ranking_size=100,
                        verbose=True,
                        iteration_per_protein=1,
                        population_size=300,
                        number_of_generations=300,
                        crossover_probability=0.5,
                        mutation_probability=0.7,
                        tournament_size=3,
                        number_of_tournament=50)
