import pytest

from deer.bibtex.entry import check_author_field

valid_author_fields = [
    "Quentin Berthet and Philippe Rigollet",
    "Martin J. Wainwright",
    "Gerard Ben Arous and Reza Gheissari and Aukosh Jagannath",
]


@pytest.mark.parametrize("author_field", valid_author_fields)
def test_valid_author_fields(author_field: str):
    assert author_field == check_author_field(author_field)


def test_invalid_author_fields(authore_field: str):
    pass
