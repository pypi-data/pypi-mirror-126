# PASTE

![PASTE Overview](https://github.com/raphael-group/paste/blob/main/paste_overview.png)

PASTE is a computational method that leverages both gene expression similarity and spatial distances between spots to align and integrate spatial transcriptomics data. In particular, there are two methods:
1. `pairwise_align`: align spots across pairwise slices.
2. `center_align`: integrate multiple slices into one center slice.

You can read our preprint [here](https://www.biorxiv.org/content/10.1101/2021.03.16.435604v1). 

PASTE is actively being worked on with future updates coming. 

### Recent News

As of version 1.1.0, PASTE now runs on AnnData making it very easy to integrate with Scanpy for better downstream analysis. Hooray!

This also means that the old version that uses the `STLayer` object is now deprecated.

### Dependencies

To run PASTE, you will need the following Python packages:
1. POT: Python Optimal Transport (https://PythonOT.github.io/)
2. Scanpy (https://scanpy.readthedocs.io/en/stable/)
3. Numpy
4. Pandas 
5. scipy.spatial
6. sklearn.preprocessing

### Installation

The easiest way is to install PASTE on pypi: https://pypi.org/project/paste-bio/. 

`pip install paste-bio` 

Or you can install PASTE on bioconda: https://anaconda.org/bioconda/paste-bio.

`conda install -c bioconda paste-bio`

Check out Tutorial.ipynb for an example of how to use PASTE.

Alternatively, you can clone the respository and run from command line (see below).


### Command Line

We provide the option of running PASTE from the command line. 

First, clone the repository:

`git clone https://github.com/raphael-group/paste.git`

Next, when providing files, you will need to provide two separate files: the gene expression data followed by spatial data (both as .csv) for the code to initialize one slice object.

Sample execution (based on this repo): `python paste-cmd-line.py -m center -f ./sample_data/slice1.csv ./sample_data/slice1_coor.csv ./sample_data/slice2.csv ./sample_data/slice2_coor.csv ./sample_data/slice3.csv ./sample_data/slice3_coor.csv`

Note: `pairwise` will return pairwise alignment between each consecutive pair of slices (e.g. \[slice1,slice2\], \[slice2,slice3\]).

| Flag | Name | Description | Default Value |
| --- | --- | --- | --- |
| -m | mode | Select either `pairwise` or `center` | (str) `pairwise` |
| -f | files | Path to data files (.csv) | None |
| -d | direc | Directory to store output files | Current Directory |
| -a | alpha | Alpha parameter for PASTE | (float) `0.1` |
| -c | cost | Expression dissimilarity cost (`kl` or `Euclidean`) | (str) `kl` |
| -p | n_components | n_components for NMF step in `center_align` | (int) `15` |
| -l | lmbda | Lambda parameter in `center_align` | (floats) probability vector of length `n`  |
| -i | intial_slice | Specify which file is also the intial slice in `center_align` | (int) `1` |
| -t | threshold | Convergence threshold for `center_align` | (float) `0.001` |
| -x | coordinates | Output new coordinates (toggle to turn on) | `Flase` |
| -w | weights | Weights files of spots in each slice (.csv) | None |
| -s | start | Initial alignments for OT. If not given uses uniform (.csv structure similar to alignment output) | None |

`pairwise_align` outputs a (.csv) file containing mapping of spots between each consecutive pair of slices. The rows correspond to spots of the first slice, and cols the second.

`center_align` outputs two files containing the low dimensional representation (NMF decomposition) of the center slice gene expression, and files containing a mapping of spots between the center slice (rows) to each input slice (cols).

### Sample Dataset

Added sample spatial transcriptomics dataset consisting of four breast cancer slice courtesy of:

Ståhl, Patrik & Salmén, Fredrik & Vickovic, Sanja & Lundmark, Anna & Fernandez Navarro, Jose & Magnusson, Jens & Giacomello, Stefania & Asp, Michaela & Westholm, Jakub & Huss, Mikael & Mollbrink, Annelie & Linnarsson, Sten & Codeluppi, Simone & Borg, Åke & Pontén, Fredrik & Costea, Paul & Sahlén, Pelin Akan & Mulder, Jan & Bergmann, Olaf & Frisén, Jonas. (2016). Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science. 353. 78-82. 10.1126/science.aaf2403. 

Note: Original data is (.tsv), but we converted it to (.csv).
