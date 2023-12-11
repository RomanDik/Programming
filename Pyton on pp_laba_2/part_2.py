import os
import shutil
import csv
from typing import List

def get_absolute_path2(name: str) -> List[str]:
    """абсолютный путь для картинок определенного имени медведя"""
    absolute_path = os.path.abspath('dataset_2')
    image_names = os.listdir(absolute_path)

    image_class_names = [name_img for name_img in image_names if name in name_img]

    image_absolute_paths = list(
        map(lambda name: os.path.join(absolute_path, name), image_class_names))
    return image_absolute_paths


def get_relative_path2(name: str) -> List[str]:
    """относительный путь для картинок определенного имени медведя"""
    relative_path = os.path.relpath('dataset_2')
    image_names = os.listdir(relative_path)

    image_class_names = [name_img for name_img in image_names if name in name_img]

    image_relative_paths = list(
        map(lambda name: os.path.join(relative_path, name), image_class_names))
    return image_relative_paths


def replace_images(name: str) -> None:
    """Изменяет имена, объединяет номер и класс, переносит в dataset2 и удаляет старую папку"""
    relative_path = os.path.relpath('dataset_2')
    class_path = os.path.join(relative_path, name)
    image_names = os.listdir(class_path)

    image_relative_paths = list(map(lambda img: os.path.join(class_path, img), image_names))
    new_relative_paths = list(map(lambda img: os.path.join(relative_path, f'{name}_{img}'), image_names))

    for old_name, new_name in zip(image_relative_paths, new_relative_paths):
        os.replace(old_name, new_name)

    os.chdir('dataset_2')
    if os.path.isdir(name):
        os.rmdir(name)
    os.chdir('..')


def main() -> None:
    polarbear='polarbear'
    brownbear='brownbear'
    if os.path.isdir('dataset_2'):
        shutil.rmtree('dataset_2')
    old = os.path.relpath('dataset')
    new = os.path.relpath('dataset_2')
    shutil.copytree(old, new)

    replace_images(polarbear)
    replace_images(brownbear) 
    
    polarbear_absolute_paths = get_absolute_path2(polarbear)
    polarbear_relative_paths = get_relative_path2(polarbear)
    brownbear_absolute_paths = get_absolute_path2(brownbear)
    brownbear_relative_paths = get_relative_path2(brownbear)

    with open('annotation_2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for absolute_path, relative_path in zip(polarbear_absolute_paths, polarbear_relative_paths):
            writer.writerow([absolute_path, relative_path, polarbear])

        for absolute_path, relative_path in zip(brownbear_absolute_paths, brownbear_relative_paths):
            writer.writerow([absolute_path, relative_path, brownbear])


if __name__ == "__main__":
    main()