import string
import random
from datetime import datetime
import json 
from pathlib import Path

from numpy import dtype
class Library:

    file_name = "data.json"
    data = {"books":[], "members":[]}
    if Path(file_name).exists():
        with open (file_name, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)

    @classmethod
    def save_data (cls):
        try:
            with open (cls.file_name, "w") as f:
                json.dump(cls.data, f, indent=4)
                print(" ------  Data has been saved successfully ------")
        except Exception as e:
            print("Error saving data:", e)

    @classmethod
    def gen_id(cls, prefix = "B"):
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

    def add_member(self):

        name = input("Enter member's name ")
        email = input("Enter member's email ")
    
        member = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed_books": [],
            "created_at":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
    
        Library.data["members"].append(member)
        Library.save_data()
    
    def get_members(self):
        print("-"*35)

        if not Library.data["members"]:
            print("No member found")
            return 
        print(f"{len(Library.data["members"])} Member{'s' if len(Library.data["members"]) > 1  else  '' } found")    
        for item in Library.data['members']:

            print("Member id.   : ", item['id'])
            print("Member name  : ",item['name'])
            print("Member email: ",item['email'])
            print("Borrowed books : ",item['borrowed_books'])
            print("Joined date : ",item['created_at'])

            print("-"*35)

    def borrow_book(self):
        member_id = input("Enter member's valid id")
        members_data = Library.data["members"]
        #print(members_data)
        member = next(filter(lambda m: m['id'] == member_id, members_data), None)

        if not member:
            print("No such member found")
            return

        book_id = input("Enter book's valid id")
        books_data = Library.data["books"]

        book = next(filter(lambda b: b['id'] == book_id, books_data), None)

        if not book:
            print("No such book found")
            return
        elif book['available_stock'] <= 0:
            print("No books are available to be borrowed")
            return

        borrow_data = {
            "id": book_id,
            "name": book['name'],
            "borrowed_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        member['borrowed_books'].append(borrow_data)


        # print(book['available_stock'])

        book['available_stock']  -= 1

        Library.save_data()
        
    def return_book(self):
        member_id = input("Enter member's valid id")
        members_data = Library.data["members"]
        #print(members_data)
        member = next(filter(lambda m: m['id'] == member_id, members_data), None)

        if not member:
            print("No such member found")
            return

        book_id = input("Enter book's valid id")
        books_data = Library.data["books"]

        book = next(filter(lambda b: b['id'] == book_id, books_data), None)

        if not book:
            print("No such book found")
            return
        
        elif not member['borrowed_books']:
            print("No  book borrowed")
            return
        

        book['available_stock'] +=1

        books_after_return = filter(lambda m: m['id'] != book_id, member['borrowed_books'])

        member["borrowed_books"] = list(books_after_return)

        Library.save_data()

    
print("-"*50)
print("Welcome to the Library Management System")
print("-"*50)



# library managrment system
# Features ->

print("Press 1 to add a book")
print("Press 2 to display all books")
print("Press 3 to add a member")
print("Press 4 to display all members")
print("Press 5 to borrow a book")
print("Press 6 to return a book")
print("Press e to exit")

c = int(input("Press here  -  "))

if(c == 1):
    l1 = Library()
    l1.create_book()

if(c == 2):
    l1 = Library()
    books = l1.get_books()
    

if(c == 3):
    l1 = Library()
    books = l1.add_member()
        
if(c == 4):
    l1 = Library()
    books = l1.get_members()
if (c == 5):
    l1 = Library()
    l1.borrow_book()

if (c == 6):
    l1 = Library()
    l1.return_book()
    
print("-"*50)
