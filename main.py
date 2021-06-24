from PIL import Image, ImageDraw

def ContrastUp():
    filename = input('Введите название изображения с расширением ')
    img = Image.open(filename)  # Открываем изображение
    idraw = ImageDraw.Draw(img)
    pix = img.load()  # Загруаем матрицу пикселей
    for i in range(img.size[0]):  # Перебираем все пиксели
        for j in range(img.size[1]):
            sr = sum(pix[i, j]) // 3  # Cредний цвет всего RGB в данном пикселе
            factor = abs(128 - sr) / 128  # Фактор удаления от серого цвета (128, 128, 128). Для плавного изменения. Чем дальше - тем сильнее.

            if sr >= 128:  # Если цвет ближе к белому
                r = pix[i, j][0] * (1 + 0.5 * factor) if pix[i, j][0] * (1 + 0.4 * factor) <= 255 else 255   # Формула для более-менее нормального изменения цвета
                g = pix[i, j][1] * (1 + 0.5 * factor) if pix[i, j][1] * (1 + 0.4 * factor) <= 255 else 255
                b = pix[i, j][2] * (1 + 0.5 * factor) if pix[i, j][2] * (1 + 0.4 * factor) <= 255 else 255
            else:  # Если цвет ближе к чёрному
                r = pix[i, j][0] * (1 - 0.4 * factor)  # Формула для более-менее нормального изменения цвета
                g = pix[i, j][1] * (1 - 0.4 * factor)
                b = pix[i, j][2] * (1 - 0.4 * factor)

            idraw.point((i, j), (int(r), int(g), int(b)))  # Рисуем поверх старого пиксель новый с новым цветом

    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def ContrastDown():
    filename = input('Введите название изображения с расширением')
    img = Image.open(filename)  # Открываем изображение
    idraw = ImageDraw.Draw(img)
    pix = img.load()  # Загруаем матрицу пикселей
    for i in range(img.size[0]):  # Перебираем все пиксели
        for j in range(img.size[1]):
            sr = sum(pix[i, j]) // 3  # Cредний цвет всего RGB в данном пикселе
            factor = abs(128 - sr) / 128  # Фактор удаления от серого цвета (128, 128, 128). Для плавного изменения. Чем дальше - тем сильнее.

            if sr >= 128:  # Если цвет ближе к белому
                r = pix[i, j][0] * (1 - 0.5 * factor) if pix[i, j][0] * (1 + 0.4 * factor) >= 0 else 255   # Формула для более-менее нормального изменения цвета
                g = pix[i, j][1] * (1 - 0.5 * factor) if pix[i, j][1] * (1 + 0.4 * factor) >= 0 else 255
                b = pix[i, j][2] * (1 - 0.5 * factor) if pix[i, j][2] * (1 + 0.4 * factor) >= 0 else 255
            else:  # Если цвет ближе к чёрному
                r = pix[i, j][0] * (1 + 0.4 * factor)  # Формула для более-менее нормального изменения цвета
                g = pix[i, j][1] * (1 + 0.4 * factor)
                b = pix[i, j][2] * (1 + 0.4 * factor)

            idraw.point((i, j), (int(r), int(g), int(b)))  # Рисуем поверх старого пиксель новый с новым цветом

    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def BrightnessUp():
    filename = input('Введите название изображения с расширением')
    img = Image.open(filename)  # Открываем изображение
    idraw = ImageDraw.Draw(img)
    pix = img.load()  # Загруаем матрицу пикселей
    for i in range(img.size[0]):  # Перебираем все пиксели
        for j in range(img.size[1]):
            r = pix[i, j][0] * 1.4 if pix[i, j][0] * 1.4 <= 255 else 255  # Увеличение яркости на 40%
            g = pix[i, j][1] * 1.4 if pix[i, j][1] * 1.4 <= 255 else 255  # Если получается цвет пикселя больше 255, то ставим 255
            b = pix[i, j][2] * 1.4 if pix[i, j][2] * 1.4 <= 255 else 255

            idraw.point((i, j), (int(r), int(g), int(b)))  # Рисуем поверх старого пиксель новый с новым цветом

    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def BrightnessDown():
    filename = input('Введите название изображения с расширением\n')
    img = Image.open(filename)  # Открываем изображение
    idraw = ImageDraw.Draw(img)
    pix = img.load()  # Загруаем матрицу пикселей
    for i in range(img.size[0]):  # Перебираем все пиксели
        for j in range(img.size[1]):
            r = pix[i, j][0] * 0.6 if pix[i, j][0] * 0.6 >= 0 else 0  # Уменьшение яркости на 40%
            g = pix[i, j][1] * 0.6 if pix[i, j][1] * 0.6 >= 0 else 0  # Если получается цвет пикселя меньше 0, то ставим 0
            b = pix[i, j][2] * 0.6 if pix[i, j][2] * 0.6 >= 0 else 0

            idraw.point((i, j), (int(r), int(g), int(b)))  # Рисуем поверх старого пиксель новый с новым цветом

    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def FlipHorizontal():
    filename = input('Введите название изображения с расширением')
    img = Image.open(filename)  # Открываем изображение
    img = img.transpose(Image.FLIP_LEFT_RIGHT)  # С помощью встроенной функции транспонируем массив пикселей
    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def FlipVertical():
    filename = input('Введите название изображения с расширением')
    img = Image.open(filename)  # Открываем изображение
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # С помощью встроенной функции транспонируем массив пикселей
    img.save('result.png')  # Обработанное изображение сохраняем в result.png
    print('ГОТОВО. Обработанное изображение находится в result.png')

def main():
    print('РАБОТА С ИЗОБРАЖЕНИЯМИ' +
          '\n1. Повысить яркость' +
          '\n2. Понизить яркость' +
          '\n3. Повысить контрастность' +
          '\n4. Понизить контрастность' +
          '\n5. Отразить по горизонтали' +
          '\n6. Отразить по вертикали')

    dig = input()
    if dig == '1':
        BrightnessUp()
    elif dig == '2':
        BrightnessDown()
    elif dig == '3':
        ContrastUp()
    elif dig == '4':
        ContrastDown()
    elif dig == '5':
        FlipHorizontal()
    elif dig == '6':
        FlipVertical()


if __name__ == "__main__":
    main()
