# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите \
# в неё первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])
    if len(str_number) > 1:
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите \
# первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0: # условие, если на конце числа стоит '0', чтобы его исключить
            first = 1 # присвоение последнему элементу в 'str_number' значение '1', так как при умножении на '1' произведение не меняется
            return first
        else:
            return first

result_1 = get_multiplied_digits(40203)
print(result_1)
result_2 = get_multiplied_digits(251000)
print(result_2)