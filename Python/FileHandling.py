# Writing to a file
file_name = "sample.txt"
with open(file_name, "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy and powerful.\n")

# Reading from the file
print("Reading file contents:")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())