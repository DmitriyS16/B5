def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

greet()
field = [[" "] * 3 for i in range(3)]
def show():
    print(f"   0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f" {i} {row_info}")

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["x", "x", "x"]:
            print("Победил крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил нолик!!!")
            return True
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["x", "x", "x"]:
            print("Победил крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил нолик!!!")
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ["x", "x", "x"]:
            print("Победил крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил нолик!!!")
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["x", "x", "x"]:
        print("Победил крестик!!!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Победил нолик!!!")
        return True
    return False

def ask():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите две координаты!")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите 2 числа!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапазона!")
            continue
        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y

count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break
