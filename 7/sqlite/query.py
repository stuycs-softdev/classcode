import sqlite3

conn = sqlite3.connect("demo.db")
c = conn.cursor()

q="""
SELECT people.name, classes.name, grade
  FROM people,classes
  WHERE people.id=classes.id and grade > 90
"""

result = c.execute(q)

for r in result:
    print r
    print r[0]


print "TAKE TWO"
for r in result:
    print r
    print r[0]
print "DONE"
