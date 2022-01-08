import os

extension_check =  input("What file type should I only rename? (type in the dot! e.g. .pdf)\n")
header = input("What header do you want all files to have?")

if extension_check == "":
    extension_check = ".pdf"
if header == "":
    header = "NEW_NAME"

# Get current directory path
current_dir = str(os.getcwd())

# List of all original names, for backup purposes
original_name_list = []

# Get all files in directory
for files in os.listdir(current_dir):
    original_name = current_dir + "\\" + files
    original_name_list.append(original_name)

    # Unique ID for each file
    counter = len(original_name_list)

# Rename
for i in range(0, len(original_name_list)):
    # Check extension
    extension = os.path.splitext(original_name_list[i])[1]
    # ! Enter your own exclusion rules here e.g. only rename files that are .pdf
    if extension != extension_check:
        continue

    # Rename the file
    # TODO: Change this to the name you want here
    new_name = current_dir + "\\" + header + str(i) + ".txt"

    os.rename(original_name_list[i], new_name)
