#Напишите функцию twist_image(input_file_name, output_file_name), которая будет
#менять местами левую и правую половины изображения.
#Параметр input_file_name задаёт имя исходного файла, а output_file_name — имя
#файла, куда следует сохранить результат.

def twist_image(input_file_name, output_file_name):
    from PIL import Image

    im = Image.open(input_file_name)
    pixels = im.load()
    x, y = im.size
    xx = x // 2
    for i in range(xx):
        for j in range(y):
            r, g, b = pixels[i, j]
            rr, gg, bb = pixels[xx + i, j]
            pixels[i, j] = rr, gg, bb
            pixels[xx + i, j] = r, g, b
    im.save(output_file_name)
