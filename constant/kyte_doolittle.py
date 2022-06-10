# Kyte-Doolittle Hydrophobicity scale mapping
# Taken from: https://resources.qiagenbioinformatics.com/manuals/clcgenomicsworkbench/650/Hydrophobicity_scales.html
# Reference: https://home.hiroshima-u.ac.jp/kei/IdentityX/picts/BE-hydrophobicity.pdf#page4
# Positive values -> hydrophobic
# Negative values -> hydrophilic (more likely to be interact with solvent -> surface)
kyte_doolittle_dict = {
    "ALA": 1.8,
    "CYS": 2.5,
    "ASP": -3.5,
    "GLU": -3.5,
    "PHE": 2.8,
    "GLY": -0.4,
    "HIS": -3.2,
    "ILE": 4.5,
    "LYS": -3.9,
    "LEU": 3.8,
    "MET": 1.9,
    "ASN": -3.5,
    "PRO": -1.6,
    "GLN": -3.5,
    "ARG": -4.5,
    "SER": -0.8,
    "THR": -0.7,
    "VAL": 4.2,
    "TRP": -0.9,
    "TYR": -1.3,
}
