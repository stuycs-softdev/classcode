

def readsplit():
    f = open("people.csv")
    for line in f:
        print line.strip().split(",")

import csv

def csv_list():
    reader = csv.reader(open("people.csv"))
    BASE="Name: %s, Age: %s, ID: %s"
    for line in reader:
        print line
        print line[0]
        print BASE%(line[0],line[1],line[2])
        print

def csv_dict():
    reader = csv.DictReader(open("people.csv"))
    BASE="Name: %(name)s, Age: %(age)s, ID: %(id)s"
    for line in reader:
        print BASE%line
        

csv_dict()
