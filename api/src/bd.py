# Librerías para el manejo de SQLite3
import sqlite3
from pathlib import Path

CURRENT_DIR = Path.cwd()
BASE_DIR = Path(CURRENT_DIR).parent

URL_DB = f"{CURRENT_DIR / 'data/db/antropometry'}"

def open_connection():
    conn = sqlite3.connect(URL_DB)
    return conn

def close_connection(conn):
    conn.commit()
    conn.close()

def exec_query_result(query, conn, varios=True):
    cur = conn.cursor()
    cur.execute(query)

    if varios:
        return cur.fetchall()
    else: 
        return cur.fetchone()

def exec_query(query, conn):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
