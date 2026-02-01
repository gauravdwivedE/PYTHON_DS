'''
Learning Python Class 21: Advanced OOP Concepts
constructor
'''
class Factory:
    # Constructor method to initialize the object
    def __init__(self, material, ram, storage):
        self.material = material
        self.ram = ram
        self.storage = storage

    def show_details(self):
        print(f'Material: {self.material}, RAM: {self.ram}, Storage: {self.storage}')

m1 = Factory('Plastic', '8GB', '256GB')

m1.show_details()