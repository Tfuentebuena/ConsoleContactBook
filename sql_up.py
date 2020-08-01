import csv
import sqlite3


def uploader(filename="contacts.csv"):
    con = sqlite3.connect("sql_DB.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE t (Name, Address, Phone, Email);")

    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        to_db = [(i["Name"], i["Address"], i["Phone"], i["Email"]) for i in
                 reader]

    cur.executemany(
        "INSERT INTO t (Name, Address, Phone, Email) VALUES (?, ?, ?, ?)",
        to_db)
    con.commit()
    con.close()
