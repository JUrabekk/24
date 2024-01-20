#В файле image.jpg лежит изображение. Напишите функцию make_preview(size,
#n_colors) которая:
#1открывает изображение image.jpg
#2уменьшает его до размера size
#3уменьшает число цветов в изображении до n_colors (такая процедура
#называется квантование или quantize)
#4сохраняет результат в файле res.bmp

from PIL import Image


def make_preview(size, n_colors):
    im = Image.open('image.jpg')
    im = im.resize(size)
    im = im.quantize(n_colors)
    im.save('res.bmp')

make_preview((400, 200), 64)