import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def dropTable(conn):

    delete_query = "DROP TABLE product;"
    try:
        c = conn.cursor()
        c.execute(delete_query)
    except Error as e:
        print(e)


def main():

    database = r".\Database\sqlite\scrapeSqlite.db"

    # create a database connection
    conn = create_connection(database)

    try:
        with conn:
            dropTable(conn)
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
