import re
import os
import shutil

def modify_conf_file(filepath):
    """
    Modifies a .conf file, replacing all occurrences of "50ms" with "100ms".
    Creates a backup of the original file.
    """
    backup_filepath = filepath + ".bak"  # Create a backup file path

    # Create a backup of the original file
    try:
        shutil.copy2(filepath, backup_filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return
    except Exception as e:
        print(f"Error creating backup: {e}")
        return

    try:
        with open(filepath, 'r') as f_in, open(backup_filepath, 'w') as f_out:
            for line in f_in:
                # Use re.sub for substitution, handling potential variations
                modified_line = re.sub(r'\b50ms\b', '100ms', line)
                f_out.write(modified_line)
        # Replace the original file with the modified backup
        shutil.move(backup_filepath, filepath)

    except Exception as e:
        print(f"An error occurred during file modification: {e}")
        # Restore the backup if an error occurred
        if os.path.exists(backup_filepath):
            shutil.move(backup_filepath, filepath)

modify_conf_file("sprint-100.conf")