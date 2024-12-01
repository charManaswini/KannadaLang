# kannada/commands.py
from shared import variables

def helu_guru(message):
    """Prints a message prefixed with 'Guru:'."""
    print(f"Guru: {message}")

def print_madi(value):
    """Prints a given value, evaluating expressions if necessary."""
    try:
        # Evaluate the string if it contains expressions
        evaluated_value = eval(value) if value.startswith("str(") else value
        print(evaluated_value)
    except Exception as e:
        print(f"Error evaluating print_madi: {e}")

def calculate(expression):
    """Evaluates an arithmetic expression and prints the result."""
    try:
        # Safely evaluate the arithmetic expression
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error in calculate: {e}")


def madu_loop(args, process_line, command_map):
    """Executes a loop with the loop index accessible as _ (dynamic_loop_var)."""
    try:
        count, code = args.split(",", 1)
        count = int(count.strip())
        for i in range(1, count + 1):  # Loop from 1 to count
            dynamic_loop_var = i  # Define _ dynamically as loop variable
            command, *cmd_args = code.split(maxsplit=1)
            if cmd_args:
                cmd_args = cmd_args[0].replace("_", str(dynamic_loop_var))
                processed_code = f"{command} {cmd_args}"
            else:
                processed_code = command
            process_line(processed_code.strip(), command_map)
    except ValueError:
        print(f"Invalid loop syntax: {args}")
    except Exception as e:
        print(f"Error in madu_loop: {e}")

def thagisu_mahiti(prompt):
    """Takes input from the user and prints the entered value."""
    try:
        user_input = input(f"{prompt}: ")
        return user_input  # Return the input for other commands if needed
    except Exception as e:
        print(f"Error in thagisu_mahiti: {e}")
        return None


def nirdharisu(args):
    """Defines a variable and stores its value."""
    try:
        var_name, value = args.split("=", 1)
        var_name = var_name.strip()
        value = eval(value.strip())  # Evaluate the value (e.g., arithmetic expressions)
        variables[var_name] = value
        print(f"Variable '{var_name}' set to {value}")
    except Exception as e:
        print(f"Error in nirdharisu: {e}")


def nodu_condition(args, process_line, command_map):
    """Executes a conditional statement with dynamic support for `_`."""
    try:
        # Split condition and code
        condition, code = args.split(",", 1)

        # Replace `_` dynamically in the condition and code
        condition = condition.replace("_", "dynamic_loop_var")
        code = code.replace("_", "dynamic_loop_var")

        # Evaluate the condition dynamically
        if eval(condition):
            process_line(code.strip(), command_map)
    except Exception as e:
        print(f"Error in nodu_condition: {e}")
        

def get_command_map(process_line):
    return {
        "helu_guru": lambda args, *_: helu_guru(args),
        "print_madi": lambda args, *_: print_madi(args),
        "thagisu_mahiti": lambda args, *_: thagisu_mahiti(args),
        "nirdharisu": lambda args, *_: nirdharisu(args),  # Define variable
        "madu_loop": lambda args, process_line, command_map, *_: madu_loop(args, process_line, command_map),
        "nodu_condition": lambda args, process_line, command_map, *_: nodu_condition(args, process_line, command_map),
        "calculate": lambda args, *_: calculate(args),
    }
