import cv2
import pandas as pd
import matplotlib.pyplot as plt


def create_and_argument_dataframe(csv_path: str) -> pd.DataFrame:
    """
    Считывает CSV, получает размеры изображения, добавляет размеры в Data_frame
    :return: DataFrame с тремя дополнительными столбцами
    """
    df = pd.read_csv(csv_path)
    df.columns = ['absolute_path', 'relative_path']

    width = []
    height = []
    channels = []
    for path in df['absolute_path']:
        img = cv2.imread(path)
        if img is not None:
            width.append(img.shape[1])
            height.append(img.shape[0])
            channels.append(img.shape[2])
        else:
            width.append(0)
            height.append(0)
            channels.append(0)

    df['width'] = width
    df['height'] = height
    df['channels'] = channels
    return df


def compute_and_show_statistic(df: pd.DataFrame) -> None:
    """
    Вычисляет и печатает статистику
    :param df: DataFrame
    """
    if not df.empty:
        stat = df[['width', 'height', 'channels']].describe()
        print(stat)
    else:
        print("DataFrame is empty")


def filter_width_height(df: pd.DataFrame, max_w: int, max_h: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по ширине и высоте
    :return: обновленный DataFrame
    """
    new_df = df[((df['width'] <= max_w) & (df['height'] <= max_h))]
    return new_df


def add_area_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбец с площадью и сортирует
    :param df: DataFrame
    :return: обновленный DataFrame
    """
    if not df.empty:
        df['area'] = df['width'] * df['height']
        return df.sort_values('area')
    else:
        print("DataFrame is empty")
        return pd.DataFrame()


def create_histogram(df: pd.DataFrame, col_name: str) -> None:
    """
    Создает и отображает гистограмму
    :param df: DataFrame
    """
    if not df.empty:
        plt.figure(figsize=(12, 6))
        df[col_name].hist(bins=len(df))
        plt.title(f'Гистограмма')
        plt.xlabel(col_name)
        plt.ylabel('Количество изображений')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()
    else:
        print("DataFrame is empty")