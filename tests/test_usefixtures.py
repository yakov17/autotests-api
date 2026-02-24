import pytest

@pytest.fixture
def clear_books_database():
    print('[FIXTURE] Clearing Books Database')

@pytest.fixture
def fill_books_database():
    print('[FIXTURE] Filling Books Database')

@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:
    def test__read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...