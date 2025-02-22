summa_user = int(input('Введите сумму, выделенную Вам на один месяц: '))
prodolzaem = 'д'
nakopitel = 0
while prodolzaem == 'д':
    rashod = int(input('Введите сумму расходов: '))
    nakopitel = nakopitel + rashod
    prodolzaem = str(input('Продолжаем? д / н ?'))
if summa_user == nakopitel:
    print('Вышли в ноль, доходы равны расходам')
if summa_user > nakopitel:
    ostatok = summa_user - nakopitel
    print(f"Остаток", ostatok)
if summa_user < nakopitel:
    pererashod = summa_user - nakopitel
    print(f"Перерасход", pererashod)
