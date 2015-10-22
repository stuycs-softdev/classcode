import random
from pymongo import MongoClient

# connection = Mongoclient("hostname")
connection = MongoClient()

# Authenticate if needed
#db = connection.admin
#db.authenticate('user','password')

# same as "use pd6" from the shell
# we could also do:  db = connection.pd6
db = connection['pd6']

print db.collection_names()
# db.people.drop() to get rid of a collection

names = ['thluffy','bucky',
         'bob','rob','dana','sue','theo']

dtype = ['plain','glazed','frosted','jelly']

# for i in range(10):
#     d = {'name' : random.choice(names),
#          'donut': random.choice(dtype),
#          'age': random.randrange(15,30)}
#     db.people.insert(d)

# l=[]
# for i in range(10):
#     d = {'name' : random.choice(names),
#          'donut': random.choice(dtype),
#          'age': random.randrange(15,30)}
#     l.append(d)
# db.people.insert(l)

res = db.people.find({'donut':'jelly'},{"_id":False})
for r in res:
    print r

