import sqlite3

class Database():
    def __init__(self, conn = 'database.db'):
        self.conn = sqlite3.connect(conn)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
    
    def create_meta_table(self):
        drop_loader_type_tbl = """
        drop table loader_name;
    """

        create_loader_type_tbl = """
        create table if not exists loader_name (
        loader_name string,
        tech_changed_dttm timestamp
    );
    """
        self.cursor.execute(drop_loader_type_tbl)
        self.conn.commit()
        self.cursor.execute(create_loader_type_tbl)
        self.conn.commit()
        self.close_connection()

db = Database()
db.create_meta_table()