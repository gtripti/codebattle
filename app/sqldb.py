import sqlite3

def sql_query(query):
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    return rows

def sql_edit_insert(query, var):
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute(query,var)
    rows=cur.fetchall()
    return rows

