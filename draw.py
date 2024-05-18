from PIL import Image, ImageDraw, ImageFont

# Создаем новое изображение (ширина, высота) с белым фоном
width, height = 400, 300
image = Image.new('RGB', (width, height), 'white')

# Создаем объект для рисования
draw = ImageDraw.Draw(image)

# Рисуем прямоугольник (начальная точка, конечная точка), цвет
draw.rectangle([50, 50, 150, 150], fill='blue', outline='black')

# Рисуем эллипс (вписанный прямоугольник), цвет
draw.ellipse([200, 50, 300, 150], fill='red', outline='black')

# Рисуем линию (начальная точка, конечная точка), цвет и ширина
draw.line([50, 200, 350, 200], fill='green', width=5)

# Рисуем текст
try:
    # Используем шрифт по умолчанию
    font = ImageFont.load_default()
    draw.text((50, 250), "Hello, PIL!", fill='black', font=font)
except IOError:
    print("Шрифт не найден")

# Сохраняем изображение
image.save('output_image.png')

print("Изображение сохранено как output_image.png")
