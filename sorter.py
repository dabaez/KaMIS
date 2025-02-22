import os
import subprocess

# Specify the folder containing the files and the path to the compiled C++ executable
folder_path = 'graphs/BHOSLIB_converted'
out_path = 'graphs/BHOSLIB_sorted'
cpp_executable = './deploy/sort_adjacencies'  # Assuming it's in the current directory

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Run the C++ executable with the file as an argument
        result = subprocess.run([cpp_executable, file_path], capture_output=True, text=True)

        # Write the output to a new file
        out_filename = filename.replace('.clq', '_sorted')
        out_file_path = os.path.join(out_path, filename)
        with open(out_file_path, 'w') as out_file:
            out_file.write(result.stdout)
