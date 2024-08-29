import os


def write_log(message, log_name="log.txt"):
    current_script_dir = os.path.dirname(__file__)
    script_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
    file_path = os.path.join(script_dir, 'data', log_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'a') as file:
        file.write(message + '\n')