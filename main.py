
#   Python File writelines() Method

# The writelines() method writes the items of a list to the file.
# syntax : file.writelines(list)

with open("text1.txt", "a") as file2:
    file2.writelines(["\nSee you soon!", "\nOver and out."])  # list datatype


