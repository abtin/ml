__author__ = 'abtin'

import psycopg2

def conntest():
    conn = psycopg2.connect(user="user", password="password",
                            host="host", port=5432,
                            database="db")


    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM TABLE")

if __name__ == "__main__":
    conntest()