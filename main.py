import cv2

import sys
import argparse
import matplotlib.pyplot as plt
from image import read_image, convert_to_grayscale, plot_histogram, save_image


def get_args() -> argparse.Namespace:
    """
    Читает аргументы из терминала
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type = str, help="Keyword of search request")
    parser.add_argument("-d", "--imgdir", type = str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--flag", type = bool, help= "Grayscale true or false")
    arguments = parser.parse_args()
    print(arguments.flag)
    return arguments


def main(image_path: str, save_path: str) -> None:
    try:

        original_image = read_image(image_path)

        print(f"Размер изображения: {original_image.shape[1]}x{original_image.shape[0]}")

        grayscale_image = convert_to_grayscale(original_image)

        plot_histogram(original_image, "оригинального изображения")

        plot_histogram(grayscale_image, "полутонового изображения")

        display_images(original_image, grayscale_image)

        save_image(grayscale_image, save_path)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def display_images(original_image, grayscale_image) -> None:
    """
    Отображает оригинальное и полутоновое изображение
    """
    plt.figure(figsize=(12, 6))

    # Отображение оригинального изображения
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title("Оригинальное изображение")
    plt.axis('off')

    # Отображение полутонового изображения
    plt.subplot(1, 2, 2)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title("Полутоновое изображение")
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Использование: python main.py <путь_к_изображению> <путь_для_сохранения>")
        sys.exit(1)

    image_path = sys.argv[1]
    save_path = sys.argv[2]
    main(image_path, save_path)