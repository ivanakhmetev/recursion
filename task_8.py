import os

def _recursive_find_files(current_path, files):
    for item in os.listdir(current_path):
        item_path = os.path.join(current_path, item)
        if os.path.isfile(item_path):
            files.append(item_path)
        elif os.path.isdir(item_path):
            _recursive_find_files(item_path, files)

def recursive_find_files(start_path):
    files= []
    _recursive_find_files(start_path, files)
    return files
