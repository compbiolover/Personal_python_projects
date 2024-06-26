import os
import shutil
import argparse
import time

def is_valid_filename(filename):
    """
    Check if a filename already follows the desired naming system.

    Args:
        filename (str): The filename to check.

    Returns:
        bool: True if the filename follows the desired naming system, False otherwise.
    """
    parts = filename.split("_")

    # Check if the filename consists of at least two parts separated by underscores
    if len(parts) >= 2:
        # Check if the rest of the parts contain only alphanumeric characters or underscores
        for part in parts[:-1]:
            if not all(c.isalnum() or c == '_' for c in part):
                return False

        # Check if all parts of the filename are lowercase
        if not all(part.islower() for part in parts):
            return False

        return True

    return False

def update_modification_time_recursive(directory):
    """
    Recursively update the modification time of files in a directory and its subdirectories.

    Args:
        directory (str): The directory path to update.

    Returns:
        None: This function does not return a value, but it updates the modification time of files.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Update the modification time of each file to the current time
            os.utime(file_path, (time.time(), time.time()))

def clean_and_organize_folder(folder_path):
    """
    Clean and organize the files in a specified folder.

    This function renames files in the given folder and its subdirectories to follow a specific naming format,
    but only if they don't already match the format and are not hidden. It also prints filenames that already
    follow the desired naming system.

    Args:
        folder_path (str): The path to the folder to be cleaned and organized.

    Returns:
        None: This function does not return a value, but it renames files in the specified folder.
    """
    if not os.path.exists(folder_path):
        print(f"The specified folder '{folder_path}' does not exist.")
    else:
        for root, _, files in os.walk(folder_path):
            for filename in files:
                old_file_path = os.path.join(root, filename)

                # Check if the file is hidden (starts with a dot)
                if filename.startswith("."):
                    print(f"Skipping hidden file '{filename}'.")
                    continue

                # Check if the filename already follows the desired naming system
                if is_valid_filename(filename):
                    print(f"Skipping file '{filename}' as it already follows the naming convention.")
                else:
                    # Split the filename and extension
                    name, extension = os.path.splitext(filename)

                    # Remove specific symbols from the filename and replace periods with underscores
                    cleaned_name = "".join(c if c.isalnum() or c == '.' else '_' for c in name)
                    cleaned_name = cleaned_name.replace(".", "_")

                    # Generate a new filename with lowercase and underscores
                    new_filename = cleaned_name.lower().replace(" ", "_") + extension

                    # Construct the new file path
                    new_file_path = os.path.join(root, new_filename)

                    # Rename the file with the new name (all lowercase)
                    os.rename(old_file_path, new_file_path)

        # Update the modification time of files and folders in the specified directory
        update_modification_time_recursive(folder_path)

def main():
    parser = argparse.ArgumentParser(description="Clean and organize files in a specified folder.")
    parser.add_argument("folder_path", type=str, help="The path to the folder to be cleaned and organized.")
    args = parser.parse_args()

    clean_and_organize_folder(args.folder_path)
    if os.path.exists(args.folder_path):
        print(f"Files in '{args.folder_path}' have been cleaned and organized.")

if __name__ == "__main__":
    main()