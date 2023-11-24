import time
from entry import Article, Book, InProceedings
from pydantic import BaseModel, Literal
from typing import Annotated, Literal

Tag = Literal["XAI", "Probability", "IS", "Statistics", "CS", "Meta", "Philosophy"]


class BibTexRecord(BaseModel):
    created_at: Annotated[int, Field(strict=True, gt=0, default_factory=time.time())]
    updated_at: Annotated[int, Field(strict=True, gt=0, default_factory=time.time())]
    tags: Annotated[list[Tag], Field(default=[])]
    bib_entry: Article | Book | InProceedings
