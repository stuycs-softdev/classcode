import re

def find_phone(s):
    expr = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
    result = re.findall(expr,s);
    return result


def fp_test1():
    print "Should print: ['111-222-3333']"
    print find_phone("111-222-3333")

def fp_test2():
    print "Should print: []"
    print find_phone("1d1-222-3333")

if __name__=="__main__":
    fp_test1()
    fp_test2()
