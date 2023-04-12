# Take inputs from the user of a file name and print the extension of it

file_name=input("Enter the name of the file: ")
extension_name=file_name.split(".")
print(extension_name[-1])
