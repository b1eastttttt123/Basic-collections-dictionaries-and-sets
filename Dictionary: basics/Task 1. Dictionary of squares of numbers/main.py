number = int(input("Введите любое число: "))

result = {num : num * num for num in range(1, number + 1)}

print(f"Результат: {result}")
