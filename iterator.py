class ImageIterator:

    def __init__(self, annotation_file) -> None:
        self.annotation_file = annotation_file
        self.image_paths = open(annotation_file, 'r', encoding='utf-8')
        next(self.image_paths)

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        line = self.image_paths.readline().strip()
        if line:
            part = line.split(',')
            return part[0]
        else:
            raise StopIteration

