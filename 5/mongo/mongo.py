import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()

# To authenticate after connecting
# db = connection.admin
# db.authenticate('username','password')

db = connection['pd5']

print db.collection_names()

names = ["Thluffy", "Bucky",
         "Susan", "Victor","Sarah","Kictor"]

dtype = ['plain','frosted','glazed','jelly']

# for i in range(10):
#     d = {'name':random.choice(names),
#          'donut':random.choice(dtype),
#          'age':random.randrange(10,30)}
#     db.people.insert(d);

# l=[]
# for i in range(10):
#     d = {'name':random.choice(names),
#          'donut':random.choice(dtype),
#          'age':random.randrange(10,30)}
#     l.append(d)
# db.people.insert(l)
    
res = db.people.find({'donut':'jelly'},{"_id":False})
for r in res:
    print r
