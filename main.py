import argparse

from data_frame import create_and_argument_dataframe, compute_and_show_statistic, filter_width_height, add_area_and_sort, create_histogram


def parse() -> tuple[str, int, int]:
    """
    Читает аргументы из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=str, help="Path to the annotation file")
    parser.add_argument("max_width", type=int, help="Max width of image")
    parser.add_argument("max_height", type=int, help="Max height of image")
    args = parser.parse_args()
    return args.csv_path, args.max_width, args.max_height


def main():
    csv_path, max_width, max_height = parse()
    try:
        data_frame = create_and_argument_dataframe(csv_path)
        if data_frame.empty:
            print("error during creation DataFrame, exited")
            return
        compute_and_show_statistic(data_frame)
        new_data_frame = filter_width_height(data_frame, max_width, max_height)
        print("\n\nfiltered DataFrame:\n", new_data_frame)
        new_new_data_frame = add_area_and_sort(data_frame)
        print("\n\nDataFrame sorted by area:\n", new_new_data_frame)
        create_histogram(data_frame, 'area')
        create_histogram(data_frame, 'height')
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()