import re
import time
import uuid
from typing import Annotated, Literal, Union

import bibtexparser
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    conlist,
    field_serializer,
    field_validator,
    model_validator,
)


def check_author_field(author_field: str):
    pattern = re.compile(r"(?:\w+\s+and\s+)*\w+(?:\s+\w+)*")
    exception_msg = """The author field has to be of the form: NAME and NAME and
    ... and NAME where NAME can consist of multiple parts sperated by a whitespace"""
    if not pattern.fullmatch(author_field):
        raise ValueError(exception_msg)
    return author_field


def extract_last_names(author_field: str) -> list[str]:
    return [name.split(" ")[-1] for name in author_field.split(" and ")]


class Article(BaseModel):
    author: Annotated[str, Field(strict=True, min_length=1)]
    title: Annotated[str, Field(strict=True, min_length=1)]
    journal: Annotated[str, Field(strict=True, min_length=1)]
    year: int
    volume: int | None = None
    pages: str | None = None
    month: str | None = None
    note: str | None = None

    @field_validator("author", mode="after")
    def check_author_field(cls, author_field):
        return check_author_field(author_field)

    def construct_key(self):
        return "_".join(
            [
                *extract_last_names(self.author)[:2],
                str(self.year),
                *self.title.split(" ")[:3],
            ]
        )


class Book(BaseModel):
    author: Annotated[str, Field(strict=True, min_length=1)]
    title: Annotated[str, Field(strict=True, min_length=1)]
    publisher: Annotated[str, Field(strict=True, min_length=1)]
    year: int
    volume: int | None = None
    number: int | None = None
    series: str | None = None
    address: str | None = None
    month: str | None = None
    note: str | None = None
    isbn: str | None = None

    @field_validator("author")
    def check_author_field(cls, author_field):
        return check_author_field(author_field)

    def construct_key(self):
        return "_".join(
            [
                *extract_last_names(self.author)[:2],
                str(self.year),
                *self.title.split(" ")[:3],
            ]
        )


class InProceedings(BaseModel):
    author: Annotated[str, Field(strict=True, min_length=1)]
    title: Annotated[str, Field(strict=True, min_length=1)]
    booktitle: Annotated[str, Field(strict=True, min_length=1)]
    year: int
    editor: str | None = None
    volume: int | None = None
    number: int | None = None
    sries: str | None = None
    pages: str | None = None
    address: str | None = None
    month: str | None = None
    organization: str | None = None
    publisher: str | None = None
    note: str | None = None

    @field_validator("author")
    def check_author_field(cls, author_field):
        return check_author_field(author_field)

    def construct_key(self):
        return "_".join(
            [
                *extract_last_names(self.author)[:2],
                str(self.year),
                *self.title.split(" ")[:3],
            ]
        )


EntryType = Literal["article", "book", "inproceedings"]


class BibEntry(BaseModel):
    id: Annotated[uuid.UUID, Field(default_factory=uuid.uuid4)]
    created_at: Annotated[
        int, Field(strict=True, gt=0, default_factory=lambda: int(time.time()))
    ]
    entry_type: EntryType | None = None
    key: Annotated[str, Field(min_lenght=1)]
    bibtex: conlist(Union[Article, Book, InProceedings], min_length=1, max_length=1)

    model_config = ConfigDict(
        extra="allow",
    )

    @field_serializer("id")
    def serializer_id(self, id):
        return str(id)

    @field_serializer("bibtex")
    def serialize_bibtex(self, bibtex):
        # return bibtex[0].model_dump()
        return (
            f"@{self.entry_type}"
            + "{"
            + f"{self.key},\n"
            + BibEntry._dict_to_bibtex(
                {
                    key: val
                    for key, val in bibtex[0].model_dump().items()
                    if val is not None
                }
            )
            + "}"
        )

    def _dict_to_bibtex(bib_dict):
        return "\n".join([f"{key}={{{val}}}" for key, val in bib_dict.items()])

    @model_validator(mode="before")
    @classmethod
    def transform_field_list_to_dict(cls, bibtex_input: str):
        entry = list(bibtexparser.parse_string(bibtex_input).entries_dict.values())[0]
        # print(dir(entry_dict))

        # entry = entry_dict["bibtex"][0]
        bib_dict = {
            BibEntry.__strip_newline_prefix(field.key): field.value
            for field in entry.fields
        }
        ret = {
            "bibtex": [bib_dict],
            "entry_type": entry.entry_type,
            "key": BibEntry._construct_key(
                bib_dict["author"], bib_dict["year"], bib_dict["title"]
            ),
        }
        return ret

    @staticmethod
    def _construct_key(author: str, year: int, title: str) -> str:
        return "_".join(
            [
                *extract_last_names(author)[:2],
                str(year),
                *title.split(" ")[:3],
            ]
        )

    @staticmethod
    def __strip_newline_prefix(s: str):
        return s[2:] if s.startswith("\\n") else s
