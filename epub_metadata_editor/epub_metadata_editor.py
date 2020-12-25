import argparse
import os
import re
import ebooklib
from ebooklib import epub
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="TERMINAL EPUB METADATA EDITOR\nNote: \
The name of the files needs to follow this structure: \
\n\{Book title\} - \{Author name\} \{Author Surname\}"
    )
    parser.add_argument(
        "-f",
        "--folder_path",
        type=Path,
        help="Absolute path to folder containing .epub files",
        required=True,
    )

    return parser.parse_args()


def epub_metadata_editor():

    args = parse_arguments()

    files = sorted(os.listdir(args.folder_path))

    for book in files:
        try:
            book_path = os.path.join(args.folder_path, book)
            epub_book = epub.read_epub(book_path)

            book_name = book.split("-")[0][:-1]
            book_name = book.split("-")[0][:-1] if book_name[:-1] == " " else book_name
            book_author = book.split("-")[1].split(".")[0]
            book_author = book_author[1:] if book_author[0] == " " else book_author

            print(f"Formatting: {book_name} - {book_author}")
            epub_book.set_title(book_name)
            epub_book.add_author(book_author)

            # write to the file
            epub.write_epub(book_path, epub_book, {})

        except:
            raise TypeError(
                "Improper file format - check whether the folder contains ONLY .epub files"
            )


if __name__ == "__main__":
    epub_metadata_editor()

    print("Formatting successful!")
