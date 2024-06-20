import pytest

c = 0


@pytest.fixture(autouse=True)
def clean_test_file():
    with open('tests/testfile.txt', 'w'):
        global c
        c += 1
        print(c)
        pass
