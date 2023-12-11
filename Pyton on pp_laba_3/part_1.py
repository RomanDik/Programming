import os
import csv
from typing import List

def get_absolute_path(name: str) -> List[str]:
    """
    Данная функция возвращает список абсолютных путей для всех изображений 
    определенного имени медведя, переданного в функцию
    """
    name_absolute_path=os.path.abspath(f"dataset/{name}")
    image_names = os.listdir(name_absolute_path)

    image_absolute_paths = list(map(lambda img: os.path.join(name_absolute_path, img), image_names))
    
    return image_absolute_paths

def get_relative_path(name: str) -> List[str]:
    """
    Данная функция возвращает список относительных путей для всех изображений 
    определенного имени медведя, переданного в функцию
    """
    name_relative_path=os.path.relpath(f"dataset/{name}")
    image_names = os.listdir(name_relative_path)

    image_relative_paths = list(map(lambda img: os.path.join(name_relative_path, img), image_names))

    return image_relative_paths
    
def make_annotation() -> None:
    polarbear='polarbear'
    brownbear='brownbear'

    polarbear_absolute_paths = get_absolute_path(polarbear)
    polarbear_relative_paths = get_relative_path(polarbear)
    brownbear_absolute_paths = get_absolute_path(brownbear)
    brownbear_relative_paths = get_relative_path(brownbear)

    with open('annotation.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for absolute_path, relative_path in zip(polarbear_absolute_paths, polarbear_relative_paths):
            writer.writerow([absolute_path, relative_path, polarbear])

        for absolute_path, relative_path in zip(brownbear_absolute_paths, brownbear_relative_paths):
            writer.writerow([absolute_path, relative_path, brownbear])


