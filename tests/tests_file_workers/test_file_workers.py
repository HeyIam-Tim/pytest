from my_funcs.file_workers import read_from_workers


def append_test_data(test_data):
    with open('tests/testfile.txt', 'a') as f:
        f.writelines(test_data)


def test_read_from_file():
    test_data = ['adffdf\n', 'werq\n', 'asd\n']
    append_test_data(test_data=test_data)

    data = read_from_workers('tests/testfile.txt')
    assert data == test_data


def test_read_from_file2():
    test_data = ['adffdf\n', 'werq\n', 'asd\n', 'asdfa']
    append_test_data(test_data=test_data)

    data = read_from_workers('tests/testfile.txt')
    assert data == test_data
