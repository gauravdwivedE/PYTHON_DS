'''
Dunder/ magical metho

# __str__

#__len__

#__add__

'''

#__str__ example

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


b1 = Book("Python Programming")
print(b1)

#__len__ example   

class Shopping:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

shop = Shopping(['apple', 'banana', 'orange'])
print(len(shop))


#__add__ example

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)