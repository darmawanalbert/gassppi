def can_run_gass_ppi(input_protein_structure, interface_template):
    """Can Run GASS PPI?
    Defensive Programming effort. Perform pre-check before running GASS-PPI.
    Edge Case:
    - The template size should be larger than 0 (sample case: 2O3B has 0 template with distance threshold 4A)
    - GASS-PPI shouldn't run if the protein structure does not contain
      all necessary residues to form an individual which has the same
      residue types with the interface template
      e.g. The template has 4 CYS, but the input protein structure only contains 3 CYS


    Parameters:
    input_protein_structure (list[Residue]): List of Residue which constitutes the entire protein structure
    interface_template (list[Residue]): List of Residue which is used as a template for the genetic algorithms

    Returns:
    bool: True if it is possible to run GASS-PPI, False otherwise

    """
    # Check whether the template size is valid (>0)
    if len(interface_template) <= 0:
        return False

    filtered_protein_structure = [residue for residue in input_protein_structure]
    # Count the number of each residue type in the filtered_protein_structure
    number_of_residues_in_structure = { x: 0 for x in amino_acid_list }
    for residue in filtered_protein_structure:
        number_of_residues_in_structure[residue.residue_name] += 1

    # Count the number of each residue type in the interface_template
    number_of_residues_in_template = { x: 0 for x in amino_acid_list}
    for residue in interface_template:
        number_of_residues_in_template[residue.residue_name] += 1

    for amino_acid in amino_acid_list:
        if number_of_residues_in_template[amino_acid] > number_of_residues_in_structure[amino_acid]:
            return False

    return True
