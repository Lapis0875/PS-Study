# Migration Support for old boj solution files.
import os
from pathlib import Path


def migrate_file(base_path: str, file_path: str):
    """Function to migrate a single file from the old format to the new format."""
    file_name, file_ext = os.path.splitext(file_path)
    boj_id = file_name[3:]
    # Read the content of the old solution file
    content = ""
    with open(os.path.join(base_path, file_path), "r") as old_file:
        content = old_file.read()

    # Create the new directory structure
    dir_path = os.path.join(base_path, boj_id)
    is_exist = os.path.exists(dir_path)
    new_file_name = f"solution_old{file_ext}" if is_exist else f"solution{file_ext}"
    if not is_exist:
        os.mkdir(dir_path)
    else:
        print(f"> Directory {dir_path} already exists. Move old solution file as {new_file_name}.")
        
    with open(os.path.join(dir_path, new_file_name), "w") as new_file:
        new_file.write(f"# Migrated from {os.path.join(base_path, file_path)} by boj_validator\n")
        new_file.write(content)
    os.remove(os.path.join(base_path, file_path))

def migrate(path: str):
    """Function to automatically migrate old boj solution files (bojXXXXX.{lang_ext}) to the new format (boj/XXXXXX/solution.{lang_ext})."""
    for item in os.listdir(path):
        # print(f": {item} / isFile? : {os.path.isfile(os.path.join(path, item))}")
        if os.path.isfile(os.path.join(path, item)) and item.startswith("boj"):
            print(f"> Found {item}, migrating ...")
            migrate_file(path, item)
