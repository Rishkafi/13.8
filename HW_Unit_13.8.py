Tickets = int(input("Введите необходимое количество билетов "))
Summ = 0

for i in range(1, Tickets+1):
    Age = int(input("Введите возраст посетителя "))
    if Age < 18:
        print("Бесплатный вход")
    elif 18 <= Age < 25:
        Summ += 990
    elif Age >= 25:
        Summ += 1300

if Tickets >= 3:
    Summ *= 0.9
    print("Ваша скидка 10%")

print("---")
print("Общая сумма=", Summ)


