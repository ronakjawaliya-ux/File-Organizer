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

    organized_count = {
        "Resume": 0,
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0
    }

    skipped_count = 0

    for category in extension_map.values():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)


    for file in files:

        source_file = os.path.join(folder_path, file)

        if not os.path.isfile(source_file):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        destination_folder = extension_map.get(extension)
        if destination_folder is None:
            skipped_count += 1
            continue

        destination_file = os.path.join(folder_path, destination_folder, file)
        if os.path.exists(destination_file):
            counter = 1
            new_filename = f"{filename}_{counter}{extension}"
            new_destination = os.path.join(folder_path, destination_folder, new_filename)

            while os.path.exists(new_destination):
                counter += 1
                new_filename = f"{filename}_{counter}{extension}"
                new_destination = os.path.join(folder_path, destination_folder, new_filename)

            destination_file = new_destination

        shutil.move(source_file, destination_file)

        organized_count[destination_folder] += 1


    print("\nFile Organized Counts:")
    print("------------------------")

    for category, count in organized_count.items():
        print(f"{category}: {count}")

    print(f"Skipped: {skipped_count}")


if __name__ == "__main__":
    main()