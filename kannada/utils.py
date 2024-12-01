from shared import variables

def process_line(line, command_map, lines_iter=None):
    """Processes a single line of Kannada code."""
    if not line or line.startswith("#"):  # Ignore empty lines and comments
        return

    # Replace variables in the line
    for var_name, value in variables.items():
        line = line.replace(var_name, str(value))

    command, *args = line.split(maxsplit=1)
    args = args[0] if args else ""

    if command in command_map:
        command_map[command](args, process_line, command_map)
    else:
        print(f"Unknown command: {command}")
