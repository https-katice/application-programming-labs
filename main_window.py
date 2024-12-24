from PyQt5.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from iterator import ImageIterator


class Window(QMainWindow):
    def __init__(self):
        """
        Cоздает окно для отображения изображений с кнопкой переключения между изображениями и кнопкой выбора аннотации
        """
        super().__init__()

        self.iterator = None

        self.setWindowTitle("hedgehog")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image = QLabel("here is a pic")
        self.image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image)

        self.annotation = QPushButton("choose annotation")
        self.annotation.clicked.connect(self.select_annotation_file)
        self.layout.addWidget(self.annotation)

        self.next = QPushButton("next")
        self.next.clicked.connect(self.show_next_image)
        self.layout.addWidget(self.next)

    def select_annotation_file(self):
        """
        Открывает диалоговое окно выбора файла и обрабатывает выбор пользователя
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "choose annotation", "", "CSV Files (*.csv)")
        if file_path:
            self.iterator = ImageIterator(file_path)
            try:
                self.show_image()
            except StopIteration:
                self.image.setText("annotation is empty")

    def show_image(self) -> None:
        """
        Показывает текущее изображение
        """
        try:
            image_path = next(self.iterator)
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                self.image.setText(f"cant load: {image_path}")
            else:
                self.image.setPixmap(pixmap.scaled(self.image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        except StopIteration:
            self.image.setText("the end")

    def show_next_image(self) -> None:
        """
        Вызывает функцию show_image()
        """
        self.show_image()