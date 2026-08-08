import os
import shutil


def main():

    folder_path = "sample_files"
    files = os.listdir(folder_path)


    os.makedirs(os.path.join(folder_path, "Resume"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "Images"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "Documents"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "Videos"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "Audio"), exist_ok=True)


    for file in files:

        file_cases = file.lower()

        if file_cases.endswith(".pdf"):
            destination_folder = os.path.join(folder_path, "Resume")

        elif file_cases.endswith(".jpg") or file_cases.endswith(".jpeg") or file_cases.endswith(".png"):
            destination_folder = os.path.join(folder_path, "Images")

        elif file_cases.endswith(".txt"):
            destination_folder = os.path.join(folder_path, "Documents")

        elif file_cases.endswith(".mp4") or file_cases.endswith(".mkv") or file_cases.endswith(".avi") or file_cases.endswith(".mov"):
            destination_folder = os.path.join(folder_path, "Videos")

        elif file_cases.endswith(".mp3") or file_cases.endswith(".wav") or file_cases.endswith(".flac"):
            destination_folder = os.path.join(folder_path, "Audio")

        else:
            continue

        source_file = os.path.join(folder_path, file)
        destination_file = os.path.join(destination_folder, file)
        shutil.move(source_file, destination_file)


if __name__ == "__main__":
    main()