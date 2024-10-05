def calculate_directory_size(fs, path):
    keys = path.split('.')  # Split the path by dots to get the hierarchy
    current_dir = fs  # Start at the root of the file system

    # Traverse the directory structure using the path
    for key in keys:
        if key in current_dir:
            current_dir = current_dir[key]  # Move to the next directory
        else:
            return "Directory not found"  # If the directory doesn't exist, return an error message

    # Now we need to calculate the total size of files in the current directory
    def get_total_size(directory):
        total_size = 0
        for item, value in directory.items():
            if isinstance(value, dict):  # If it's a subdirectory, recurse into it
                total_size += get_total_size(value)
            elif isinstance(value, int):  # If it's a file, add its size
                total_size += value
        return total_size

    total_size = get_total_size(current_dir)
    return f"Total size: {total_size}"


# Example Usage:

# Example file system structure:
file_system = {
    "root": {
        "dir1": {
            "subdir1": {
                "file1": 500,
                "file2": 500
            },
            "subdir2": {
                "file3": 300
            }
        },
        "dir2": {
            "subdir3": {
                "file4": 800
            },
            "subdir4": {
                "subsubdir5": {
                    "file5": 1000,
                    "file6": 2400
                }
            }
        }
    }
}

# Input-1:
path1 = "root.dir1.subdir1"
print(calculate_directory_size(file_system, path1))  # Output: "Total size: 1000"

# Input-2:
path2 = "root.dir2.subdir4.subsubdir5"
print(calculate_directory_size(file_system, path2))  # Output: "Total size: 3400"
