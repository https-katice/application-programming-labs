import argparse
import os

import crawler
import iterator


def main() -> None:
    parser = argparse.ArgumentParser(description='Image crawler for downloading images and creating annotations.')
    parser.add_argument("keyword", type=str, help='Keyword to search for images.')
    parser.add_argument("save_dir", type=str, help='Directory to save images.')
    parser.add_argument("annotation_file", type=str, help='CSV file for annotations.')
    parser.add_argument("max_images", type=int, help='Maximum number of images to download.')

    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    cr = crawler.ImageCrawler(args.keyword, args.save_dir, args.annotation_file, args.max_images)
    cr.download_images()

    it = iterator.ImageIterator(args.annotation_file)
    for image_path in it:
        print(f'Обрабатываем изображение: {image_path}')


if __name__ == "__main__":
    main()
