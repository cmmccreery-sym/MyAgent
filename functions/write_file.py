from pathlib import Path

def write_file(working_directory, file_path, content):
    work_dir = Path(working_directory).resolve()
    file = (work_dir / file_path).resolve()

    if not file.is_relative_to(work_dir):
        return f'Error: Cannot write to "{file}" as it is outside the permitted working directory'
    
    try: 
        if not file.exists():
            with open(file, "w") as fp:
                fp.write(content)

        else:
            with open(file, "a") as fp:
                fp.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

