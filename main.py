import os
import shutil


extension_map = {
    ".pdf": "Resume",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
}


def main():
    folder_path = "sample_files"
    files = os.listdir(folder_path)

    for category in extension_map.values():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)


    for file in files:

        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        destination_folder = extension_map.get(extension)
        if destination_folder is None:
            continue

        source_file = os.path.join(folder_path, file)
        destination_file = os.path.join(folder_path, destination_folder, file)
        shutil.move(source_file, destination_file)


if __name__ == "__main__":
    main()