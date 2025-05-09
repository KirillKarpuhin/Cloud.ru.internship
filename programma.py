user_numbers = input("Введите числа через пробел: ")

# пустой список 
numbers = []

# ищем не числовые значения \\ user_numbers.split() делит на отдельные строки user_numbers
for str_num in user_numbers.split():
    try:
        numbers.append(int(str_num)) # к пустому списку добавляем числовые значение str_num из отдельных строк user_numbers.split
    except ValueError:
         print(f"Пропускаем нечисловое значение: '{str_num}'") # если вводимые символы не числа, то пропускаем


print("Четные числа:")
# четные числа
for num in numbers: 
    if num % 2 == 0:
        print(num)

# максимальное и минимальное число
max_number = max(numbers)
min_number = min(numbers)

print("Максимальное число: ", max_number)
print("Минимальное число: ", min_number)

# сортированный список по возрастанию 
sorted_num = [] # пустой список для хранения
while numbers:
    min_num = numbers[0] # первое число в списке является минимальным
    for num in numbers: # перебираем все числа в списке numbers
        if num < min_num:
            min_num = num     
    sorted_num.append(min_num) # добавляем минимальное число в список sorted_num
    numbers.remove(min_num) # удаляем минимальное число из списка numbers

print("Cписок в порядке возрастания:", sorted_num)