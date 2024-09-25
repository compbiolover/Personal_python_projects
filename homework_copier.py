'''
Purpose:
This script copies homework assignments from students' directories to a single directory for grading.

Author:
Andrew Willems

Instructions:
1. Update the my_id variable with your login id.
2. Update the usr_list variable with the login ids of the students whose homework assignments you want to copy over.
3. Update the grading_dir variable with the directory where you want to copy the students' homework assignments for grading.
4. Update the homework_number variable with the number of the homework you want to copy over (if looking to only copy over specific assignments). If you want to copy over all of the students' homework assignments, set this variable to None.
5. Run the script.

Additional Instructions (Optional):
- You can also pass command line arguments to the script for more flexibility:
    - Use the `--homework_number` argument followed by the number(s) of the homework you want to copy over (if looking to only copy over specific assignments).
    - Use the `--my_id` argument followed by your login id.
    - Example usage: `python homework_copier.py --homework_number 05 06 --my_id thong`
'''
# Import necessary modules
import os
import subprocess
from shutil import copyfile
import pwd
import grp
import re
import argparse

# Initializing the parser
parser = argparse.ArgumentParser(description='A simple script to copy homework assignments from students directories to a single directory for grading')

# Adding arguments
parser.add_argument('--homework_number', type=str, nargs='*', help='The number(s) of the homework you want to copy over (if looking to only copy over specific assignments)', default=None, required=False)
parser.add_argument('--my_id', type=str, help='Your login id', required=True, default='thong')

# Parsing the arguments
args = parser.parse_args()

# Assigning the arguments to variables
my_id = args.my_id
homework_number = args.homework_number

# My login id
# my_id = 'awillems'

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

# Specify the number of the homework you want to copy over (if looking to only copy over specific assignments)
# homework_number = ['05']


for student in usr_list:
    # Create a directory for the student in the grading directory
    student_grading_dir = os.path.join(grading_dir, student)
    student_data_dir = os.path.join(grading_dir, student, 'data')
    os.makedirs(student_grading_dir, exist_ok=True)
    os.makedirs(student_data_dir, exist_ok=True)
    
    # Set the appropriate permissions for the student directories
    os.chmod(student_grading_dir, 0o755) # rwxr-xr-x
    os.chmod(student_data_dir, 0o755) # rwxr-xr-x

    # Ensure the current user has write permissions
    current_user = pwd.getpwuid(os.getuid()).pw_name
    current_group = grp.getgrgid(os.getgid()).gr_name
    
    # Make sure the current user has proper permissions
    os.chown(student_grading_dir, os.getuid(), os.getgid())
    os.chown(student_data_dir, os.getuid(), os.getgid())



    students_dir = '/home/jupyter-' + student + '/assignments'

    for root, dirs, files in os.walk(students_dir):
        for file in files:
            if homework_number is None:
                # Copy over all of their homework assignments
                if file.endswith('.ipynb' or '.py'):
                    copyfile(os.path.join(root, file), os.path.join(student_grading_dir, file))
                    print('Copying ' + file + ' from ' + students_dir + ' to ' + student_grading_dir)
            else:
                # Copy over only the homework assignments specified in the homework_number list
                if any(number in file for number in homework_number):
                    copyfile(os.path.join(root, file), os.path.join(student_grading_dir, file))
                    print('Copying ' + file + ' from ' + students_dir + ' to ' + student_grading_dir)


    # Copy over the data directory separately
    data_dir = '/home/jupyter-' + student + '/assignments/data'
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            copyfile(os.path.join(root, file), os.path.join(student_data_dir, file))
            print('Copying ' + file + ' from ' + data_dir + ' to ' + student_data_dir)
