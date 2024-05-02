import pytest
from conftest import books_collector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, books_collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(books_collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_set_genre(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', 'Фантастика')
        assert books_collector.get_book_genre('Harry Potter') == 'Фантастика'

    def test_get_book_genre_add_new_book_with_empty_genre(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', '')
        assert books_collector.get_book_genre('Harry Potter') == ''

    def test_get_books_with_specific_genre_get_book_name_of_specific_genre(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Harry Potter']

    def test_get_books_genre_is_positive(self, books_collector):
        books_collector.add_new_book('Harry Potter')
        books_collector.set_book_genre('Harry Potter', 'Фантастика')
        assert books_collector.get_books_genre() == {'Harry Potter': 'Фантастика'}

    def test_get_books_for_children_get_books_without_age_rating(self, books_collector):
        books_collector.add_new_book('Paw Patrol')
        books_collector.add_new_book('Saw')
        books_collector.set_book_genre('Paw Patrol', 'Мультфильмы')
        books_collector.set_book_genre('Saw', 'Ужасы')
        assert books_collector.get_books_for_children() == ['Paw Patrol']

    def test_add_book_in_favorites_is_positive(self, books_collector):
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        assert books_collector.get_list_of_favorites_books() == ['Book1']

    def test_delete_book_from_favorites_book_is_deleted_from_favorites(self, books_collector):
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        books_collector.delete_book_from_favorites('Book1')
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_book_to_favorites(self, books_collector):
        books_collector.add_new_book('Book1')
        books_collector.add_book_in_favorites('Book1')
        assert books_collector.get_list_of_favorites_books() == ['Book1']

    def test_add_new_book_invalid_name(self, books_collector):
        books_collector.add_new_book('')
        assert '' not in books_collector.books_genre

    @pytest.mark.parametrize('name, genre', [['Война и мир', 'Роман'], ['Гарри Поттер', 'Приключения']])
    def test_set_book_genre_invalid_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_nonexistent_genre(self, books_collector):
        books_collector.add_new_book('Book1')
        books_collector.set_book_genre('Book1', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Роман') == []
