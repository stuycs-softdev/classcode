
import sqlite3
import csv

conn = sqlite3.connect("demo.db")
c = conn.cursor()

q = "delete from people"
c.execute(q)
BASE="INSERT INTO people VALUES('%(name)s',%(age)s,%(id)s)"
for item in csv.DictReader(open("people.csv")):
    q = BASE%item
    print q
    c.execute(q)

q = "delete from classes"
c.execute(q)
BASE="""
INSERT INTO classes
  VALUES("%(name)s", %(grade)s, %(id)s)
"""
for item in csv.DictReader(open("classes.csv")):
    q = BASE%item
    print q
    c.execute(q)
conn.commit()
        
