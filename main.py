import os
import shutil


def main():

    folder_path = "sample_files"
    files = os.listdir(folder_path)
    print(files)

    os.makedirs(os.path.join(folder_path, "Resume"), exist_ok=True)

    for file in files:
        if file.endswith(".pdf"):
            source_file = os.path.join(folder_path, file)
            destination_file = os.path.join(folder_path,"Resume", file)
            shutil.move(source_file,destination_file)



if __name__ == "__main__":
    main()