import shutil


def move_file(file, destination_directory):
    shutil.copy2(file, destination_directory)
