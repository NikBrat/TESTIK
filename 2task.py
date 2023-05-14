import random

n = 10
field = [[0] * n for s in range(n)]
mines = int(input('Введите количество мин(число не может превышать 99!!!!):\n'))


def mines_location():
    global field
    global mines
    global n
    # Счётчик установленных мин
    count = 0
    while count < mines:
        # Генерируем рандомное число
        val = random.randint(0, n * n - 1)
        # находим строку и столбец
        r = val // n
        c = val % n
        # Располагаем мины
        if field[r][c] != '*':
            count = count + 1
            field[r][c] = '*'


def cells_val():
    global field
    global n

    for r in range(n):
        for c in range(n):

            if field[r][c] == '*':
                continue

            # Верхняя клетка
            if r > 0 and field[r - 1][c] == '*':
                field[r][c] = field[r][c] + 1
            # Нижняя клетка
            if r < n - 1 and field[r + 1][c] == '*':
                field[r][c] = field[r][c] + 1
            # Левая
            if c > 0 and field[r][c - 1] == '*':
                field[r][c] = field[r][c] + 1
            # Правая
            if c < n - 1 and field[r][c + 1] == '*':
                field[r][c] = field[r][c] + 1
            # Верхняя левая
            if r > 0 and c > 0 and field[r - 1][c - 1] == '*':
                field[r][c] = field[r][c] + 1
            # Верхняя правая
            if r > 0 and c < n - 1 and field[r - 1][c + 1] == '*':
                field[r][c] = field[r][c] + 1
            # Нижняя левая
            if r < n - 1 and c > 0 and field[r + 1][c - 1] == '*':
                field[r][c] = field[r][c] + 1
            # Нижняя правая
            if r < n - 1 and c < n - 1 and field[r + 1][c + 1] == '*':
                field[r][c] = field[r][c] + 1


def generator():
    mines_location()
    cells_val()


generator()
for i in range(n):
    print(field[i])
