import json

from bibtex.entry import BibEntry
from utils import read_from_editor

BASE_DIR = "data"

DEFAULT_ARTICLE_BIB = """@article{10.1214/13-AOS1127,
author = {Quentin Berthet and Philippe Rigollet},
title = {Optimal detection of sparse principal components in high dimension},
volume = {41},
journal = {The Annals of Statistics},
number = {4},
publisher = {Institute of Mathematical Statistics},
pages = {1780 -- 1815},
keywords = {High-dimensional detection, minimax lower bounds, planted clique,
semidefinite relaxation, sparse principal component analysis, spiked covariance model},
year = {2013},
doi = {10.1214/13-AOS1127},
URL = {https://doi.org/10.1214/13-AOS1127}
}
"""

DEFAULT_BOOK_BIB = """@book{wainwright_2019,
place={Cambridge},
series={Cambridge Series in Statistical and Probabilistic Mathematics},
title={High-Dimensional Statistics: A Non-Asymptotic Viewpoint},
DOI={10.1017/9781108627771},
publisher={Cambridge University Press},
author={Martin J. Wainwright},
year={2019},
collection={Cambridge Series in Statistical and Probabilistic Mathematics}}
"""

DEFAULT_IN_PROCEEDINGS_BIB = """@inproceedings{arous2022highdimensional,
title={High-dimensional limit theorems for {SGD}: Effective dynamics and critical scaling},
author={Gerard Ben Arous and Reza Gheissari and Aukosh Jagannath},
booktitle={Advances in Neural Information Processing Systems},
editor={Alice H. Oh and Alekh Agarwal and Danielle Belgrave and Kyunghyun Cho},
year={2022},
url={https://openreview.net/forum?id=Q38D6xxrKHe}
}
"""


def add_bib_entry():
    bib_entry = BibEntry(bibtex=read_from_editor(DEFAULT_BOOK_BIB))
    with open("data/index.jsonl", "a") as f:
        f.write(json.dumps(bib_entry.model_dump()))


def add_pdf():
    pass
