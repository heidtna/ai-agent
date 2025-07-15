import os
from config import *

def get_file_content(working_directory, file_path):
    """
    Accepts a working directory and path to a file then reads the content 
    and returns a string of those contents up to a maximum character limit.

    Args: 
        working_directory (str): The base directory acting as the root.
        directory (str, optional): Relative path to target file within 'working_directory'.
        MUST BE INSIDE OF 'working_directory'.

    Returns:
        String representing the contents of the file.
    """
    
    abspath = os.path.abspath(
        os.path.join(working_directory, file_path)
    )

    if working_directory not in abspath:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abspath, "r") as f:
            content_string = f.read(READ_FILE_MAX_CHAR)
    except FileNotFoundError as e:
        return f'Error: {e}'
    
    if len(content_string) == READ_FILE_MAX_CHAR:
        content_string = content_string[:-1] 
        content_string += f' [... File "{file_path}" truncated at 10000 characters]'

    return content_string