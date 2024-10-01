'''
Purpose:
This script copies homework assignments from students' directories to a single directory for grading.

Author:
Andrew Willems

Instructions:
- You can pass command line arguments to the script for more flexibility:
    - Use the `--homework_number` argument followed by the number(s) of the homework you want to copy over (if looking to only copy over specific assignments).
    - Use the `--my_id` argument followed by your login id.
    - Use the `--verbose` flag to show detailed information about each file being copied.
    - Example usage: `python homework_copier.py --homework_number 05 06 --my_id thong --verbose`
'''
# Import necessary modules
import os
import subprocess
from shutil import copyfile
import pwd
import grp
import re
import argparse
import stat

# Initializing the parser
parser = argparse.ArgumentParser(description='A simple script to copy homework assignments from students directories to a single directory for grading')

# Adding arguments
parser.add_argument('--homework_number', type=str, nargs='*', help='The number(s) of the homework you want to copy over (if looking to only copy over specific assignments)', default=None, required=False)
parser.add_argument('--my_id', type=str, help='Your login id', required=True, default='thong')
parser.add_argument('--verbose', action='store_true', help='Show detailed information about each file being copied')

# Parsing the arguments
args = parser.parse_args()

# Assigning the arguments to variables
my_id = args.my_id
homework_number = args.homework_number
verbose = args.verbose

# Students' login ids
usr_list = [
    'jadetunj',
    'dandre10',
    'abaner10',
    'mbhuiya5',
    'ebonanno',
    'rchowdh3',
    'ddumont2',
    'helshora',
    'kestler1',
    'kfaberqu',
    'sgarci24',
    'kgarla13',
    'egilles4',
    'brideno1',
    'alamia',
    'seamlarr',
    'mmccar53',
    'tmyers14',
    'oolorun2',
    'aovispom',
    'kperille',
    'pramaswa',
    'nremilla',
    'brubino',
    'tsimms5',
    'csisca',
    'jturne88',
    'xxu28',
    'jking139',
    'aoverhol'
]

# Directory where to copy students' homework assignments for grading
grading_dir = '/home/jupyter-' + my_id + '/assignments'

def copy_file(src, dst):
    copyfile(src, dst)
    os.chmod(dst, 0o666)  # rw-rw-rw-
    if verbose:
        print(f'Copying {os.path.basename(src)} from {os.path.dirname(src)} to {os.path.dirname(dst)}')

def set_permissions(path):
    # Set directory permissions to 775 (rwxrwxr-x)
    os.chmod(path, 0o775)
    
    # Set group to the current user's primary group
    gid = os.getgid()
    os.chown(path, -1, gid)
    
    # Set the setgid bit
    current_mode = os.stat(path).st_mode
    os.chmod(path, current_mode | stat.S_ISGID)

for student in usr_list:
    # Create a directory for the student in the grading directory
    student_grading_dir = os.path.join(grading_dir, student)
    student_data_dir = os.path.join(grading_dir, student, 'data')
    os.makedirs(student_grading_dir, exist_ok=True)
    os.makedirs(student_data_dir, exist_ok=True)
    
    # Set permissions for the student directories
    set_permissions(student_grading_dir)
    set_permissions(student_data_dir)

    students_dir = '/home/jupyter-' + student + '/assignments'

    for root, dirs, files in os.walk(students_dir):
        # Skip .ipynb_checkpoints directories
        dirs[:] = [d for d in dirs if d != '.ipynb_checkpoints']
        
        for file in files:
            # Skip hidden files and .ipynb_checkpoints files
            if file.startswith('.') or '.ipynb_checkpoints' in root:
                continue
            
            if homework_number is None:
                # Copy over all of their homework assignments
                if file.endswith(('.ipynb', '.py')):
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(student_grading_dir, file)
                    copy_file(src_file, dst_file)
            else:
                # Copy over only the homework assignments specified in the homework_number list
                if any(number in file for number in homework_number):
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(student_grading_dir, file)
                    copy_file(src_file, dst_file)

    # Copy over the data directory separately
    data_dir = '/home/jupyter-' + student + '/assignments/data'
    for root, dirs, files in os.walk(data_dir):
        # Skip .ipynb_checkpoints directories
        dirs[:] = [d for d in dirs if d != '.ipynb_checkpoints']
        
        for file in files:
            # Skip hidden files and .ipynb_checkpoints files
            if file.startswith('.') or '.ipynb_checkpoints' in root:
                continue
            
            src_file = os.path.join(root, file)
            dst_file = os.path.join(student_data_dir, file)
            copy_file(src_file, dst_file)

print("Homework copying process completed.")