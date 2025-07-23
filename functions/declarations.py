from google.genai import types

# Declarations to tell LLM what functions are available.
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. Use '.' for the root/current working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Accepts a path to a file, then reads the content and returns a string of those contents up to a maximum character limit, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from which to retrieve the contents."
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Takes a python file within 'working_directory' and executes the code inside. 'file_path' must be located within the working_directory to limit access to other files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from which to retrieve the contents."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING), # Need this to keep LLM from complaining about not being given params.
                description="An array of optional string parameters. If not provided, default to None."
            )
        },
        required=["file_path"], # This probably helps, too.
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=" Writes contents to a file specified within the working directory. Overwrites the file if it already exists.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from which to retrieve the contents."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text to be written to the file."
            )
        },
    ),
)

available_functions = types.Tool(
    function_declarations = [
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)