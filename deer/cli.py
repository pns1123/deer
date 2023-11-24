import json
import os
import typer

from add import add_bib_entry, add_pdf
from git import Repo
from typing import Optional

app = typer.Typer()


@app.command()
def init():
    # 1) git init
    print("initializing git repo...")
    Repo.init(".")
    # 2) add dirs: pdfs, notes, bib_files
    print("initializing data directory...")
    os.makedirs("./data/pdf", exist_ok=True)
    os.makedirs("./data/md", exist_ok=True)
    with open("./data/db.json", 'w') as fp:
        json.dump({}, fp)

    print("initialization successfully completed!")


@app.command()
def add():
    # 1) open vim to insert and edit .bib
    # 2) check .bib
    # 3) check for duplicates
    # 4) ask for pdf file
    # 5) ask for note
    add_bib_entry()


@app.command()
def rm():
    # remove entry (bibtex, note, pdf)
    # add safety check
    print("rm")


@app.command()
def edit(id: str, pdf: Optional[bool] = False, note: Optional[bool] = False):
    # edit bibtex or note of entry
    print("edit")


@app.command()
def view():
    # start markserv in notes dir
    print("view")


@app.command()
def find(query: str, author: Optional[bool] = False, tag: Optional[bool] = False):
    if author:
        print(f"author: {query}")
    elif tag:
        print(f"tag: {query}")
    else:
        print(f"RAG query: {query}")
