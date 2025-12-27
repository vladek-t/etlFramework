import datetime
from database.DatabasInit import InitDatabase

class InsertData(InitDatabase):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        InitDatabase().run()

    def insert_metadata(self):
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime("%d-%m-%Y")

        query = f"""insert into {self.table_name} (loader_name, tech_changed_dttm)
        select 'csv' as loader
        , current_timestamp as tech_changed_dttm"""
        self.cursor.execute(query)
        self.conn.commit()

InsertData('loader_name').insert_metadata()