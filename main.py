
#    Use of with...open

# The with...open syntax to automatically close the file.
# syntax : with open() as file_name

with open("text.txt") as file1: # by default file on read mode open("text.txt", "r")

    # read the file
    read_content = file1.read()
    print(read_content)

