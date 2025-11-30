from pathlib import Path

def get_file_content(working_directory, file_path):
    work_dir = Path(working_directory).resolve()
    file = (work_dir / Path(file_path)).resolve()

    if not file.is_relative_to(work_dir):
        return f'Error: Cannot read "{file}" as it is outside the permitted working directory'

    if not file.is_file():
        return f'Error: File not found or is not a regular file: "{file}"'
    
    # You're doing I/O now, This is where you need to check for every bizare error under the sun
    try:
        with open(file, "r") as fp:
            content = fp.read()

            if len(content) > 10000:
                content = content[:10000]
                content += '...File "{file}" truncated at 10000 characters'

            return content
    except Exception as e:
        return f"Error: {e}"



