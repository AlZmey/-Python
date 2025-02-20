MONETA5 = 5
MONETA10 = 10
MONETA50 = 50
RUBL = 100

mon5 = int(input('Введите количество монет 5 копеек')) * MONETA5
mon10 = int(input('Введите количество монет 10 копеек')) * MONETA10
mon50= int(input('Введите количество монет 50 копеек')) * MONETA50

itog = mon5 + mon10 + mon50

if itog == RUBL:
    print('Получился РУБЛЬ')
else:
    print(f" Получилось {itog}")
