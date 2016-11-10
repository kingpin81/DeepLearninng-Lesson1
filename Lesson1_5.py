import numpy as np

# 5) Дан трёхмерный массив, содержащий изображение, размера (height, width,
# numChannels), а также вектор длины numChannels. Сложить каналы
# изображения с указанными весами, и вернуть результат в виде матрицы
# размера (height, width). Считать реальное изображение можно при помощи
# функции scipy.misc.imread (если изображение не в формате png, установите
# пакет pillow: conda install pillow). Преобразуйте цветное изображение в оттенки
# серого, использовав коэффициенты np.array([0.299, 0.587, 0.114]). Для вывода
# используйте scipy.misc.imshow или matplotlib.pyplot.imshow

vectorCfs = np.array([0.299, 0.587, 0.114])

# Read image
from scipy import misc
f = misc.face()
misc.imsave('face.png', f)

# To array
face = misc.imread('face.png')

# Не хватило вермени разобраться что нужно сделать с массивом...
# В первом приблежении я подумал что каждый "слой", т.е. face[:][:][0], face[:][:][1] и face[:][:][2]
# нужно соответственно умножить на значения vectorCfs[0], vectorCfs[1] и vectorCfs[2].
# Но, к сожалению, не понял что означает "сложить каналы".


# Output image
# import matplotlib.pyplot as plt
# plt.imshow(face)
# plt.show()


