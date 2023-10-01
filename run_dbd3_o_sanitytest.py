from Bio.PDB import *

from utility.load_ppi_templates import load_ppi_templates
from utility.execute_with_elapsed_time import execute_with_elapsed_time
from constant.directory_constant import dbd5_path, templates_path
from constant.last_heavy_atom import lha_dict
from constant.dbd3_dataset import dbd3_o_list
from benchmark.dbd_sanity_check import dbd_sanity_check

pdb_parser = PDBParser()

# Load DBD3 PPI template dictionary from .json files (to be used in the main program)
dbd3_o_templates_5a_dict = load_ppi_templates(templates_path, "dbd3_o_templates_5a.json")

print("DBD3: O")
execute_with_elapsed_time(dbd_sanity_check,
                        pdb_id_list=dbd3_o_list,
                        templates_dict=dbd3_o_templates_5a_dict,
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
