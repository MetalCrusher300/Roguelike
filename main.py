from useCommand import *

def main():
# Main loop to continuously take user input and process it
    while True:
        try:
            UserInputFunc = str(input(''))  # Get user input
            terminalInput(UserInputFunc)  # Process the input
        except KeyboardInterrupt:
            print("\nExiting...")
            break  # Exit the loop on Ctrl+C
        # except Exception as e:
        #     print(f"\tAn error occurred: {e}")

if __name__ == '__main__':
    main()