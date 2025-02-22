import os
import subprocess

# Specify the folder containing the files and the path to the compiled C++ executable
folder_path = 'graphs/BHOSLIB_sorted'
cpp_executable = './deploy/graphchecker'  # Assuming it's in the current directory

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Run the C++ executable with the file as an argument
        result = subprocess.run([cpp_executable, file_path], capture_output=True, text=True)

        # print result
        print(f"For file {filename}: {result.stdout}")