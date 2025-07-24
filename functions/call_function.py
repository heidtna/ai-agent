from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
    function_dict = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    # We don't let the LLM set the working directory, so set it here by adding it to keyword arguments dictionary
    function_call_part.args["working_directory"] = "calculator"
    
    try:
        if verbose:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f" - Calling function: {function_call_part.name}")

        function_name = function_dict[function_call_part.name]
        #print(f"FUNCTION_NAME: {function_name}")
        function_result = function_name(**function_call_part.args)
        #print(f"FUNCTION_RESULT: {function_result}")
    
    # Invalid function name
    except KeyError as e:
        print(f"Error: {e}.\nFunction '{function_call_part.name}' not found.")
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name.__name__,
                    response={"error": f"Unkown function: {function_name.__name__}"},
                )
            ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name.__name__,
                response={"result": function_result},
            )
        ],
    )