import os
from shutil import copy2

from mutagen.easyid3 import ID3, EasyID3

from src.utils.console import bcolors, printProgressBar
from src.utils.settings import get_config


def main():
    """
    Console entry point for this program. This is where the magic happens.
    """

    config = get_config()

    print()

    copy_files(
        config["input_path"], config["output_path"], config["new_filename_format"]
    )

    files = os.listdir(config["output_path"])

    if len(files) == 0:
        print()
        print("No files has been copied! Maybe your input directory has no valid files")
        print()
        print("Exiting the program...")
        return

    print(
        bcolors.GREEN
        + "\u2714 Files correctly copied to your output directory"
        + bcolors.ENDC
    )
    print()

    printProgressBar(
        0, len(files), prefix="Modifying metadata:", suffix="Complete", length=50
    )

    for i, file in enumerate(files):
        printProgressBar(
            i + 1,
            len(files),
            prefix="Modifying metadata:",
            suffix="Complete",
            length=50,
        )

        audio = ID3(config["output_path"] + "/" + file)
        if config["id3_version"] == "2.3":
            audio.update_to_v23()
            audio.save(v2_version=3)
        elif config["id3_version"] == "2.4":
            audio.update_to_v24()
            audio.save(v2_version=4)

    print(bcolors.GREEN + "\u2714 File metadata correctly modified" + bcolors.ENDC)
    print()


def copy_files(from_path: str, to_path: str, filename_format: str):
    """
    Copy the .mp3 files of the input directory into the output directory. The copied files must be exactly the same as the originals.
    """

    path_full_destination = os.path.join(os.getcwd(), to_path)

    files = os.listdir(from_path)

    printProgressBar(
        0, len(files), prefix="Copying files:", suffix="Complete", length=50
    )

    for i, file in enumerate(files):
        printProgressBar(
            i + 1, len(files), prefix="Copying files:", suffix="Complete", length=50
        )

        filename, file_extension = os.path.splitext(file)
        if file_extension == ".mp3":
            if not os.path.exists(path_full_destination):
                os.makedirs(path_full_destination)

            new_file_name = get_new_filename(
                filename_format, file, os.path.join(os.getcwd(), from_path, file)
            )

            copy2(from_path + "/" + file, to_path + "/" + new_file_name)


def get_new_filename(filename_format: str, current_filename: str, path: str) -> str:
    if not filename_format:
        return current_filename

    name_to_return = filename_format + ".mp3"

    for key in ["artist", "title", "album", "discnumber", "tracknumber"]:
        if ("{" + key + "}") in filename_format:
            if EasyID3(path).get(key) and len(EasyID3(path).get(key)[0]) > 0:
                name_to_return = name_to_return.replace(
                    "{" + key + "}", EasyID3(path).get(key)[0].split("/")[0]
                )
            else:
                print(
                    f"\n{bcolors.WARNING}WARN: for file: {current_filename} -> We cannot change the name of the file. Attribute '{key}' is missing in the file metadata. The previous filename will be kept{bcolors.ENDC}"
                )
                return current_filename

    # this is Windows specific (disallowed chars)
    name_to_return = "".join(char for char in name_to_return if char not in "/?\\*|<>")

    # double quotes (") and semi-colons (:) are also disallowed characters but we would
    # like to retain their equivalents, so they aren't removed
    name_to_return = name_to_return.replace('"', "'").replace(":", "-")

    return name_to_return
