"""
This is a module that contains an interface to interact with database
"""
import sqlite3


class Database:
    """
    Represents a database interface with minimal functionality needed for this
    task.
     """
    def __init__(self, db="db.sqlite3"):
        """Initialize a new database connection and a cursor"""
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.close_connection()

    def query_data(self, table, **columns):
        """
        Execute a SQL SELECT query that returns all the records from the
        database that match the filters given for columns.
        """
        query_str = f"SELECT * FROM {table}"

        if columns:
            query_str += " WHERE"

            for i, (column, value) in enumerate(columns.items()):
                if i:
                    query_str += " AND"

                query_str += f" {column}='{value}'"

            query_str += ";"

        self.cursor.execute(query_str)

        return self.cursor.fetchall()

    def close_connection(self):
        """Closes the current database connection"""
        self.connection.close()
