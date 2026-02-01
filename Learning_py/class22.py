'''
class methos in Python:
1. Instance method
2. Class method
3. Static method
4. Constructor
'''


class Factory:

    material = 'Plastic'  
    ram = '8GB'       
    storage = '256GB' 

    # Constructor method to initialize the object
    def __init__(self, material, ram, storage):
        self.material = material
        self.ram = ram
        self.storage = storage

    # Instance method
    def show_details(self):
        print(f'Material: {self.material}, RAM: {self.ram}, Storage: {self.storage}')

    # class method
    @classmethod
    def factory_info(cls):
        print(cls.material, cls.ram, cls.storage)
    
    # Static method
    @staticmethod
    def factory_policy():
        print("All products come with a 1-year warranty.")

m1 = Factory('Metal', '16GB', '512GB')

m1.show_details()
Factory.factory_info()
Factory.factory_policy()