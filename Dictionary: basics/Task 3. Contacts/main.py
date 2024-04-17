result = dict()
print('Текущие контакты на телефоне: \n<Пусто>')

while True:
    name = input('Введите имя: ')
    number_phone = int(input('Введите номер телефона: '))
    if name not in result:
        result[name] = number_phone
        print('Текущие контакты на телефоне: \n')
        for info in result:
            print(info, result[info])
    else:
        print('Ошибка: такое имя уже существует.')
        break

