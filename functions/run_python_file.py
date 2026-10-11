import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        is_valid = os.path.commonpath([working_dir_abs,target_path]) == working_dir_abs
        if is_valid== False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path.endswith(".py")== False:
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args is not None:
            command.extend(args)
        proc =  subprocess.run(command,cwd=working_dir_abs,capture_output=True,text=True,timeout=30) 
        report = ""
        if proc.returncode!=0:
            report+= f"Process exited with code {proc.returncode}"+"\n"
        if proc.stdout== "" and proc.stderr=="":
            return f"No output produced"
        if proc.stdout!="":
            report+= "STDOUT:"+proc.stdout+"\n"
        if proc.stderr!="":
            report+= "STDERR:"+proc.stderr+"\n"
    except Exception as e:
        return(f"Error: executing Python file: {e}")
    return report

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the Python file to run, relative to the working directory",
                        },
                        "args":{
                            "type": "array",
                            "items":{"type":"string"},
                            "description":"Optional list of arguments to pass to the Python script",
                        },
                    },
            "required":["file_path"],
        }
    },
}


