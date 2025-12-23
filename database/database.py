import sqlite3

class Database():
    def __init__(self, conn = 'database.db'):
        self.conn = sqlite3.connect(conn)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


db = Database()
db.close_connection()