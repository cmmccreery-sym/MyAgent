from pathlib import Path

def get_files_info(working_directory, directory="."):
    working_path = Path(working_directory).absolute()
    proposed_dir = Path(directory) 

    if (working_path / proposed_dir).exists() and (working_path / proposed_dir).is_dir():
        curr_path = (working_path / proposed_dir).resolve()
    else:
        return f"Error: {directory} is not a directory"

    if not curr_path.is_relative_to(working_path):
        # Were outside the provided directory. Abort
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    result_str_lst = []
    for p in curr_path.iterdir():
        result_str_lst.append(f"- {p}: file_size={p.stat().st_size}, is_dir={p.is_dir()}")

    return "\n".join(result_str_lst)


