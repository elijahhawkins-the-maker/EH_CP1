import sys
import time

def slow_print(text, delay=0.05):
    """
    Prints the given text character by character with a delay.

    Args:
        text (str): The string to be printed slowly.
        delay (float): The time in seconds to wait between printing each character.
                       Default is 0.05 seconds.
    """
    for char in text:
        sys.stdout.write(char)  # Write the character to standard output
        sys.stdout.flush()      # Ensure the character is immediately displayed
        time.sleep(delay)       # Pause for the specified delay
    print()  # Print a newline character at the end of the text

# Example usage:
slow_print("Hello, world! This text is appearing slowly.")
slow_print("Another example with a different speed.", delay=0.1)