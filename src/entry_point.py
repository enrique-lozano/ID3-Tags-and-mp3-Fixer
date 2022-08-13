from mutagen.easyid3 import ID3
from shutil import copy2
import os

from src.utils.settings import get_config

def main():
    """
    Console entry point for this program. This is where the magic happens.
    """

    config = get_config()
    
    copy_files(config["input_path"], config["output_path"])

    files = os.listdir(config["output_path"])
    for file in files:
        audio = ID3(config["output_path"] + "/" + file)
        if config["id3_version"] == "2.3":
            audio.update_to_v23()
            audio.save(v2_version=3)
        elif config["id3_version"] == "2.4":
            audio.update_to_v24()
            audio.save(v2_version=4)


def copy_files(from_path: str, to_path: str):
    """
    Copy the .mp3 files of the input directory into the output directory. The copied files must be exactly the same as the originals. 
    """

    path_full_destination = os.path.join(os.getcwd(), to_path)

    files = os.listdir(from_path)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".mp3":
            if not os.path.exists(path_full_destination):
                os.makedirs(path_full_destination)

            copy2(from_path + "/" + file, to_path + "/" + file)
