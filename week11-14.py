def draw_box():
    print("*" * 10)  # Верхняя граница
    for _ in range(12):  # 12 строк с боковыми границами
        print("*" + " " * 8 + "*")
    print("*" * 10)  # Нижняя граница


# Вызов функции
draw_box()


# 2
def draw_triangle():
    for i in range(1, 11):  # от 1 до 10 включительно
        print("*" * i)


# Вызов функции
draw_triangle()


# 3
def draw_triangle(fill, base):
    # Верхняя часть треугольника (до середины)
    for i in range(1, base // 2 + 2):
        print(fill * i)

    # Нижняя часть треугольника (после середины)
    for i in range(base // 2, 0, -1):
        print(fill * i)


# Примеры вызова:
draw_triangle("*", 9)
draw_triangle("+", 5)
draw_triangle("?", 7)
draw_triangle(".", 11)


# 4
def print_fio(name, surname, patronymic):
    # Получаем первые буквы фамилии, имени и отчества
    initials = surname[0].upper() + name[0].upper() + patronymic[0].upper()
    print(initials)


# Примеры вызова:
print_fio("Александр", "Пушкин", "Сергеевич")  # ПАС
print_fio("тимур", "Гуев", "ахсарбекович")  # ГТА
print_fio("Николай", "гоголь", "Васильевич")  # ГНВ
print_fio("светлана", "гергиева", "георгиевна")  # ГСГ


# 5
def print_digit_sum(num):
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    print(sum_digits)


# 6
def convert_to_miles(km):
    return km * 0.6214


# Примеры вызова:
print(convert_to_miles(1))  # 0.6214
print(convert_to_miles(5))  # 3.107
print(convert_to_miles(10))  # 6.214
print(convert_to_miles(1000))  # 621.4


# 7
def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


# Примеры вызова:
print(get_days(1))  # 31
print(get_days(2))  # 28
print(get_days(9))  # 30
print(get_days(12))  # 31


# 8
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# Примеры вызова:
print(get_factors(1))  # [1]
print(get_factors(5))  # [1, 5]
print(get_factors(10))  # [1, 2, 5, 10]
print(get_factors(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(
    get_factors(360)
)  # [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360]
print(get_factors(101))  # [1, 101]


# 9
def number_of_factors(num):
    return len(get_factors(num))


# Предполагая, что функция get_factors уже определена как:
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# Примеры вызова:
print(number_of_factors(1))  # 1
print(number_of_factors(5))  # 2
print(number_of_factors(10))  # 4
print(number_of_factors(36))  # 9
print(number_of_factors(360))  # 24
print(number_of_factors(10800))  # 60
print(number_of_factors(101))  # 2


# 10
def find_all(target, symbol):
    return [i for i, char in enumerate(target) if char == symbol]


# Примеры вызова:
print(find_all("abcdabcaaa", "a"))  # [0, 4, 7, 8, 9]
print(find_all("abcadbcaaa", "e"))  # []
print(find_all("abcadbcaaa", "d"))  # [4]
print(find_all("tttt", "t"))  # [0, 1, 2, 3]
print(find_all("ppooooopp", "p"))  # [0, 1, 7, 8]
print(find_all("ppooooopp", "o"))  # [2, 3, 4, 5, 6]
print(find_all("ppooppoopp", "o"))  # [2, 3, 6, 7]
# 11
