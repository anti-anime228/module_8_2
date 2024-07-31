def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'В numbers записан некорректный тип данных {number}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_result, incorrect_data = personal_sum(numbers)
        average = sum_result / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    return average


numbers_1 = "1, 2, 3"
numbers_2 = [1, "Строка", 3, "Ещё Строка"]
numbers_3 = 567
numbers_4 = [42, 15, 36, 13]
print(f'Результат 1: {calculate_average(numbers_1)}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average(numbers_2)}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(numbers_3)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average(numbers_4)}')  # Всё должно работать
