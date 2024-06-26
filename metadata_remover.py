import argparse # For parsing command-line arguments
import os # For working with file paths and file operations
import shutil # For copying and renaming files
import exiftool # For removing metadata from files

def remove_metadata(input_file_path):
    
    # Copy the original file to a new file with "_metadata_removed" in the filename
    base_name, ext = os.path.splitext(input_file_path)
    output_file_path = f"{base_name}_metadata_removed{ext}"
    shutil.copy2(input_file_path, output_file_path)

    # Remove metadata from the copied file
    with exiftool.ExifTool() as et:
        et.execute("-all=", output_file_path)

    # Delete any files that match the pattern 'original_file_metadata_removed.extension_original'
    pattern_to_delete = f"{base_name}_metadata_removed{ext}_original"
    if os.path.exists(pattern_to_delete):
        os.remove(pattern_to_delete)

def main():
    parser = argparse.ArgumentParser(description="Remove metadata from a file and create a new file with '_metadata_removed' in the filename.")
    parser.add_argument("input_file_path", help="Path to the input file from which you want to remove metadata.")
    args = parser.parse_args()
    
    remove_metadata(args.input_file_path)
    print(f"Metadata removed successfully. Created new file with metadata removed: {args.input_file_path}_metadata_removed")

if __name__ == "__main__":
    main()
