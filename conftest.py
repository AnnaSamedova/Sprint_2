import pytest
from main import BooksCollector

@pytest.fixture
def create_book_collector():
    new_book_collector = BooksCollector()
    return new_book_collector

@pytest.fixture
def add_book(create_book_collector):
    create_book_collector.add_new_book('Гордость и предубеждение и зомби')
    return create_book_collector

@pytest.fixture
def add_two_books(create_book_collector):
    create_book_collector.add_new_book('Гордость и предубеждение и зомби')
    create_book_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    return create_book_collector


