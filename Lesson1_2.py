import numpy as np

# 2) Дана матрица X и два вектора одинаковой длины i_idx и j_idx. Построить вектор
# np.array([X[i_idx[0], j_idx[0]], X[i_idx[1], j_idx[1]], . . . , X[i_idx[N-1], j_idx[N-1]]]). Для
# X = np.array(range(4 * 5)).reshape(4, 5) + 1, i_idx = np.array([1, 3, 0, 2]), j_idx =
# np.array([0, 2, 3, 1]) ответ: [ ​6 18 4 12]

i_idx = np.array([1, 3, 0, 2])
j_idx = np.array([0, 2, 3, 1])
X = np.array(range(4 * 5)).reshape(4, 5) + 1

# 1. First way
def getVectorOriginal():
    Y = np.array([], dtype=int)
    for i, column in enumerate(i_idx):
        Y = np.append(Y,  X[i_idx[i], j_idx[i]])

    return Y

# %timeit resul1t = getVectorOriginal()
print(getVectorOriginal())


# 2. With numpy
def getVectorNumpy():
    iterable = (X[i_idx[i], j_idx[i]] for i in range(len(i_idx)))
    return np.fromiter(iterable, dtype=int)

# %timeit resul1t = getVectorNumpy()
print(getVectorNumpy())