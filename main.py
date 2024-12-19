import argparse

import cv2
import matplotlib.pyplot as plt

from image import read_image, convert_to_grayscale, plot_histogram, save_image


def get_args() -> argparse.Namespace:
    """
    Читает аргументы из терминала
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type = str, help="")
    parser.add_argument("save_path", type = str, help="")
    arguments = parser.parse_args()
    return arguments


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


def main() -> None:
    try:
        args = get_args()

        image_path = args.image_path
        save_path = args.save_path

        original_image = read_image(image_path)

        print(f"Размер изображения: {original_image.shape[1]}x{original_image.shape[0]}")

        grayscale_image = convert_to_grayscale(original_image)

        plot_histogram(original_image, "оригинального изображения")

        plot_histogram(grayscale_image, "полутонового изображения")

        display_images(original_image, grayscale_image)

        save_image(grayscale_image, save_path)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
