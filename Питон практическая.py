import os
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self._name = name 

    @abstractmethod  # Делаем метод абстрактным
    def show_info(self): 
        pass

class Librarian(User):
    def show_info(self): 
        #полиморфизм1
        print("Библиотекарь: " + self._name)

class Member(User):
    def __init__(self, name, borrowed_books=None):
        User.__init__(self, name)
        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books
    
    def show_info(self): 
        #полиморфизм2
        books_string = ", ".join(self.borrowed_books)
        print("Пользователь: " + self._name + " | Книги: " + books_string)


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def load_data(self):
        if os.path.exists("books.txt"):
            file = open("books.txt", "r", encoding="utf-8")
            for line in file:
                parts = line.strip().split("|")
                book_data = {
                    "name": parts[0], 
                    "author": parts[1], 
                    "status": parts[2]
                }
                self.books.append(book_data)
            file.close()
            
        if os.path.exists("users.txt"):
            file = open("users.txt", "r", encoding="utf-8")
            for line in file:
                parts = line.strip().split("|")
                name = parts[0]
                if parts[1]:
                    user_books = parts[1].split(",")
                else:
                    user_books = []
                self.members.append(Member(name, user_books))
            file.close()

    def save_data(self):
        file = open("books.txt", "w", encoding="utf-8")
        for book in self.books:
            file.write(book["name"] + "|" + book["author"] + "|" + book["status"] + "\n")
        file.close()
        
        file = open("users.txt", "w", encoding="utf-8")
        for member in self.members:
            books_string = ",".join(member.borrowed_books)
            file.write(member._name + "|" + books_string + "\n")
        file.close()

    def add_book(self):
        name = input("Название: ")
        author = input("Автор: ")
        self.books.append({"name": name, "author": author, "status": "доступна"})
    
    def remove_book(self):
        title = input("Название для удаления: ")
        new_list = []
        for book in self.books:
            if book["name"] != title:
                new_list.append(book)
        self.books = new_list

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
                current_user.show_info() # Используем метод полиморфизма для вывода
        else:
            print("Пользователь не найден.")
