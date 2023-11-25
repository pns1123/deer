import os
from typing import Optional

import typer
from add import add_bib_entry
from git import Repo

app = typer.Typer()


@app.command()
def init():
    # 1) git init
    print("initializing git repo...")
    Repo.init(".")
    # 2) add dirs for pdfs and md notes
    print("initializing data directory...")
    os.makedirs("./data/pdf", exist_ok=True)
    os.makedirs("./data/md", exist_ok=True)
    # 3) if bib index file does not exist create it
    with open("./data/index.jsonl", "a"):
        pass

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
