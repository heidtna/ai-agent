import os

def get_files_info(working_directory, directory="."):
    """
    Accepts a directory path and returns a string representing
    the contents of that directory, including all nested 
    directories and files.

    Args: 
        working_directory (str): The base directory acting as the root.
        directory (str, optional): Relative path to target directory within 'working_directory'.
        MUST BE INSIDE OF 'working_directory'.

    Returns:
        String representing the nested directories and files inside 'directory'.
    """
    abspath = os.path.abspath(
        os.path.join(working_directory, directory))

    # Validate path for LLM safety
    if directory != ".":
        if os.path.isfile(directory):
            return f'Error: "{directory}" is not a directory'
        
        if working_directory not in abspath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'        

    contents = os.listdir(abspath)

    output = []
    for content in contents:
        size = os.path.getsize(abspath)
        isfile = os.path.isfile(content)
        output.append(f"- {content}: file_size={size} bytes, is_dir={isfile}")
    
    return "\n".join(output)