import sqlite3
import psycopg2

class Connection:
    def __init__(self):
        self.conn = sqlite3.connect("lite.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
        )

    def insert(self, item, quantity, price):
        self.cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))

    def view(self):
        self.cur.execute("SELECT * FROM store")
        rows = self.cur.fetchall()
        return rows

    def delete(self, item):
        self.cur.execute("DELETE FROM store WHERE item=?", (item,))
        rows = self.cur.fetchall()
        return rows

    def update(self, quantity, price, item):
        self.cur.execute(
            "UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item)
        )
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.commit()
        self.conn.close()
