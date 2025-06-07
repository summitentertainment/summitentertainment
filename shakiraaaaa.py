exam_results = {
    "Иванов": 4,
    "Петрова": 5,
    "Смирнова": 3,
    "Попова": 5,
    "Сергеев": 2,
    "Козлова": 4,
    "Николаев": 3
}

def средний_балл():
    return sum(exam_results.values()) / len(exam_results)

def отличники():
    return [name for name, mark in exam_results.items() if mark == 5]

def отстающие():
    return [name for name, mark in exam_results.items() if mark < 3]

def распределение():
    d = {}
    for mark in exam_results.values():
        d[mark] = d.get(mark, 0) + 1
    return d

# Примеры:
print("Средний балл:", средний_балл())
print("Отличники:", отличники())
print("Отстающие:", отстающие())
print("Распределение:", распределение())
