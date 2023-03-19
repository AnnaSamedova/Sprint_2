import pytest

book_1 = 'Гордость и предубеждение и зомби'
book_2 = 'Что делать, если ваш кот хочет вас убить'
book_rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#тестируемый класс
class TestBooksCollector:


    #test №1
    def test_add_new_book_add_two_books(self, create_book_collector, add_two_books):
        collector = add_two_books
        assert len(collector.get_books_rating()) == 2

    #test №2
    def test_add_new_book_add_one_book_twice(self, create_book_collector):
        collector = create_book_collector
        collector.add_new_book(book_1)
        collector.add_new_book(book_1)
        assert len(collector.get_books_rating()) == 1

    #test №3
    @pytest.mark.parametrize('wrong_rating', [0, 11])
    def test_set_book_rating_within_range_less_1_and_more_10(self, wrong_rating, create_book_collector, add_book):
        collector = add_book
        collector.set_book_rating(book_1, wrong_rating)
        assert collector.get_book_rating(book_1) != wrong_rating

    #test №4
    @pytest.mark.parametrize('true_rating', book_rating)
    def test_set_book_rating_within_range_1_to_10(self, true_rating, create_book_collector, add_book):
        collector = add_book
        collector.set_book_rating(book_1, true_rating)
        assert collector.get_book_rating(book_1) == true_rating

    #test №5
    @pytest.mark.parametrize('true_rating', book_rating)
    def test_set_book_rating_book_is_not_dict(self, true_rating, create_book_collector):
        collector = create_book_collector
        collector.set_book_rating(book_1, true_rating)
        assert collector.get_book_rating(book_1) is None

    #test №6
    def test_add_book_in_favorites_add_two_books(self, create_book_collector, add_book):
        collector = add_book
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_2)
        assert len(collector.favorites) == 1

    #test №7
    def test_add_book_in_favorites_book_is_not_in_book_rating(self, create_book_collector):
        collector = create_book_collector
        collector.add_book_in_favorites(book_1)
        assert len(collector.favorites) == 0

    #test №8
    def test_add_book_in_favorites_add_one_book_twice(self, create_book_collector, add_book):
        collector = add_book
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_1)
        assert len(collector.favorites) == 1

    #test №9
    def test_delete_book_from_favorites_delete_one_book(self, create_book_collector, add_book):
        collector = add_book
        collector.add_book_in_favorites(book_1)
        collector.delete_book_from_favorites(book_1)
        assert len(collector.favorites) == 0

    #test №10
    def test_get_books_rating_get_book_dict(self, create_book_collector, add_two_books):
        collector = add_two_books
        assert collector.get_books_rating() == {book_1: 1, book_2: 1}

    #test №11
    def test_get_list_of_favorites_books_get_book_list(self, create_book_collector, add_two_books):
        collector = add_two_books
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_2)
        assert collector.get_list_of_favorites_books() == [book_1, book_2]

    #test №12
    def test_delete_book_from_favorites_book_is_not_in_favorites(self, create_book_collector, add_book):
        collector = add_book
        collector.add_book_in_favorites(book_1)
        collector.delete_book_from_favorites('book_2')
        assert len(collector.favorites) == 1

    #test №13
    def test_get_books_with_specific_rating_get_book_with_rating_6(self, create_book_collector, add_two_books):
        collector = add_two_books
        collector.set_book_rating(book_1, 3)
        collector.set_book_rating(book_2, 6)
        assert collector.get_books_with_specific_rating(6) == [book_2]