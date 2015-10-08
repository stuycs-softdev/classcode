
#f = open("people.csv")
#for line in f.readlines():
#    print line.strip().split(",")


import csv

def csv_list():
    reader = csv.reader(open("people.csv"))

    BASELINE = "Name: %s, id: %s, Age: %s"
    for line in reader:
        print BASELINE%(line[0],line[1],line[2])


def csv_dict():
    reader = csv.DictReader(open("people.csv"))
    BASELINE = "Name: %(name)s, id: %(id)s, Age: %(age)s"
    for line in reader:
        print line
        print BASELINE%line

#csv_list()
csv_dict()
