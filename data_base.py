'''
name     score

name1    400
name2    100
name3    500
'''
import sqlite3

db = sqlite3.connect("2048.sqlite")
cursor = db.cursor()

cursor.execute("""
create table if not exists RECORDS(
    name text,
    score integer
)""")

def insert_result(name, score):
    cursor.execute("""
        insert into RECORDS values(?, ?)
    """, (name, score))
    db.commit()

def get_best():
    cursor.execute("""
        SELECT ROWID, name, score from RECORDS
        GROUP by name
        ORDER by score DESC
        limit 3
    """)
    return cursor.fetchall()

result = get_best()
#print(result)
