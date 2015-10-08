import csv

def readsplit():
    f = open("people.csv")
    for line in f:
        print line.strip().split(",")

def csv_list():
    reader = csv.reader(open("people.csv"))
    TEMPLATE="name: %s, age: %s, id: %s"
    for item in reader:
        print item
        print item[0]
        print TEMPLATE%(item[0],item[1],item[2])

def csv_dict():
    reader = csv.DictReader(open("people.csv"))
    TEMPLATE="name: %(name)s, age: %(age)s, id: %(id)s"
    for item in reader:
        print item
        print TEMPLATE%(item)
csv_dict()
