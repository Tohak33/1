import os
import pickle
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self._name = name 

    @abstractmethod
    def show_info(self): 
        pass

class Librarian(User):
    def show_info(self): 
        print("Библиотекарь: " + self._name)

class Member(User):
    def __init__(self, name, borrowed_books=None):
        User.__init__(self, name)
        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books
    
    def show_info(self): 
        books_string = ", ".join(self.borrowed_books)
        print("Пользователь: " + self._name + " | Книги: " + books_string)

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def load_data(self):
        if os.path.exists("library_data.pkl"):
            with open("library_data.pkl", "rb") as file:
                data = pickle.load(file)
                self.books = data.get("books", [])
                self.members = data.get("members", [])

    def save_data(self):
        with open("library_data.pkl", "wb") as file:
            data = {"books": self.books, "members": self.members}
            pickle.dump(data, file)

    def add_book(self):
        name = input("Название: ")
        author = input("Автор: ")
        self.books.append({"name": name, "author": author, "status": "доступна"})
    
    def remove_book(self):
        title = input("Название для удаления: ")
        book_to_find = None
        for book in self.books:
            if book["name"] == title:
                book_to_find = book
                break
        
        if book_to_find:
            self.books.remove(book_to_find)
            print("Книга удалена.")
        else:
            print("Книга не найдена.")

    def take_book(self, user):
        title = input("Название книги: ")
        for book in self.books:
            if book["name"] == title:
                if book["status"] == "доступна":
                    book["status"] = "выдана"
                    user.borrowed_books.append(title)
                    print("Книга взята.")
                else:
                    print("Книга уже занята.")
                return
        print("Книга не найдена.")

    def return_book(self, user):
        title = input("Название книги: ")
        if title in user.borrowed_books:
            for book in self.books:
                if book["name"] == title:
                    book["status"] = "доступна"
            user.borrowed_books.remove(title)
            print("Книга возвращена.")
        else:
            print("У вас нет такой книги.")

library = Library()

while True:
    print("\n1-Библиотекарь, 2-Пользователь, 0-Выход")
    role = input("Выберите роль: ")
    
    if role == "0":
        library.save_data()
        break
        
    if role == "1":
        print("\n[Меню библиотекаря]")
        act = input("1-Добавить, 2-Удалить, 3-Рег. юзера, 4-Все юзеры, 5-Все книги: ")
        if act == "1":
            library.add_book()
        elif act == "2":
            library.remove_book()
        elif act == "3":
            new_name = input("Имя пользователя: ")
            library.members.append(Member(new_name))
        elif act == "4":
            for member in library.members:
                member.show_info()
        elif act == "5":
            for book in library.books:
                print(book)
                
    elif role == "2":
        name = input("Введите ваше имя: ")
        current_user = None
        for m in library.members:
            if m._name == name:
                current_user = m
                
        if current_user:
            print("\n[Меню пользователя]")
            act = input("1-Доступные книги, 2-Взять, 3-Вернуть, 4-Мои книги: ")
            if act == "1":
                for book in library.books:
                    if book["status"] == "доступна":
                        print(book)
            elif act == "2":
                library.take_book(current_user)
            elif act == "3":
                library.return_book(current_user)
            elif act == "4":
                current_user.show_info()
        else:
            print("Пользователь не найден.")