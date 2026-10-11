import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs,directory))
    valid_target_dir = os.path.commonpath([working_dir_abs,target_dir]) == working_dir_abs
    try:
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'


        os_dir = os.listdir(target_dir)
        result =[]
        for item in os_dir:
            try:
                item_path = os.path.join(target_dir, item)     
                size =(os.path.getsize(item_path))
                result.append(f"-{item}: file_size={size}, is_dir={os.path.isdir(item_path)}")

            except OSError as err:
                 return (f"Error:{err}")
                
        return "\n".join(result)
                
    except Exception as e:
            return(f"Error:{e}")

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
            


        
