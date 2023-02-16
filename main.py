#задача 1
pas1 = input("")
pas2 = input("")
if pas1 == pas2:
    print("Пароль принят")
else:
    print("Пароль не принят")

#Задача 1.2 усложнённая
pas = input("Введите пароль: ")
if len(pas) < 6:
    print("Пароль слишком короткий")
elif pas[0:7] == "qwerty":
    print("Ненадёжный пароль")
else:
    print("ОК")

#Задача 2
mesto = int(input(""))
if mesto in range (1, 36):
    if mesto % 2 == 0:
        print("Верхнее место в купе")
    else:
        print("Место нижнее в купе")
if mesto in range (37,54):
    if mesto % 2 == 0:
        print("Боковое верхнее")
    else:
        print("Боковое нижнее")
#Задача 3
year = int(input(""))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

#Задача 4
vvod1 = input("Введите цвет (синий, красный, жёлтый ")
vvod2 = input("Введите цвет (синий, красный, жёлтый ")
if vvod1 == "красный" and vvod2 == "синий" or vvod1 == "синий" and vvod2 == "красный":
    print("фиолетовый")
elif vvod1 == "красный" and vvod2 == "жёлтый" or vvod1 == "жёлтый" and vvod2 == "красный" :
    print("оранжевый")
elif vvod1 == "синий" and vvod2 == "жёлтый" or vvod1 == "жёлтый" and vvod2 == "красный":
    print("зелёный")
elif vvod1 or vvod2 != "красный" or "синий" or "жёлтый":
    print("Неправильный цвет")

#Задача 5
n = int(input("Введите"))
res = ''
for i in range (n):
    s = input()
    res = res+s+''
print(res)
