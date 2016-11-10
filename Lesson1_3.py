import numpy as np
import collections

# 3) Даны два вектора x и y. Проверить, задают ли они одно и то же
# мультимножество. Для x = np.array([1, 2, 2, 4]), y = np.array([4, 2, 1, 2]) ответ
# True.

x = np.array([1, 2, 2, 4, 55])
y = np.array([4, 2, 55, 1, 2])

# 1. First way
def isEqualsOriginal():
    if len(x) == len(y):
        return sorted(x) == sorted(y)
    else:
        return False

    # Не уверен, что мультимножества можно сравнивать вышеуказанным способом, возможно так правильнее (нашел в сети):
    # compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    # return compare(x, y)

# %timeit result = isEqualsOriginal()
print(isEqualsOriginal())

# 2. With numpy
def isEqualsNumpy():
    return np.array_equal(np.sort(x), np.sort(y))

# %timeit result = isEqualsNumpy()
print(isEqualsNumpy())