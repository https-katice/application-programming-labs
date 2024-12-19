import cv2

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def read_image(file_path: str) -> np.ndarray:
    """
    Считывает изображение из файла
    """
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"Изображение не найдено по пути: {file_path}")
    return image


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Преобразует изображение в полутоновое
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def plot_histogram(image: np.ndarray, title: str) -> None:
    """
    Строит и показывает гистограмму изображения
    """
    plt.figure()
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='gray')
    plt.title(f'Гистограмма {title}')
    plt.xlabel('Значение яркости')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()


def save_image(image: np.ndarray, save_path: str) -> None:
    """
    Сохраняет изображение по заданному пути
    """
    cv2.imwrite(save_path, image)