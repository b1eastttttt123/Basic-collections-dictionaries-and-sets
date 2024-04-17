students_info_enter = input(
    "Введите информацию о студенте через пробел\n"
    "(имя, фамилия, город, место учёбы, оценки): "
)

students_info = students_info_enter.split()
student = dict()

student["Имя"] = students_info[0]
student["Фамилия"] = students_info[1]
student["Город"] = students_info[2]
student["Место учёбы"] = students_info[3]
student["Оценки"] = []

for estimation in students_info[4:]:
    student["Оценки"].append(int(estimation))

for result in student:
    print(result, "-", student[result])
