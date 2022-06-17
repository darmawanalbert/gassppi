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

# Load 1BVK receptor's PPI template
dbd5_a_templates_5a_dict = load_ppi_templates(templates_path, "dbd5_a_templates_5a.json")
ppi_template_1bvk_r_u = dbd5_a_templates_5a_dict["1BVK_r_u"]

# Load 1BVK receptor's protein structure
protein_structure_1bvk_r_u = load_pdb("1BVK_r_u", dbd5_path, pdb_parser, lha_dict, "lha")

predicted_ppis = gass_ppi(input_protein_structure=protein_structure_1bvk_r_u,
                          interface_template=ppi_template_1bvk_r_u,
                          population_size=400,
                          number_of_generations=200,
                          crossover_probability=0.9,
                          mutation_probability=0.9,
                          tournament_size=2,
                          number_of_tournament=20,
                          verbose=True)

# Script for PyMOL rendering
save_pymol_script("1BVK_r_u", ppi_template_1bvk_r_u, predicted_ppis[0][0], render_distance=False)

# Development Logs
amino_acid_dict= { x: 0 for x in amino_acid_list }
for residue in protein_structure_1bvk_r_u:
    amino_acid_dict[residue.residue_name] += 1

print(amino_acid_dict)

print_interface_info(ppi_template_1bvk_r_u)
