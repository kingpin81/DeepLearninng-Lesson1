import numpy as np

# 6) Реализовать кодирование длин серий (Run-length encoding). Дан вектор x.
# Необходимо вернуть кортеж из двух векторов одинаковой длины. Первый
# содержит числа, а второй - сколько раз их нужно повторить. Пример: x =
# np.array([2, 2, 2, 3, 3, 3, 5]). Ответ: (np.array([2, 3, 5]), np.array([3, 3, 1])).

testArray = np.array([2, 2, 2, 3, 3, 3, 5])

# 1. Without numpy's functions
def getRLEOriginal(inArray):
    numArray = np.array([], dtype=int)
    countArray = np.array([], dtype=int)
    lastNum = None
    count = 0

    for i, column in enumerate(inArray):
        if lastNum == None:
            lastNum = column
            count += 1
            continue

        if column == lastNum:
            count += 1
        else:
            numArray = np.append(numArray, lastNum)
            countArray = np.append(countArray, count)
            lastNum = column
            count = 1

        if i == len(inArray) - 1:
            numArray = np.append(numArray, lastNum)
            countArray = np.append(countArray, count)

    return (numArray, countArray)

# %timeit tuple = getRLEOriginal(testArray)
print(getRLEOriginal(testArray))


# 2. With numpy
# Не хватило времени разобраться как реалиовать без обычных циклов...

