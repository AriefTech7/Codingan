import os
import subprocess
import shutil

# Automating repetitive tasks
def backup_files(src_dir, dst_dir):
    """Backup files from source directory to destination directory"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)
        shutil.copy2(src_file, dst_file)
    print("Backup complete.")

# Handling configurations
def update_config(config_file, key, value):
    """Update a configuration file with a new key-value pair"""
    with open(config_file, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(key + '='):
            lines[i] = f"{key}={value}\n"
            break
    else:
        lines.append(f"{key}={value}\n")
    with open(config_file, 'w') as file:
        file.writelines(lines)
    print(f"Updated {key} in {config_file}")

# Integrating different tools
def run_command(command):
    """Run a shell command and return the output"""
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

# Example usage
backup_files('/path/to/source', '/path/to/backup')
update_config('config.ini', 'database_host', 'localhost')
result = run_command('git status')
print(result)