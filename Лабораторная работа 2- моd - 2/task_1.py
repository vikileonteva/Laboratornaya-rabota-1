BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """Класс для инициализации книги по трем параметрам"""
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'

class Library:

    def __init__ (self, books=list()):
        self.books = books

    def get_next_book_id(self):
        if self.books is []:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id_:int):
        for book in self.books:
            if book.id_ is id_:
                return self.books.index(book)
            else:
                raise ValueError("Книги с запрашиваемым id не существует")

# TODO написать класс Book


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
