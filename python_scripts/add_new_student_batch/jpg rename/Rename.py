import os

# Set the directory containing the .jpg files
directory = "\students\\e22\\ori"  # Replace with your directory path
directory_1 = "\students\\e22\\rename"

# Get all files in the directory
files = os.listdir(directory)

# Filter for .jpg files
jpg_files = [f for f in files if f.lower().endswith(".jpg")]

# Rename files
for index, file in enumerate(jpg_files):
    # Define the new file name, e.g., "image_1.jpg"
    new_name = f"e22{file}"

    # Get the full file paths
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory_1, new_name)

    # Rename the file
    os.rename(old_path, new_path)

    print(f"Renamed {file} to {new_name}")
