red = 'красный'
blue = 'синий'
yellow = 'желтый'
cvet1 = str(input('Введите красный / синий / желтый'))
cvet2 = str(input('Введите красный / синий / желтый'))

if cvet1 != red and cvet1 != blue and cvet1 != yellow:
    print('Цвет1 отличен от красного / синего / желтого')
if cvet2 != red and cvet2 != blue and cvet2 != yellow:
    print('Цвет2 отличен от красного / синего / желтого')
else:
    if cvet1 == red and cvet2 == blue:
        print('Фиолетовый')
    elif cvet1 == red and cvet2 == yellow:
        print('Оранжевый')
    elif cvet1 == blue and cvet2 == yellow:
        print('Зеленый')
