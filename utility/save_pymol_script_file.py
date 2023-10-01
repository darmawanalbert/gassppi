import os
from constant.directory_constant import repository_path, dbd5_path
from constant.last_heavy_atom import lha_dict

def save_pymol_script(pdb_id, actual_interface, predicted_interface, render_distance=False):
    """Save PyMOL Script
    Given a PDB ID and its corresponding PPIs, generate .pml file which contains script to visualise
    these in PyMOL

    Parameters:
    pdb_id (str): The PDB ID of the protein structure
    actual_interface (list[Residue]): List of amino acids that constitute the actual interface
    predicted_interface (list[Residue]): List of amino acids that constitute the predicted interface
    render_distance (bool): Indicate whether to render Euclidean distance for each residue pair (default: False)

    Returns:
    None

    """
    target_path = repository_path + "/pymol-script/" + pdb_id + ".pml"
    # Make sure that all directory within the target_path exists
    # os.makedirs will recursively make the directory if it doesn't exist
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    # Initialise the PyMOL script buffer
    pymol_script = "bg_color white;\n"
    pymol_script += "hide all;\n\n"

    # Add PyMOL command to load PDB structure
    pymol_script += "load " + dbd5_path + pdb_id + ".pdb;\n\n"

    # Add PyMOL command to load the actual interface
    actual_interface_str = ""
    for i in range(len(actual_interface)):
        if i != 0:
            actual_interface_str += " + "
        actual_interface_str += pdb_id + "//" + actual_interface[i].chain_name + "/" + str(actual_interface[i].residue_sequence_position) + "/"

    pymol_script += "create actual_interface, (" + actual_interface_str + ");\n"
    pymol_script += "show sticks, actual_interface;\n"
    pymol_script += "util.cbaw actual_interface;\n\n"

    # Add PyMOL command to load the predicted interface
    predicted_interface_str = ""
    for i in range(len(predicted_interface)):
        if i != 0:
            predicted_interface_str += " + "
        predicted_interface_str += pdb_id + "//" + predicted_interface[i].chain_name + "/" + str(predicted_interface[i].residue_sequence_position) + "/"

    pymol_script += "create predicted_interface, (" + predicted_interface_str + ");\n"
    pymol_script += "show sticks, predicted_interface;\n"
    pymol_script += "util.cbam predicted_interface;\n"

    if render_distance:
        pymol_script += "\n"

        # Render distance in the actual interface
        for j in range(len(actual_interface) - 1):
            for k in range(j+1, len(actual_interface)):
                pymol_script += "distance actual_dist, (actual_interface//"
                pymol_script += actual_interface[j].chain_name + "/"
                pymol_script += str(actual_interface[j].residue_sequence_position) + "/"
                pymol_script += lha_dict[actual_interface[j].residue_name]
                pymol_script += "), (actual_interface//"
                pymol_script += actual_interface[k].chain_name + "/"
                pymol_script += str(actual_interface[k].residue_sequence_position) + "/"
                pymol_script += lha_dict[actual_interface[k].residue_name]
                pymol_script += ");\n"
        pymol_script += "\n"

        # Render distance in the predicted interface
        for j in range(len(predicted_interface) - 1):
            for k in range(j+1, len(predicted_interface)):
                pymol_script += "distance predicted_dist, (predicted_interface//"
                pymol_script += predicted_interface[j].chain_name + "/"
                pymol_script += str(predicted_interface[j].residue_sequence_position) + "/"
                pymol_script += lha_dict[predicted_interface[j].residue_name]
                pymol_script += "), (predicted_interface//"
                pymol_script += predicted_interface[k].chain_name + "/"
                pymol_script += str(predicted_interface[k].residue_sequence_position) + "/"
                pymol_script += lha_dict[predicted_interface[k].residue_name]
                pymol_script += ");\n"
        pymol_script += "\n"

        # Label configuration
        pymol_script += "label (actual_interface and predicted_interface and name ca),\"%s-%s\" % (resn,resi)"
        pymol_script += "set label_size, -0.6;\n"
        pymol_script += "set label_color, black;\n"
        pymol_script += "set dash_gap, 0.5;\n"
        pymol_script += "set dash_radius, 0.1;\n"
        pymol_script += "set dash_color, grey;\n"
        pymol_script += "set ray_shadows, on;\n"

    # Save the PyMOL script buffer to a .pml file
    with open(target_path, "w") as fp:
        fp.write(pymol_script)
