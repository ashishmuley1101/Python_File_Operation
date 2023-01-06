
#   Python File readline() Method

# The readline() method returns one line from the file.
# syntax : file.readline(size)
# size	Optional. The number of bytes from the line to return. Default -1,
# which means the whole line.

with open("text1.txt", "r") as file2:

    # readline() printing the first line from the file
    print(file2.readline())

# Output : Created new file.
