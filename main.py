import os
import shutil


def main():
    pass

folder_path = "sample_files"

files = os.listdir(folder_path)

files = [
    "resume.pdf",
    "photo.jpg",
    "notes.txt",
    "book.pdf"
]

for file in files:
    if file.endswith(".pdf"):
        print(file)

if __name__ == "__main__":
    main()