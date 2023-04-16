# gassppi

This repository contains the implementation of GASS-PPI (Genetic Active Site Search for Protein-Protein Interfaces), a method to predict [PPI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2566606/) of a monomeric protein structure (represented as a [.pdb](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/introduction) file).

## Installation

To run GASS-PPI on your local machine, perform all steps below:

1. Download and install [Python 3.8](https://www.python.org/downloads/release/python-3816/)

2. Install all required Python libraries (including [Biopython](https://biopython.org/)), by referring to the `requirements.txt`.
For example, if you are using [pip](https://pip.pypa.io/en/stable/):

```shell
pip install -r requirements.txt

```

3. We use a module called [MSMS](https://ssbio.readthedocs.io/en/latest/instructions/msms.html), which is a required dependency to use [Bio.PDB.ResidueDepth module](https://biopython.org/docs/1.79/api/Bio.PDB.ResidueDepth.html). This repository contains a fork of `msms` module (under `msms/` directory), we only need to add this directory path (i.e., `[your_root_path]/gassppi/msms`) to the local machine's PATH environment variable.

## Run GASS-PPI scripts

After finishing the installation steps, we can run some `GASS-PPI` scripts, available at the root directory. For example, we can run `run_sample.py` to ensure that our installation is successful:

```shell
python run_sample.py

```

## Directory Structure

    .
    ├── benchmark                   #
    ├── constant                    #
    ├── core                        #
    ├── data                        #
    ├── model                       #
    ├── utility                     #
    └── README.md

## Datasets

All datasets used to execute and benchmark GASS-PPI are stored inside the `data/` directory. This includes the original [.pdb](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/introduction) and [.ply](http://paulbourke.net/dataformats/ply/) files that represents the protein structure, as well as the preprocessed PPI templates stored as `.json` files. List of [PDB ID](https://www.rcsb.org/docs/general-help/identifiers-in-pdb) for each dataset is stored inside the `constant/` directory as a Python list.

There are two main datasets used in GASS-PPI, which are:
1. Docking Benchmark Dataset (abbreviated as DBD). We used two versions:
- DBD5: https://zlab.umassmed.edu/benchmark/benchmark5.0.html
- DBD3: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2726780/

2. MaSIF Dataset: https://github.com/lpdi-epfl/masif

## Contributors

- [Albert Darmawan](https://github.com/darmawanalbert)
- [A/Prof Douglas E. V. Pires](https://orcid.org/0000-0002-3004-2119)
- [Prof Sandro Carvalho Izidoro](https://orcid.org/0000-0001-5555-3321)

## Credits

Credits to open source tools/libraries used in this repository. This includes [MSMS](https://ssbio.readthedocs.io/en/latest/instructions/msms.html), [Python](https://www.python.org/downloads/release/python-3816/) and some available libraries (listed in `requirements.txt`), and [PyMOL](https://pymol.org/2/).
