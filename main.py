#Вариант4
a = float(input("Введите первое число ")) #инициализируем переменную а и просим ввести ее значение.
b = float(input("Введите второе число ")) #инициализируем переменную b и просим ввести ее значение.
c = float(input("Введите третье число ")) #инициализируем переменную c и просим ввести ее значение.
if b > c and b > a: #условие через которое проверяется большее число.
    print(f"Число {b} большe {a} , {c}") #выводим самое большее число
elif a > b and a > c: #условие через которое проверяется большее число.
    print(f"Число {a} больше {c} , {b}") #выводим самое большее число
elif c > a and c > b: #условие через которое проверяется большее число.
    print(f"Число {c} больше {a} , {b}") #выводим самое большее число
elif a == b == c: #условие через которое проверяется равенство чисел.1
    print(f"Числа {a} , {b} , {c} равны")#выводим самое большее число
else: #иначе
    print(f"2 числа равны и 3 меньше этих двух") #выводим ситуацию