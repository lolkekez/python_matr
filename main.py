if __name__ == '__main__':
    matr_y = []
    while True:  # юзер вводит матрицу
        element = input().split()
        element_in_int = []
        for i in element:
            if i != "end":
                element_in_int.append(int(i))

        matr_y.append(element_in_int)
        if element[-1] == "end":
            break


    for i in range(0, len(matr_y)):  # преобразовали числа в int
        for j in range(0, int(len(matr_y[0]))):
            matr_y[i][j] = int(matr_y[i][j])

    matr_x = [[int(0) for j in range(len(matr_y[0]))] for i in range(len(matr_y))]  # сделали копию матрицы
    for i in range(len(matr_x)):
        for j in range(len(matr_x[0])):
            matr_x[i][j] = matr_y[i][j]

    for i in range(0, len(matr_y)):  # делаю преобразования матрицы
        for j in range(0, len(matr_y[0])):
            if i == 0 and j == 0:  # меняю первый квадрат
                matr_x[i][j] = matr_y[-1][0] + matr_y[0][-1] + matr_y[0][j + 1] + matr_y[i + 1][j]
            elif i == 0 and j != 0 and j != len(matr_y[0]) - 1:  # меняю квадарты 1 строки (не первый и не последний)
                matr_x[i][j] = matr_y[i + 1][j] + matr_y[-1][j] + matr_y[i][j + 1] + matr_y[i][j - 1]
            elif i == 0 and j == len(matr_y[0]) - 1:  # меняю квадрат первой строки последний столбец
                matr_x[i][j] = matr_y[0][0] + matr_y[i + 1][j] + matr_y[i][j - 1] + matr_y[-1][-1]
            elif j == 0 and i != 0 and i != len(matr_y) - 1:  # меняю квардраты первого столбца (не первый и не последний)
                matr_x[i][j] = matr_y[i - 1][j] + matr_y[i + 1][j] + matr_y[i][-1] + matr_y[i][j + 1]
            elif i == len(matr_y) - 1 and j == 0:  # меняю послединй квадрат первого столбца последней строки
                matr_x[i][j] = matr_y[i][j + 1] + matr_y[i - 1][j] + matr_y[0][0] + matr_y[-1][-1]
            elif i == len(matr_y) - 1 and j != 0 and j != len(matr_y[0]) - 1:  # меняю квадраты последней строки (не первый и не последний)
                matr_x[i][j] = matr_y[i - 1][j] + matr_y[i][j - 1] + matr_y[i][j + 1] + matr_y[0][j]
            elif i == len(matr_y) - 1 and j == len(matr_y[0]) - 1:  # меняю самый последний квадрат
                matr_x[i][j] = matr_y[i - 1][j] + matr_y[i][j - 1] + matr_y[0][j] + matr_y[i][0]
            elif j == len(matr_y[0]) - 1 and i != 0 and i != len(matr_y):  # меняю квадраты последнего столбца (не первая и не последняя строка)
                matr_x[i][j] = matr_y[i-1][j] + matr_y[i+1][j] + matr_y[i][0] + matr_y[i][j-1]
            else:
                matr_x[i][j] = matr_y[i-1][j] + matr_y[i+1][j] + matr_y[i][j-1] + matr_y[i][j+1]


#Выводим матрицу:
    for i in range(0,len(matr_y)):
        for j in range (0, len(matr_y[0])):
            print((matr_x[i][j]), end=" ")
        print()
