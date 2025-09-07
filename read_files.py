


import os

def get_all_file_paths(folder_path):
    """
    Loops over a folder and its subfolders to get the full path of every file.

    Args:
        folder_path (str): The path to the folder to start the search from.

    Returns:
        list: A list containing the full paths of all files found.
    """
    all_file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_file_paths.append(full_path)
    return all_file_paths

# Example usage:
target_folder = 'C:/audio-files'  # Replace with the actual folder path
file_paths = get_all_file_paths(target_folder)

for path in file_paths:
    print(path)