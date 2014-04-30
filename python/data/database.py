import sqlite3 as lite

con = None

def connect(data_dir):
    global con
    con = lite.connect(data_dir + 'train.db')
    cur = con.cursor()
    return (cur, con)

def disconnect():
    con.close()