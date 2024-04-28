from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', 'Фантастика')
        assert collector.get_book_genre('Harry Potter') == 'Фантастика'

    def test_get_book_genre_add_new_book_with_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', '')
        assert collector.get_book_genre('Harry Potter') == ''

    def test_get_books_with_specific_genre_get_book_name_of_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Harry Potter']

    def test_get_books_genre_is_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', 'Фантастика')
        assert collector.get_books_genre() == {'Harry Potter': 'Фантастика'}

    def test_get_books_for_children_get_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Paw Patrol')
        collector.add_new_book('Saw')
        collector.set_book_genre('Paw Patrol', 'Мультфильмы')
        collector.set_book_genre('Saw', 'Ужасы')
        assert collector.get_books_for_children() == ['Paw Patrol']

    def test_add_book_in_favorites_is_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        assert collector.get_list_of_favorites_books() == ['Book1']

    def test_delete_book_from_favorites_book_is_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        collector.delete_book_from_favorites('Book1')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        assert collector.get_list_of_favorites_books() == ['Book1']

    def test_add_new_book_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Роман')
        assert collector.get_book_genre('Book1') == ''

    def test_get_books_with_specific_genre_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []

