'''
Objects - objects are instances of classes. A class is a blueprint for creating objects.
          It defines a set of attributes and methods that the created objects will have.
'''

class Factory:
    order = 500

    def create_product(s):
        print("Mobile phone has been created")


m1 = Factory()  # Creating an object of the Factory class
m1.create_product()  # Calling the create_product method on the object

Factory.order = 4000
print(Factory.order)  # Accessing the order attribute of the class directly
