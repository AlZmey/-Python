books = int(input('Введите количество купленных книг за месяц: '))
if books == 0:
    print('Вы ничего не купили, очки не заработаны')
if books == 2:
    print('Количество очков: 5')
if books == 4:
    print('Количество очков: 15')
if books == 6:
    print('Количество очков: 15')
if books >=8:
    print('Количество очков: 60')