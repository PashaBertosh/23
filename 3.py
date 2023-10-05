def find_largest_odd(lst):
    largest_odd = float('-inf')  # Инициализация наибольшего нечетного элемента

    for num in lst:
        if num % 2 != 0 and num > largest_odd:
            largest_odd = num

    return largest_odd


def find_min_absolute(lst):
    min_absolute = float('inf')  # Инициализация минимального по модулю элемента

    for num in lst:
        if abs(num) < abs(min_absolute):
            min_absolute = num

    return min_absolute


if __name__ == "__main__":
    user_input = input("Введите одномерный целочисленный список, разделяя элементы пробелом: ")
    user_list = list(map(int, user_input.split()))

    if not user_list:
        print("Список пуст.")
    else:
        largest_odd = find_largest_odd(user_list)
        if largest_odd != float('-inf'):
            print("Наибольший нечетный элемент:", largest_odd)
        else:
            print("Нет нечетных элементов в списке.")

        min_absolute = find_min_absolute(user_list)
        print("Минимальный по модулю элемент:", min_absolute)
