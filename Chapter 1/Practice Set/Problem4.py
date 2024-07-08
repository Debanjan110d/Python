import os

def list_directory_contents(path):
    return os.listdir(path)

# Example usage:
path = "."  # current working directory
contents = list_directory_contents(path)
print("Contents of", path, ":")
for item in contents:
    print(item)

    # Or 

    import os

# Specify the path to the directory you want to list
directory_path = "/"

# Get a list of all files and subdirectories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
# The output will be a list of all files and subdirectories in the specified directory.

#Note : Just " / "n means all files in your pc