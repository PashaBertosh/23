string = 'Enjoy every moment'

char_count = {}  # Инициализация пустого словаря

for char in string:
    if char != ' ':  # Игнорируем пробелы
        char_count[char] = char_count.get(char, 0) + 1

print(char_count)
