import os

def recursive_find_files(start_path):
    items = os.listdir(start_path)
    items = [os.path.join(start_path, el) for el in items]
    files = [el for el in items if os.path.isfile(el)]
    dirs = [el for el in items if os.path.isdir(el)]
    if len(dirs) == 0:
        return files
    for dir in dirs:
        files.extend(recursive_find_files(dir))
    return files

