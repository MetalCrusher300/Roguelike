from CommandFunctions import *

def terminalInput(userInput):
    """
    Processes the user input and executes the corresponding function.
    """
    userFunction = userInput.split()  # Split the input into a list of arguments
    if not userFunction:  # If the input is empty, do nothing
        return

    # Get the corresponding action and length requirement from the dictionary
    action = function_mappings.get(userFunction[0])

    if action:
        required_length, func = action["func"]
        # Check if the number of arguments matches the required length
        if required_length is None or (isinstance(required_length, tuple) and len(userFunction) in required_length) or len(userFunction) == required_length:
            # Pass the arguments to the function (excluding the command itself)
            func(*userFunction[1:])
        else:
            print(f"\tInvalid number of arguments for '{userFunction[0]}'.")
    else:
        print(f"\tUnknown command '{userFunction[0]}'.")