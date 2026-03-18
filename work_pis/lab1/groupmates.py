# -*- coding: utf-8 -*-

groupmates = [
    {
        "name": u"Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print u"Имя студента".ljust(15),
    print u"Группа".ljust(8),
    print u"Возраст".ljust(8),
    print u"Оценки".ljust(20)
    for student in students:
        print student["name"].ljust(15),
        print student["group"].ljust(8),
        print str(student["age"]).ljust(8),
        print str(student["marks"]).ljust(20)
    print "\n"

def filter_by_avg_mark(students, min_avg):
    """
    Возвращает список студентов, у которых средний балл >= min_avg.
    """
    filtered = []
    for s in students:
        avg = sum(s["marks"]) / float(len(s["marks"]))
        if avg >= min_avg:
            filtered.append(s)
    return filtered

# Пример использования
print_students(groupmates)
good_students = filter_by_avg_mark(groupmates, 4.0)
print u"Студенты со средним баллом >= 4.0:"
print_students(good_students)
