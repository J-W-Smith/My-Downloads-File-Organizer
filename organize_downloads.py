import os
from pathlib import Path

# Mapping of directories to their corresponding file extensions
DIRECTORIES = {
        "AI": [".safetensors"],
    "HTML": [".html5", ".html", ".htm", ".xhtml"], 
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd", ".svg", ".jfif"], 
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp"], 
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".ppt", 
                  "pptx"], 
    "EXCEL": [".xlsx",".xls"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                 ".dmg", ".rar", ".xar", ".zip", ".tgz"], 
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "PLAINTEXT": [".txt", ".in", ".out", ".csv"], 
    "PDF": [".pdf"], 
    "PYTHON": [".py", "whl"], 
    "XML": [".xml"], 
    "EXE": [".exe", ".msi"], 
    "SHELL": [".sh"], 
    "ANDROID": [".apk"], 
    "3D Modeling": [".blend",".blend1"]
 }

# Flatten the DIRECTORIES dictionary for easy lookup
FILE_FORMATS = {
    file_format: directory
    for directory, file_formats in DIRECTORIES.items()
    for file_format in file_formats
}

def organize_junk():
    """
    Organize files in the current directory based on their file extensions.

    This function scans each file in the current directory, identifies its extension,
    and moves it to the corresponding directory based on its extension.
    """
    for entry in os.scandir():
        # Skip directories and continue with files
        if entry.is_dir():
            continue

        file_path = Path(entry)
        file_format = file_path.suffix.lower()  # Extract the file extension

        # Check if the file extension is in the predefined directories
        if file_format in FILE_FORMATS:
            # Determine the destination directory for the file based on its extension
            directory_path = Path(FILE_FORMATS[file_format])
            # Ensure the directory exists; if not, create it
            directory_path.mkdir(exist_ok=True)
            # Move the file to the corresponding directory
            file_path.rename(directory_path.joinpath(file_path))

    # Cleanup: Attempt to remove any empty directories left after organizing files
    for dir_entry in os.scandir():
        if dir_entry.is_dir():
            try:
                # Try to remove the directory; if it's not empty, the removal will fail
                os.rmdir(dir_entry)
            except OSError:
                # Ignore any errors while trying to remove directories
                pass

if __name__ == "__main__":
    # Entry point of the script: Organize files in the current directory
    organize_junk()
