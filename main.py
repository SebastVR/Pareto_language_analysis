"""Pareto analysis language."""
from pathlib import PosixPath

path_books = PosixPath("./data")


def check_data_epub():
    """Execute the check for data epub."""
    list_epub_true = []
    for book in path_books.iterdir():
        try:
            if book.suffix == ".epub":
                list_epub_true.append(book)
        except ValueError:
            print("error")
