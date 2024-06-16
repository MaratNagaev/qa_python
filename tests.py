import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_add_new_book(self, books_collector):
        books_collector.add_new_book('Book 1')
        assert "Book 1" in books_collector.books_genre

    def test_add_new_book_with_invalid_name_false(self, books_collector):
        assert not books_collector.add_new_book("Book 1" * 41)

    @pytest.mark.parametrize('name, genre', [['Book 1', 'Фантастика']])
    def test_set_book_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre

    def test_set_book_genre_with_invalid_genre_false(self, books_collector):
        books_collector.add_new_book("Book 1")
        assert not books_collector.set_book_genre("Book 1", "Романтика")

    def test_get_book_genre(self, books_collector):
        books_collector.add_new_book("Book 1")
        books_collector.set_book_genre("Book 1", "Фантастика")
        assert books_collector.get_book_genre("Book 1") == "Фантастика"

    @pytest.mark.parametrize('name, genre', [['Book 1', 'Фантастика'], ['Book 2', 'Ужасы']])
    def test_get_books_with_specific_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == [name]

    @pytest.mark.parametrize('name, genre', [['Book 1', 'Фантастика'], ['Book 2', 'Ужасы']])
    def test_get_books_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_genre() == {name: genre}

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Book 1")
        books_collector.add_new_book("Book 2")
        books_collector.set_book_genre("Book 1", "Фантастика")
        books_collector.set_book_genre("Book 2", "Ужасы")
        assert 'Book 2' not in books_collector.get_books_for_children()

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Book 1")
        books_collector.add_book_in_favorites("Book 1")
        assert "Book 1" in books_collector.favorites

    def test_add_book_in_favorites_with_invalid_book_false(self, books_collector):
        assert not books_collector.add_book_in_favorites("Book 4")

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Book 1")
        books_collector.add_book_in_favorites("Book 1")
        books_collector.delete_book_from_favorites("Book 1")
        assert "Book 1" not in books_collector.favorites

    @pytest.mark.parametrize('name', ['Book 1', 'Book 2'])
    def test_get_list_of_favorites_books(self, books_collector, name):
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        assert books_collector.favorites
