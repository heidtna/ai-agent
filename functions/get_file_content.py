import os
from config import *

def get_file_content(working_directory, file_path):
    abspath = os.path.abspath(
        os.path.join(working_directory, file_path)
    )

    if working_directory not in abspath:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abspath, "r") as f:
        content_string = f.read(READ_FILE_MAX_CHAR)
    
    if len(content_string) == READ_FILE_MAX_CHAR:
        content_string = content_string[:-1] 
        content_string += f' [... File "{file_path}" truncated at 10000 characters]'

    return content_string