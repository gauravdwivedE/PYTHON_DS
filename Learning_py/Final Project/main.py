import string
import random
from datetime import datetime
import json 
from pathlib import Path
class Library:

    file_name = "data.json"
    data = {"books":[], "member":[]}
    if Path(file_name).exists():
        with open (file_name, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)

    @classmethod
    def save_data (cls):
        with open (cls.file_name, "w") as f:
          json.dump(cls.data, f, indent= 4)

    def gen_id(prefix = "B"):
        id = ""
        for i in range (5):
            id += random.choice(string.ascii_uppercase + string.digits)
        
        return prefix + "-" + id
    
    def create_book(self):
        name = input("Enter book name ")
        author = input("Enter author name ")
        stock = int(input("Enter stock quentity "))

        book = {
            "id": Library.gen_id(),
            "name": name,
            "author": author,
            "stock": stock,
            "available_stock": stock,
            "created_at":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        Library.data["books"].append(book)
        Library.save_data()

    def get_books(self):
        if not Library.data["books"]:
            print("No books found")
            return 
        for item in Library.data['books']:

            print("-"*25)
            print("Book id.   : ", item['id'])
            print("Book name  : ",item['name'])
            print("Book author: ",item['author'])
            print("Book stock : ",item['stock'])
            print("Available stock : ",item['available_stock'])

            print("-"*25)


print("-"*50)
print("Welcome to the Library Management System")
print("-"*50)



# library managrment system
# Features ->

print("Press 1 to add a book")
print("Press 2 to display all books")
print("Press 3 to search for a book")
print("Press 4 to delete a book")
print("Press 5 to add a member")
print("Press 6 to display all members")
print("Press 7 to borrow a book")
print("Press 8 to return a book")
print("Press e to exit")

c = int(input("Press here  -  "))

if(c == 1):
    l1 = Library()
    l1.create_book()

if(c == 2):
    l1 = Library()
    books = l1.get_books()
    
        
print("-"*50)
