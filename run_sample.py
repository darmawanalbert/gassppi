from Bio.PDB import *
import warnings

from core.gassppi import gass_ppi
from utility.load_pdb import load_pdb
from utility.load_ppi_templates import load_ppi_templates
from utility.print_interface_info import print_interface_info
from utility.save_pymol_script_file import save_pymol_script
from constant.directory_constant import dbd5_path, templates_path
from constant.last_heavy_atom import lha_dict
from constant.amino_acid import amino_acid_list

warnings.filterwarnings("ignore")

pdb_parser = PDBParser()

sample_pdb_id = "1BVK_r_u"

# Load sample PPI template
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

sample_ppi_template = dbd5_all_templates_5a_dict[sample_pdb_id]

# Load sample protein structure
sample_protein_structure = load_pdb(sample_pdb_id, dbd5_path, pdb_parser, lha_dict, "lha")

predicted_ppis = gass_ppi(input_protein_structure=sample_protein_structure,
                          interface_template=sample_ppi_template,
                          population_size=300,
                          number_of_generations=300,
                          crossover_probability=0.5,
                          mutation_probability=0.7,
                          tournament_size=3,
                          number_of_tournament=50,
                          verbose=True)

# Script for PyMOL rendering
save_pymol_script(sample_pdb_id, sample_ppi_template, predicted_ppis[0][0], render_distance=False)

# Development Logs
amino_acid_dict= { x: 0 for x in amino_acid_list }
for residue in sample_protein_structure:
    amino_acid_dict[residue.residue_name] += 1

print("Number of each amino acid type")
print(amino_acid_dict)

print("Actual PPI templates")
print_interface_info(sample_ppi_template)
