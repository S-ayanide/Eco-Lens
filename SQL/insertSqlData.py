import sqlite3
import pickle
from sqlite3 import Error

# Loading Saved Dataset
with open(r'./Data/item_details_url', 'rb') as item_data:
    items = pickle.load(item_data)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def insert_product(conn, product):
    """
    Create a new product into the product table
    :param conn:
    :param product:
    :return: product id
    """
    sql = ''' INSERT INTO product(name,image,url)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, product)
    return cur.lastrowid


def fetchData():

    # check the item list
    for item in items:
        print(item)
        print("\n")


def main():

    database = r".\Database\sqlite\scrapeSqlite.db"

    # create a database connection
    conn = create_connection(database)

    try:
        with conn:
            # add product items
            for item in items:
                product = (item['item_name'],
                           item['item_image'], item['item_url'])
                product_id = insert_product(conn, product)
    except Error as e:
        print(e)


if __name__ == '__main__':
    fetchData()
