import sqlite3


class BooksDB:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
        )

    def insert(self, title, author, year, isbn):
        self.cur.execute(
            "INSERT INTO books VALUES(NULL,?,?,?,?)", (title, author, year, isbn)
        )

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute(
            "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
            (title, author, year, isbn),
        )
        rows = self.cur.fetchall()
        return rows

    def update(self, id, title, author, year, isbn):
        self.cur.execute(
            "UPDATE books SET id=?, title=?, author=?, year=?, isbn=?",
            (id, title, author, year, isbn),
        )

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))

    def __del__(self):
        self.conn.commit()
        self.conn.close()
