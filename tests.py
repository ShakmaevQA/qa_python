import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["1984", "Гарри Поттер", "Преступление и наказание"])
    def test_add_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_duplicate_book(self, collector):
        collector.add_new_book("1984")
        collector.add_new_book("1984")
        assert len(collector.get_books_genre()) == 1

    def test_add_book_with_long_name(self, collector):
        long_name = "a" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ("1984", "Фантастика"),
        ("Гарри Поттер", "Мультфильмы"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("1984", "Фантастика"),
        ("Гарри Поттер", "Мультфильмы"),
        ("Шерлок Холмс", "Детективы")
    ])

    def test_get_books_genre(self, collector):
        books = {"1984": "Фантастика", "Гарри Поттер": "Мультфильмы", "Шерлок Холмс": "Детективы"}
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        assert collector.get_books_genre() == books

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["1984"]),
        ("Мультфильмы", ["Гарри Поттер"]),
        ("Детективы", ["Шерлок Холмс"])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        books = {"1984": "Фантастика", "Гарри Поттер": "Мультфильмы", "Шерлок Холмс": "Детективы"}
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        assert collector.get_books_with_specific_genre(genre) == expected_books

    @pytest.mark.parametrize("book_name, genre, expected", [
        ("1984", "Фантастика", True),
        ("Гарри Поттер", "Мультфильмы", True),
        ("Шерлок Холмс", "Детективы", False)
    ])
    def test_get_books_for_children(self, collector, book_name, genre, expected):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert (book_name in collector.get_books_for_children()) == expected

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        collector.delete_book_from_favorites("1984")
        assert "1984" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        books = ["1984", "Гарри Поттер", "Шерлок Холмс"]
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == books