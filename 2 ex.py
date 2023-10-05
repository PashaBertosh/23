def extract_numbers(input_string):
    numbers = []
    current_number = ''

    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''

    if current_number:
        numbers.append(int(current_number))

    return numbers

input_string = input("Введите строку: ")

# Извлекаем числа из строки
numbers = extract_numbers(input_string)

# Выводим числа на экран
print("Извлеченные числа из строки:")
for number in numbers:
    print(number)
