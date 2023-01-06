
#   Writing to Files in Python

# If we try to open a file that doesn't exist, a new file is created.
# If a file already exists, its content is erased, and new content is added to the file.
# syntax : with open("text.txt", "w") as file_name:

with open("text1.txt", "w") as file2:

    # write contents to the test2.txt file
    file2.write('Created new file.')
    file2.write('\nWelcome here..!')

