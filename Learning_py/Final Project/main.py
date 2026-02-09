import streamlit as st
import string
import random
from datetime import datetime
import json
from pathlib import Path

# ---------------- Library Class ---------------- #
class Library:
    file_name = "data.json"
    data = {"books": [], "members": []}

    if Path(file_name).exists():
        with open(file_name, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)

    @classmethod
    def save_data(cls):
        with open(cls.file_name, "w") as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def gen_id(cls, prefix="B"):
        return prefix + "-" + "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(5)
        )

    def create_book(self, name, author, stock):
        book = {
            "id": Library.gen_id(),
            "name": name,
            "author": author,
            "stock": stock,
            "available_stock": stock,
            "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
        Library.data["books"].append(book)
        Library.save_data()

    def add_member(self, name, email):
        member = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed_books": [],
            "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
        Library.data["members"].append(member)
        Library.save_data()

    def borrow_book(self, member_id, book_id):
        member = next((m for m in Library.data["members"] if m["id"] == member_id), None)
        book = next((b for b in Library.data["books"] if b["id"] == book_id), None)

        if not member or not book:
            return False, "Invalid member or book ID"

        if book["available_stock"] <= 0:
            return False, "No stock available"

        member["borrowed_books"].append({
            "id": book_id,
            "name": book["name"],
            "borrowed_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })
        book["available_stock"] -= 1
        Library.save_data()
        return True, "Book borrowed successfully"

    def return_book(self, member_id, book_id):
        member = next((m for m in Library.data["members"] if m["id"] == member_id), None)
        book = next((b for b in Library.data["books"] if b["id"] == book_id), None)

        if not member or not book:
            return False, "Invalid member or book ID"

        member["borrowed_books"] = [
            b for b in member["borrowed_books"] if b["id"] != book_id
        ]
        book["available_stock"] += 1
        Library.save_data()
        return True, "Book returned successfully"


# ---------------- Streamlit Setup ---------------- #
st.set_page_config(page_title="Library Management", layout="wide")
st.title("📚 Library Management System")

lib = Library()

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Add Book", "View Books", "Add Member", "View Members", "Borrow Book", "Return Book"]
)

# ---------------- Dashboard ---------------- #
if menu == "Dashboard":
    col1, col2, col3 = st.columns(3)

    col1.metric("📘 Total Books", len(Library.data["books"]))
    col2.metric("👥 Total Members", len(Library.data["members"]))
    borrowed = sum(len(m["borrowed_books"]) for m in Library.data["members"])
    col3.metric("📕 Borrowed Books", borrowed)

# ---------------- Add Book ---------------- #
elif menu == "Add Book":
    st.subheader("➕ Add New Book")
    with st.form("add_book"):
        name = st.text_input("Book Name")
        author = st.text_input("Author Name")
        stock = st.number_input("Stock Quantity", min_value=1, step=1)
        submit = st.form_submit_button("Add Book")

        if submit:
            lib.create_book(name, author, stock)
            st.success("Book added successfully!")

# ---------------- View Books ---------------- #
elif menu == "View Books":
    st.subheader("📖 Books Inventory")
    if Library.data["books"]:
        st.table(Library.data["books"])
    else:
        st.warning("No books available")

# ---------------- Add Member ---------------- #
elif menu == "Add Member":
    st.subheader("➕ Add Member")
    with st.form("add_member"):
        name = st.text_input("Member Name")
        email = st.text_input("Email Address")
        submit = st.form_submit_button("Add Member")

        if submit:
            lib.add_member(name, email)
            st.success("Member added successfully!")

# ---------------- View Members (Modern UI) ---------------- #
elif menu == "View Members":
    st.subheader("👥 Members")

    if not Library.data["members"]:
        st.warning("No members found")
    else:
        for m in Library.data["members"]:
            with st.container():
                st.markdown("---")
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"### 👤 {m['name']}")
                    st.write(f"**Id:** {m['id']}")
                    st.write(f"📧 **Email:** {m['email']}")
                    st.write(f"🕒 **Joined:** {m['created_at']}")

                with col2:
                    st.metric("Borrowed", len(m["borrowed_books"]))

                st.write("📚 **Borrowed Books:**")
                if m["borrowed_books"]:
                    for b in m["borrowed_books"]:
                        st.markdown(
                            f"- **{b['name']}** _(Borrowed on {b['borrowed_date']})_"
                        )
                else:
                    st.info("No books borrowed")

# ---------------- Borrow Book ---------------- #
elif menu == "Borrow Book":
    st.subheader("📕 Borrow Book")
    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Borrow"):
        success, msg = lib.borrow_book(member_id, book_id)
        st.success(msg) if success else st.error(msg)

# ---------------- Return Book ---------------- #
elif menu == "Return Book":
    st.subheader("📗 Return Book")
    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Return"):
        success, msg = lib.return_book(member_id, book_id)
        st.success(msg) if success else st.error(msg)
