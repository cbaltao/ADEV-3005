'''
Carlo Baltao

ADEV-3005 (254275)

Topic Challenge - Module 6C

2024-10-13
''' 

import sqlite3


weather = {
    "2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1},
    "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
    "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}
}

class DBOperations:

    def __init__(self, db_name):
        """Initialize DBOperations class and properties"""
        self.conn = None
        self.c = None
        self.dbName = db_name
    
    def initialize_db(table_name):
        """Establish a connection to the database, and create a table."""
        try:
            self.conn = sqlite3.connect(self.dbName)
            self.c = self.conn.cursor()
            print("Opened database successfully.")
        except Exception as e:
            print("Error opening DB:", e)

        try:
            self.c.execute(f"""create table {table_name}
                            (id integer primary key autoincrement not null,
                            date text not null,
                            location text not null,
                            max real not null,
                            min real not null,
                            mean real not null);""")
            self.conn.commit()
            print("Table created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def insert_data(data, table_name):
        """Insert data into table, then close connection."""
        try:
            for date, values in data.items():
                self.c.execute(f"""
                    INSERT INTO {table_name} (date, location, max, min, mean)
                    VALUES (?, ?, ?, ?, ?);
                """, (date, "Winnipeg, MB", values['Max'], values['Min'], values['Mean']))
            self._conn.commit()
            print("Added sample successfully.")
        except Exception as e:
            print("Error inserting sample.", e)

        try:
            for row in self.c.execute("select * from weather"):
                print(row)
        except Exception as e:
            print("Error fetching samples.", e)

        self.conn.close()

weather_db = DBOperations("weather.sqlite")
weather_db.initialize_db("weather")
weather_db.insert_data(weather, "weather")