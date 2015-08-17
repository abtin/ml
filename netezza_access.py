__author__ = 'abtin'

import pyodbc


def connect():
    cnxn = pyodbc.connect('DRIVER={NetezzaSQL};SERVER=<IP>;PORT=5480;DATABASE=<DB>;UID=<UID>;PWD=<PWD>')
    print("Connected!")
    cursor = cnxn.cursor()
    count = cursor.execute("select count(*) from tbl").fetchone()
    print(count)

if __name__ == "__main__":
    connect()



