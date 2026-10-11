import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        is_valid = os.path.commonpath([working_dir_abs,target_path])==working_dir_abs
        if is_valid == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_path):
              return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(target_path)
        os.makedirs(parent_dir,exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
        
    except Exception as e:
                return(f"Error:{e}")
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Check if the file path exists is in the permitted working directory and it is not a directory itself",
        "parameters": {
            "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "File to write in the working directory (default place to write is the working directory itself)",
                        },
                        "content":{
                              "type":"string",
                              "description": "content we want to write on the file."
                        }
                    },
            "required":["file_path","content"],
        },
    },
}
