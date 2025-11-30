from pathlib import Path
from subprocess import run, CalledProcessError

def run_python_file(working_directory, file_path, args=[]):
    work_dir = Path(working_directory).resolve()
    file = (work_dir / Path(file_path)).resolve()

    if not file.is_relative_to(work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not file.exists():
        return f'Error: File "{file_path}" not found.'

    if not file.suffix == ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = run(
                ["python3", file.as_posix()] + args,
                timeout=30,
                text=True,
                capture_output=True,
                check=True
        )

        _stdout = completed_process.stdout
        _stderr = completed_process.stderr
        _return_code = completed_process.returncode

        return f"Process exited with {_return_code}\n\tSTDOUT: {_stdout}\n\tSTDERR: {_stderr}" if (_stdout or _stderr) else "No output produced"

    except CalledProcessError as e:
        return f"Error: executing Python file: {e}"
