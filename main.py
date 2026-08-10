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
    folder_path = input("Enter folder path: ")

    if not os.path.isdir(folder_path):
        print("Enter a valid folder path.")
        return

    files = os.listdir(folder_path)

    organized_count = {
        category: 0
        for category in set(extension_map.values())
    }

    skipped_files = 0
    ignored_folders = 0

    for category in set(extension_map.values()):
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)


    for file in files:

        source_file = os.path.join(folder_path, file)

        if not os.path.isfile(source_file):
            ignored_folders += 1
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        destination_folder = extension_map.get(extension)
        if destination_folder is None:
            skipped_files += 1
            continue

        destination_file = os.path.join(folder_path, destination_folder, file)
        if os.path.exists(destination_file):
            counter = 1
            new_filename = f"{filename}_{counter}{extension}"

            while os.path.exists(os.path.join(folder_path, destination_folder, new_filename)):

                counter += 1
                new_filename = f"{filename}_{counter}{extension}"

            destination_file = os.path.join(folder_path, destination_folder, new_filename)


        shutil.move(source_file, destination_file)

        organized_count[destination_folder] += 1


    print("\nFile Organized Counts:")
    print("------------------------")

    for category, count in organized_count.items():
        print(f"{category}: {count}")

    print(f"Skipped Files: {skipped_files}")
    print(f"Folders Ignored: {ignored_folders}")

if __name__ == "__main__":
    main()
