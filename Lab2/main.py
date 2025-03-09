import csv
from collections import namedtuple
from dataclasses import dataclass, field, make_dataclass

print(csv)
orders = csv.reader(open("csvki/zamowienia.csv", encoding='utf-8'), delimiter=';')
orders = list(orders)

for order in orders[:5]:
    print(order)

raw_arguments = orders[0]
print(type(raw_arguments))

lower_arguments = [x.lower() for x in raw_arguments]
lower_arguments = [x.replace(" ", "_") for x in lower_arguments]
print(lower_arguments)



Order = namedtuple('Order', lower_arguments)
o = map(Order._make, csv.reader(open("csvki/zamowienia.csv", encoding='utf-8'), delimiter=';'))
o = list(o)

for x in o[1:11]:
    print(x)

#ZADANIE 1

sample = csv.reader(open("csvki/zamowienia.csv", encoding='utf-8'), delimiter=';')
l = list(sample)

def tuple_task(data):
    raw_args = data[0]
    lower_args = [x.lower() for x in raw_args]
    lower_args = [x.replace(" ", "_") for x in lower_args]
    Order = namedtuple('Order', lower_args)
    result = map(Order._make, data)
    result = list(result)
    return result

o2 = tuple_task(l)

for row in o2[1:11]:
    print(row)

#ZADANIE 2

Point = namedtuple('Point', ['x','y'], defaults=[0,0])
p = Point(6, 9)
p2 = Point(3, 4)
p3 = Point(3, 4)
p4 = Point()

print(dir(p))
print(p > p2)
print(p == p4)
print(p3 != p2)
print(p2 < p3)
print(p3 >= p2)
print(p4 <= p)

print(p + p2)
#print(p - p2)
print(p * p4)
print(p * 2)

#ZADANIE 3

dictionary = {
    1 : {
        'class_name': 'Osoba',
        'props': [('name', 'str'), ('is_admin', 'bool', 'False')]},
    2 : {
        'class_name': 'Produkt',
        'props': [('name', 'str'), ('price', 'float', '0.0'), ('quantity', 'float', '0.0')]}
    }

def class_from_dict(data):
    class_name = data["class_name"]
    props = data["props"]
    return make_dataclass(class_name, props)

a = dictionary[1]
b = a["class_name"]

class1 = class_from_dict(dictionary[1])
print(class1.__dict__)

class2 = class_from_dict(dictionary[2])
print(class2.price)
print(class2.quantity)
print(class1.is_admin)
