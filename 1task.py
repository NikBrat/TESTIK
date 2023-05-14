def check(af):
    opr = ['+', '-', ':', '*']
    for i in range(4):
        if af.find(opr[i]) == 0:
            print('Не введено первое число')
            return
        if af.find(opr[i]) == len(af) - 2:
            print('Не введено второе число/знак (=)')
            return
        if opr[i] not in af:
            opr[i] = 0
        else:
            opr[i] = 1
    if not sum(opr) == 1:
        print('Неверно введена арифметическая операция')
        return
    get_numbers(af)


def summa(eql):
    nb = [int(i) for i in eql.split('+')]
    return sum(nb)


def raznost(eql):
    nb = [int(i) for i in eql.split('-')]
    return nb[0] - nb[1]


def mult(eql):
    nb = [int(i) for i in eql.split('*')]
    return nb[0] * nb[1]


def dived(dg1, dg2):
    if dg2 == 0:
        return 'Нельзя делить на 0. Введите другой делитель'
    return f'Результат: {dg1 / dg2}'


def get_numbers(eql):
    eql = eql[:-1]
    if '+' in eql:
        print(f'Результат: {summa(eql)}')
    elif '-' in eql:
        print(f'Результат: {raznost(eql)}')
    elif ':' in eql:
        nb = [int(i) for i in eql.split(':')]
        print(dived(nb[0], nb[1]))
    elif '*' in eql:
        print(f'Результат: {mult(eql)}')


def cod():
    print('Калькулятор открыт')
    print('Доступные операции: +, -, *, :')
    a = input('Введите ваш пример по образцу (77+13=):\n')
    try:
        check(a)
    except ValueError:
        print('Неправильно введено выражение')


if __name__ == "__main__":
    while True:
        cod()
        if input("Хотите продолжить? (Y/N)\n").strip().upper() != 'Y':
            break
