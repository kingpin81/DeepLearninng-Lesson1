import numpy as np
from functools import reduce

# 1) Подсчитать произведение ненулевых элементов на диагонали прямоугольной
# матрицы. Для X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]), ответ: 3.

# matrix = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
matrix = np.random.randint(0, 5, (10, 10))
# print(matrix)

# 1. First way
def getContOriginal():
    list_res = []

    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if i == j and column != 0:
                list_res.append(column);

    if len(list_res) > 0:
        result = 1;
        for i in list_res:
            result *= i;
    else:
        result = 0;

    return result

#%timeit resul1t = getContOriginal()
print(getContOriginal())

# 2. With numpy
def getContNumpy():
    list_res = np.diagonal(matrix)
    list_res = list_res[(list_res != 0)]

    if len(list_res) > 0:
        result = reduce(lambda x, y: x * y, list_res)
    else:
        result = 0;

    return result

#%timeit resul1t = getContNumpy()
print(getContNumpy())