from tinytag import TinyTag
import json


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






# # Specify the path to your WAV file
# file_path = "path/to/your/audio.wav"
#
# try:
#     # Get the tag object for the WAV file
#     tag = TinyTag.get(file_path)
#
#     # Access various metadata attributes
#     print(f"Title: {tag.title}")
#     print(f"Artist: {tag.artist}")
#     print(f"Album: {tag.album}")
#     print(f"Duration (seconds): {tag.duration}")
#     print(f"Sample Rate (Hz): {tag.samplerate}")
#     print(f"Bitrate (kbps): {tag.bitrate}")
#     print(f"Channels: {tag.channels}")
#     print(f"Filesize (bytes): {tag.filesize}")
#     print(f"Genre: {tag.genre}")
#     print(f"Year: {tag.year}")
#
# except FileNotFoundError:
#     print(f"Error: File not found at {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# data = {
#                 "file_path": full_path,
#                 "metadata": {
#                     "title": tag.title,
#                     "artist": tag.artist,
#                     "album": tag.album,
#                     "duration": tag.duration,  # in seconds
#                     "filesize": tag.filesize,  # in bytes
#                     # Add other metadata fields as needed
#                 }
#             }
#
# def get_meta_data(full_path):
#     meta_data = TinyTag.get(full_path)
#     return meta_data
# def convert_meta_data_to_json(meta_data,full_path):
#     data = {
#         "file_path": full_path,
#         "metadata": {
#             "title": tag.title,
#             "artist": tag.artist,
#             "album": tag.album,
#             "duration": tag.duration,  # in seconds
#             "filesize": tag.filesize,  # in bytes
#             # Add other metadata fields as needed
#         }
#     }
#     json_string = json.dumps(data, indent=4)
#     print(json_string)
#     return json_string





