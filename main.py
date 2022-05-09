import pandas as pd
import numpy as np
import ebooklib as eb
from pathlib import PosixPath

path_books = PosixPath("./datos")
def check_data_epub():   
     
    list_epub_true = []
    for book in path_books.iterdir():
        try:
            if book.suffix == ".epub":
                return list_epub_true.append(book)
        except ValueError:
            
        # print(i.stem, type(i.suffix))