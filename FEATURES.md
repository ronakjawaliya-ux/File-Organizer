# File Organizer — Features

## 1. Custom Folder Path
- User can enter the folder path they want to organize.
- No fixed folder is required.

## 2. Folder Validation
- Checks whether the entered path is a valid directory.
- Displays an error and stops safely if the path is invalid.

## 3. Automatic File Organization
- Files are organized automatically based on their extensions.
- Supported categories:
  - Resume
  - Images
  - Documents
  - Videos
  - Audio

## 4. Multiple File Extensions
- Supports multiple extensions for the same category.
- Example:
  - `.jpg`, `.jpeg`, `.png` → Images
  - `.mp4`, `.mkv`, `.avi`, `.mov` → Videos
  - `.mp3`, `.wav`, `.flac` → Audio

## 5. Case-Insensitive Extensions
- Converts extensions to lowercase before checking.
- Example:
  - `TEST.PDF`
  - `Test.Pdf`
  - `test.pdf`
- All are recognized as `.pdf`.

## 6. Duplicate Filename Handling
- Prevents files from being overwritten.
- Automatically generates a new filename when a duplicate exists.
- Example:
  - `resume.pdf`
  - `resume_1.pdf`
  - `resume_2.pdf`

## 7. Unsupported File Tracking
- Files with unsupported extensions are skipped.
- The number of skipped files is displayed at the end.

## 8. Folder Detection
- Existing folders inside the target directory are ignored.
- The number of ignored folders is displayed.

## 9. Organization Statistics
- Tracks how many files were organized into each category.
- Displays a final summary after execution.

## 10. Automatic Category Folder Creation
- Required category folders are created automatically if they don't already exist.

## 11. Safe File Movement
- Uses Python's `shutil.move()` to move files to their appropriate destinations.