def write_log(message, log_file=r"C:\Users\Gintas\Documents\MANO IT\pathFinding\Blender_scripts\log.txt"):
    with open(log_file, 'a') as file:
        file.write(message + '\n')