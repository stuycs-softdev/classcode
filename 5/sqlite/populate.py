import sqlite3
import csv

conn = sqlite3.connect('demo.db')
c = conn.cursor()

# remove old people and classes
q = "delete from people"
c.execute(q)
q = "delete from classes"
c.execute(q)


BASE='INSERT INTO people VALUES("%(name)s", %(age)s , %(id)s)'
for l in csv.DictReader(open("people.csv")):
    q = BASE%l
    print q
    c.execute(q)


BASE="""
INSERT INTO classes
  VALUES('%(name)s', %(grade)s,%(id)s)
"""
for l in csv.DictReader(open("classes.csv")):
    q = BASE%l
    print q
    c.execute(q)
    
    

conn.commit()





