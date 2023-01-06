
#   Python File readlines() Method

# Return all lines in the file, as a list where each line is an item in the list object:
# syntax : file.readlines(hint)
# hint	Optional. If the number of bytes returned exceed the hint number, no more lines will be returned.
# Default value is  -1, which means all lines will be returned.

with open("text1.txt", "r") as file2:

    # readlines() printing the all lines from the file in list datatype.
    print(file2.readlines())

# Output : ['Created new file.\n', 'Welcome here..!\n', 'appending the new to check the code.']
