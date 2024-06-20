def f1(value: str) -> str:
    """
        Реверс строки:
        Функция, которая принимает на вход строку и
        возвращает её обратно, т.е. перевернутую.
    """

    return value[::-1]


def f2(value: str) -> int:
    """
        Подсчет слов:
        Функция, которая принимает на вход строку
        и возвращает количество слов в этой строке.
    """

    words = value.split()
    return len(words)


def f3(numbers: list[int]) -> list[int]:
    """
        Сортировка списка:
        Функцию, которая принимает на вход список
        чисел и возвращает отсортированный по возрастанию список.
    """

    return sorted(numbers)


def f4(value: str) -> bool:
    """
    Проверка на палиндром:
    Функцию, которая принимает на вход строку и возвращает True,
    если строка является палиндромом (читается одинаково как с начала, так и с конца),
    и False в противном случае.
    """

    value = value.lower().replace(" ", "")
    # return value == f1(value=value)
    return value == value[::-1]


def f5(number: int) -> int:
    """
        Факториал числа:
        Функция, которая принимает на
        вход число и возвращает его факториал.
    """

    if number == 0:
        return 1
    else:
        return number * f5(number-1)


def f6(number_input: int) -> list[int]:
    """
        Генерация списка простых чисел:
        Функция, которая принимает на вход число n
        и возвращает список всех простых чисел до n.
    """

    primes = []
    for num in range(2, number_input):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# if __name__ == '__main__':
#     print(f1(value='adffs aadfa adf'))
#     print(f2(value='adf aadfa adf'))
#     print(f3(numbers=[3, 6, 3, 2, 8, 1, 0]))
#     print(f4(value='А роза упала на лапу Азора'))
#     print(f5(number=6))
#     print(f6(number_input=77))
