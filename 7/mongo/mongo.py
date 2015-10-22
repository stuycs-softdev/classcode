import random
from pymongo import MongoClient

# connection = MongoClient("hostname")
connection = MongoClient()

# for authentication
#db = connection.admin
#db.authenticate("username","password")



# from command line: use pd7
# we could also have done: db = connection.pd7
db = connection['pd7']

# from command line: show collections
print db.collection_names()

# we can drop a collection using db.collection.drop()

names = ['thluffy','bucky','sue','arnold','alice']
dtypes = ['plain','jelly','glazed','frosted']

# for i in range(10):
#     d = {'name' : random.choice(names),
#          'donut' : random.choice(dtypes),
#          'age' : random.randrange(15,30)}
#     db.people.insert(d)

# l=[]
# for i in range(10):
#     d = {'name' : random.choice(names),
#          'donut' : random.choice(dtypes),
#          'age' : random.randrange(15,30)}
#     l.append(d)
# db.people.insert(l)

res = db.people.find({'donut':'glazed'},{"_id":False})
for r in res:
    print r
