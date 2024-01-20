#Два изображения можно совместить так, что одно из них будет как бы
#«полупрозрачным». Для этого значения цветовых компонент каждого совмещаемого
#пикселя обоих изображений нужно попарно суммировать с определёнными весовыми
#коэффициентами.
#Например, если итоговый цвет (в нотации RGB) вычислять по формуле:
#R = 0.8 * R1 + 0.2 * R2
#G = 0.8 * G1 + 0.2 * G2
#B = 0.8 * B1 + 0.2 * B2
#то получится, что первое изображение будет иметь 20 процентов прозрачности.

from PIL import Image


def transparency(filename1, filename2):
    im1 = Image.open(filename1)
    im2 = Image.open(filename2)
    pix1 = im1.load()
    pix2 = im2.load()
    x, y = im1.size
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pix1[i, j]
            r2, g2, b2 = pix2[i, j]
            r = int(0.5 * r1 + 0.5 * r2)
            g = int(0.5 * g1 + 0.5 * g2)
            b = int(0.5 * b1 + 0.5 * b2)
            pix1[i, j] = r, g, b
    im1.save('res.jpg')

transparency('fish.jpg', 'space.jpg')