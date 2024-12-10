import os
import sys
import csv
from icrawler.builtin import GoogleImageCrawler
from pathlib import Path


class ImageCrawler:
    def __init__(self, keyword, save_dir, annotation_file, max_images) -> None:
        self.keyword = keyword
        self.save_dir = save_dir
        self.annotation_file = annotation_file
        self.max_images = max_images

    def download_images(self) -> None:
        """
        Загрузка изображений по слову
        """
        crawler = GoogleImageCrawler(storage={"root_dir": self.save_dir})
        crawler.crawl(keyword=self.keyword, max_num=self.max_images)


    def create_annotation(self) -> str:
        """
        Создание файла аннотации изображений
        """
        image_paths = list(Path(self.save_dir).glob('**/*.jpg')) + \
                      list(Path(self.save_dir).glob('**/*.png'))

        absolute_paths = [str(image_path.resolve()) for image_path in image_paths]
        relative_paths = [str(image_path.append(os.path.join(self.save_dir))) for image_path in image_paths]

        # Запись аннотации в CSV файл
        with open(self.annotation_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Absolute Path', 'Relative Path'])
            for abs_path, rel_path in zip(absolute_paths, relative_paths):
                writer.writerow([abs_path, rel_path])

        print(f"Аннотация сохранена в: {self.annotation_file}")
