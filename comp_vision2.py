import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('girl.jpg')

# Запросить размер батча
batch_size = int(input("Введите размер батча (от 30 до 80 пикселей): "))

# Проверка диапазона
if batch_size < 30 or batch_size > 80:
    print("Неверный размер батча. Пожалуйста, введите число в диапазоне от 30 до 80.")
else:
    # Создание окна для отображения изображения
    cv2.namedWindow('Image')

    # Функция обработки событий мыши
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Координаты точки: x={x}, y={y}")

            # Определение координат батча (площадь вокруг клика)
            half_batch = batch_size // 2

            # Ограничение координат батча, чтобы не выходить за пределы изображения
            x1 = max(0, x - half_batch)
            x2 = min(image.shape[1], x + half_batch)
            y1 = max(0, y - half_batch)
            y2 = min(image.shape[0], y + half_batch)

            # Отображение батча на изображении
            batch = image[y1:y2, x1:x2]

            # Вычисление средней интенсивности (по всем каналам изображения)
            mean_intensity = np.mean(batch)
            print(f"Средняя интенсивность батча: {mean_intensity}")

            # Отображение батча
            cv2.imshow("Batch", batch)

    # Привязка функции обработки событий мыши к окну
    cv2.setMouseCallback('Image', mouse_callback)

    # Отображение изображения
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


