import hashlib
import json

import os
from pathlib import Path
from logger import Logger
Logger = Logger()
logger = Logger.get_logger()


def get_meta_data(full_path):

    file_path = Path(full_path)
    try:
        stats = file_path.stat()
        logger.info("got meta data for this file")
        return stats
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")

def convert_meta_data_to_json(stats,full_path):
    meta_data = {
        "file_path": full_path,
        f"File size": f"{stats.st_size} bytes",
        "Last modified time": os.path.getmtime(full_path),
        "Creation time": os.path.getctime(full_path),
        f"Permissions": stats.st_mode,
        f"Inode number": stats.st_ino,
        "file name": os.path.basename(full_path)

    }


    json_string = json.dumps(meta_data, indent=4)
    return json_string
#

# Example usage
if __name__ == "__main__":

    meta_data = get_meta_data(r"C:/audio-files\download (6).wav")
    print(convert_meta_data_to_json(meta_data,r"C:/audio-files\download (6).wav"))








