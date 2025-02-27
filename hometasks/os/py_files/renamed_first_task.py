import shutil

import os

os_name = os.name
current_dir = os.getcwd()

print(f"Операционная система: {os_name}")
print(f"Текущий каталог: {current_dir}")

files_info = {}

# Проходим по всем файлам в текущей директории
for file in os.listdir():
    file_path = os.path.join(current_dir, file)
    print(os.path.splitext(file)[-1])
    # Проверяем, является ли это файлом
    if os.path.isfile(file_path):
        # Получаем расширение файла
        file_ext = os.path.splitext(file)[-1].lower()

#
        if file_ext:  # Если есть расширение
            folder_name = file_ext[1:] + "_files"  # Создаем имя папки без точки
            folder_path = os.path.join(current_dir, folder_name)

            # Создаем папку, если её нет
            os.makedirs(folder_path, exist_ok=True)

            # Перемещаем файл
            new_file_path = os.path.join(folder_path, file)
            shutil.move(file_path, new_file_path)

            # Сохраняем информацию о файле
            file_size = os.path.getsize(new_file_path)
            if folder_name not in files_info:
                files_info[folder_name] = {"count": 0, "size": 0}
            files_info[folder_name]["count"] += 1
            files_info[folder_name]["size"] += file_size

# Выводим информацию о перемещенных файлах
for folder, info in files_info.items():
    size_in_mb = round(info["size"] / (1024 * 1024), 2)  # Переводим байты в мегабайты
    print(f"В папке '{folder}' перемещено {info['count']} файлов, их суммарный размер - {size_in_mb} МБ")

# Переименование одного файла в каждой папке
for folder in files_info.keys():
    folder_path = os.path.join(current_dir, folder)
    files = os.listdir(folder_path)

    if files:  # Если в папке есть файлы
        old_name = files[0]
        old_path = os.path.join(folder_path, old_name)

        new_name = "renamed_" + old_name
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Файл {old_name} был переименован в {new_name}")
