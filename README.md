# File Organizer

A Python automation project that organizes files into categorized folders based on their file extensions.

## Features

- Accepts a folder path from the user
- Validates that the provided path is a directory
- Automatically creates category folders
- Organizes files based on their extensions
- Supports multiple file extensions
- Handles uppercase and lowercase extensions
- Prevents filename conflicts by generating unique filenames
- Tracks skipped unsupported files
- Tracks ignored folders
- Displays a final organization summary

## Supported Categories

| Category | Extensions |
|----------|------------|
| Resume | `.pdf` |
| Images | `.jpg`, `.jpeg`, `.png` |
| Documents | `.txt` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio | `.mp3`, `.wav`, `.flac` |

## How It Works

1. The user enters a folder path.
2. The program verifies that the path is a valid directory.
3. Files inside the folder are scanned.
4. The file extension is identified.
5. The extension is matched with `extension_map`.
6. The file is moved into the appropriate category folder.
7. If a filename already exists, a new filename is generated:
   - `resume.pdf`
   - `resume_1.pdf`
   - `resume_2.pdf`
8. Unsupported files are counted as skipped.
9. Folders are counted separately as ignored.
10. A final summary is displayed.

## Technologies Used

- Python
- `os`
- `shutil`

## How to Run

```bash
python main.py