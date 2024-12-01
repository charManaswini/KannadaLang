# kannada/interpreter.py

import sys
from kannada.commands import get_command_map
from kannada.utils import process_line

def execute_kannada_code(file_path):
    """Executes Kannada code from a file."""
    command_map = get_command_map(process_line)  # Dynamically fetch command map
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = iter(file.readlines())  # Create an iterator for lines
        for line in lines:
            process_line(line.strip(), command_map, lines)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m kannada.interpreter <file.knd>")
        return
    
    file_path = sys.argv[1]
    execute_kannada_code(file_path)

if __name__ == "__main__":
    main()
