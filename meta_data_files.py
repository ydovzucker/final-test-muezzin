from tinytag import TinyTag
import json
import wave
from pathlib import Path


import os

# def get_all_file_paths(folder_path):
#     """
#     Loops over a folder and its subfolders to get the full path of every file.
#
#     Args:
#         folder_path (str): The path to the folder to start the search from.
#
#     Returns:
#         list: A list containing the full paths of all files found.
#     """
#     all_file_paths = []
#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             full_path = os.path.join(root, file)
#             meta_data = TinyTag.get(full_path)
#
#             all_file_paths.append()
#     return all_file_paths
def get_meta_data(full_path):
    tag = TinyTag.get(full_path)
    return tag
def convert_meta_data_to_json(tag,full_path):
    data = {
        "file_path": full_path,
        "metadata": {
            "title": tag.title,
            "artist": tag.artist,
            "album": tag.album,
            "duration": tag.duration,  # in seconds
            "filesize": tag.filesize,  # in bytes
            # Add other metadata fields as needed
        }
    }
    json_string = json.dumps(data, indent=4)

    return json_string

# Example usage
if __name__ == "__main__":
    # target_folder = 'C:/audio-files'  # Replace with the actual folder path
    # file_paths = get_all_file_paths(target_folder)

    # for path in file_paths:
    #     print(path)
    meta_data = get_meta_data(r"C:/audio-files\download (6).wav")
    print(convert_meta_data_to_json(meta_data,r"C:/audio-files\download (6).wav"))






# import wave
# from pathlib import Path
#
#     wav_file_path = Path("your_audio_file.wav") # Replace with your WAV file path
#
#     try:
#         with wave.open(str(wav_file_path), 'rb') as wf:
#             print(f"Number of channels: {wf.getnchannels()}")
#             print(f"Sample width (bytes): {wf.getsampwidth()}")
#             print(f"Frame rate (sample rate): {wf.getframerate()}")
#             print(f"Number of frames: {wf.getnframes()}")
#             print(f"Compression type: {wf.getcomptype()}")
#             print(f"Compression name: {wf.getcompname()}")
#     except wave.Error as e:
#         print(f"Error reading WAV file: {e}")





