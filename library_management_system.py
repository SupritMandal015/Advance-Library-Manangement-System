import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author,
            "issued_to": None
        })
        self.save_books()

    def get_all_books(self):
        return self.books

    def issue_book(self, title, user):
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["issued_to"]:
                book["issued_to"] = user
                self.save_books()
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and book["issued_to"]:
                book["issued_to"] = None
                self.save_books()
                return True
        return False

    def search_books(self, keyword):
        return [
            book for book in self.books
            if keyword.lower() in book["title"].lower()
        ]

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.library = Library()

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="📚 Library Management System", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(self.root, text="Add Book", width=30, command=self.add_book).pack(pady=5)
        tk.Button(self.root, text="View All Books", width=30, command=self.view_books).pack(pady=5)
        tk.Button(self.root, text="Issue Book", width=30, command=self.issue_book).pack(pady=5)
        tk.Button(self.root, text="Return Book", width=30, command=self.return_book).pack(pady=5)
        tk.Button(self.root, text="Search Book", width=30, command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Exit", width=30, command=self.root.quit, bg="red", fg="white").pack(pady=15)

    def add_book(self):
        title = simpledialog.askstring("Add Book", "Enter book title:")
        author = simpledialog.askstring("Add Book", "Enter author name:")
        if title and author:
            self.library.add_book(title, author)
            messagebox.showinfo("Success", f"✅ Book '{title}' added.")

    def view_books(self):
        books = self.library.get_all_books()
        if not books:
            messagebox.showinfo("Books", "No books available.")
            return
        book_list = "\n".join(
            f"- {b['title']} by {b['author']} ({'Issued to ' + b['issued_to'] if b['issued_to'] else 'Available'})"
            for b in books
        )
        messagebox.showinfo("All Books", book_list)

    def issue_book(self):
        title = simpledialog.askstring("Issue Book", "Enter book title:")
        user = simpledialog.askstring("Issue Book", "Enter your name:")
        if title and user:
            success = self.library.issue_book(title, user)
            if success:
                messagebox.showinfo("Success", f"📖 Book '{title}' issued to {user}.")
            else:
                messagebox.showerror("Unavailable", f"❌ Book '{title}' not available or already issued.")

    def return_book(self):
        title = simpledialog.askstring("Return Book", "Enter book title:")
        if title:
            success = self.library.return_book(title)
            if success:
                messagebox.showinfo("Success", f"✅ Book '{title}' returned.")
            else:
                messagebox.showerror("Error", f"❌ Book '{title}' was not issued.")

    def search_books(self):
        keyword = simpledialog.askstring("Search Book", "Enter keyword:")
        if keyword:
            results = self.library.search_books(keyword)
            if results:
                result_text = "\n".join(
                    f"- {b['title']} by {b['author']} ({'Issued to ' + b['issued_to'] if b['issued_to'] else 'Available'})"
                    for b in results
                )
                messagebox.showinfo("Search Results", result_text)
            else:
                messagebox.showinfo("Not Found", "No books matched your search.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = LibraryApp(root)
    root.mainloop()
