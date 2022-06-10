def remove_hetatm_row(file_path):
	"""Remove HETATM Row
	Given a path to a PDB file, remove its HETATM rows

	Parameters:
	file_path (str): File path to a PDB file

	Returns:
	None

	"""
	line_list = []
	with open(file_path, "r") as fp:
		line_list = fp.readlines()

	with open(file_path, "w") as fp:
		for line in line_list:
			if "HETATM" not in line:
				fp.write(line)
