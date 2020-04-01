count = 0
date_s = 0

f = open('sport.txt', 'w', encoding='utf-8')
for i in range(30):
    if count % 2 == 0:
        date_s += 1
        f.write('\n')
        f.write(f'{date_s} апреля 2020' + '\n' + '\n')
        f.write('Приседания 120' + '\n')
        f.write('3 задания английский' + '\n')
        f.write('Прогулка 10к шагов минимум' + '\n')
        f.write('Повороты 200' + '\n')
        f.write('Повороты с палкой 200' + '\n')
        f.write('Колени вверх 80-80' + '\n')
        f.write('Шея 30-30' + '\n')
        f.write('Руки в стороны 200' + '\n')
        f.write('Планка со сменой рук 60' + '\n')
        f.write('Наклоны 120' + '\n')
        f.write('Пресс 70' + '\n')
        f.write('Битцепс 60' + '\n')
        count += 1
        f.write('\n')

    elif count % 2 != 0:
        date_s += 1

        f.write('\n')
        f.write(f'{date_s} апреля 2020' + '\n' + '\n')
        f.write('Приседания 120' + '\n')
        f.write('3 задания английский' + '\n')
        f.write('Прогулка 10к шагов минимум' + '\n')
        f.write('Повороты 200' + '\n')
        f.write('Повороты с палкой 200' + '\n')
        f.write('Колени вверх 80-80' + '\n')
        f.write('Шея 30-30' + '\n')
        f.write('Руки в стороны 200' + '\n')
        f.write('Планка 70- 70 - 70 -70' + '\n')
        f.write('Наклоны 120' + '\n')
        f.write('Трицепс 80' + '\n')
        count += 1
        f.write('\n')