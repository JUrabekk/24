#В файле image.jpg лежит изображение. Напишите функцию motion_blur(n) которая:
#1открывает изображение image.jpg
#2поворачивает его на 270 градусов против часовой стрелки без использования
#циклов (только встроенными средствами PIL)
#3обрабатывает полученное изображение с помощью размытия Гаусса
#(GaussianBlur) с параметром n
#4сохраняет результат в файле res.jpg

from PIL import Image, ImageFilter


def motion_blur(n):
    image = Image.open("image.jpg")
    image = image.transpose(Image.ROTATE_270)
    filtered = image.filter(ImageFilter.GaussianBlur(radius=n))
    filtered.save("res.jpg")

motion_blur(10)