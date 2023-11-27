import re

import pytest

from deer.bibtex.entry import _AUTHOR_RE, check_author_field

valid_author_names = [
    "Martin J. Wainwright",
    "Aukosh Jaganath",
    "Pythagoras",
    "Fei Fei Li",
    "Richard Socher",
    "Quentin Berthet",
    "Anderson Gray McKendrick",
]


@pytest.mark.parametrize("author_name", valid_author_names)
def test_valid_author_names(author_name: str):
    pattern = re.compile(_AUTHOR_RE)

    assert pattern.fullmatch(author_name)


valid_author_fields = [
    "Quentin Berthet and Philippe Rigollet",
    "Martin J. Wainwright",
    "Martin J. Wainwright and Test Test",
    "Gerard Ben Arous and Reza Gheissari and Aukosh Jagannath",
]


@pytest.mark.parametrize("author_field", valid_author_fields)
def test_valid_author_fields(author_field: str):
    assert author_field == check_author_field(author_field)


invalid_author_fields = [
    "Quentin Berthet3 and Philippe Rigollet",
    "Quentin Berthet3 and Philippe Rigollet",
    "Martin J. Wainwright, Test Test",
]


@pytest.mark.parametrize("author_field", invalid_author_fields)
def test_invalid_author_fields(author_field: str):
    with pytest.raises(ValueError):
        check_author_field(author_field)
