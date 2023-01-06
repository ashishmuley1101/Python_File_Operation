
#   appending text to Files at the end in Python

# Open a file for appending at the end of the file without truncating it.
# Creates a new file if it does not exist.
# syntax : with open("text.txt", "a") as file_name:  where "a" = append

with open("text1.txt", "a") as file2:

    # appending contents to the test2.txt file
    file2.write('\nappending the new to check the code.')

