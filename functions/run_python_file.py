import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    """
    THIS METHOD WILL RUN ARBITRARY CODE. NO SECURITY CHECKS ARE BEING 
    PERFORMED TO ENSURE THE CODE IS SAFE. RUN AT YOUR OWN RISK.

    Takes a python file within 'working_directory' and executes the code inside.
    'file_path' must be located within the working_directory to limit access to 
    other files.

    Args:
        working_directory (str): Directory to act as root. Nothing outside of it can be accessed.
        file_path (str): Path to file intended to be written to.
        args (Array):

    Returns:
        A string indicating the status of the code execution.
    """
    abspath = os.path.abspath(
        os.path.join(working_directory, file_path)
    )    

    # Perform checks to ensure the file exists, is within working_directory, and is a Python file
    if working_directory not in abspath:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    if not os.path.exists(abspath):
        return f'Error: File "{file_path}" not found.'
    if not abspath.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    outputStr = ""
    try:
        completed_process = subprocess.run(
            ["python3", abspath, *args], 
            timeout=30, 
            capture_output=True)
        
        out = "STDOUT:\n" + completed_process.stdout.decode() if completed_process.stdout else ""
        err = "STDERR: " + completed_process.stderr.decode() if completed_process.stderr else ""

        if not out and not err:
            return "No output produced"
        
        outputStr += out + err

        if completed_process.returncode != 0:
            outputStr += f"Process exited with code {completed_process.returncode}"

    except Exception as e:
        return f'Error: executing Python file: {e}'
    
    return outputStr