import os

def write_file(working_directory, file_path, content):
    """
    Writes contents to a file specified within the working directory. Overwrites the file
    if it already exists.

    Args:
        working_directory (str): Directory to act as root. Nothing outside of it can be accessed.
        file_path (str): Path to file intended to be written to.
        content (str): The text to be written to the file.

    Returns: A string indicating the failure or success of the writing process.
    """
    abspath = os.path.abspath(
        os.path.join(working_directory, file_path)
    )

    if working_directory not in abspath:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # Create any parent directories in path if needed.
        path_parent_dir = os.path.dirname(abspath)
        os.makedirs(path_parent_dir, exist_ok=True)

        file_exists = os.path.exists(abspath)

        # Open/create the file for writing
        with open(abspath, "w") as f:
            f.write(content)
    except FileNotFoundError as e:
        return f'Error: {e}'
    
    status = "overwritten" if file_exists else "created"
    return f'File successfully {status}: "{file_path}". ({len(content)} characters written)'