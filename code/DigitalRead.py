"""
This Python script reads the state of a button connected to an Arduino board using PyFirmata.
The button is connected to digital pin 2, and the script will print the button's state to the console every second.
PyFirmata is used to communicate with the Arduino, and the script is designed to run indefinitely until interrupted by the user.

Features:
- Continuously reads and displays the state of a button connected to digital pin 2.
- Utilizes the PyFirmata Iterator to keep pin states updated.
- Includes exception handling to gracefully stop the program when interrupted.

Required:
- An Arduino board connected to your computer.
- A button connected to digital pin 2 on the Arduino.
- The PyFirmata library installed in your Python environment.

Working:
- The program starts by establishing a connection with the Arduino on the specified port.
- It then initializes the iterator, which continuously reads data from the Arduino.
- The main loop reads the state of the button every second and prints it to the console.
- The program listens for a KeyboardInterrupt (Ctrl+C) to safely terminate and disconnect from the Arduino.
"""


from pyfirmata import Arduino, util
import time

# Replace 'COM8' with your Arduino port
board = Arduino('COM8')  # Establish a connection to the Arduino board

# Set up digital pin 2 as an input pin for the button
button_pin = board.get_pin('d:2:i')  # 'd' stands for digital, '2' is the pin number, 'i' is for input

# Start the iterator to continuously read and update pin states
it = util.Iterator(board)
it.start()

try:
    while True:
        button_state = button_pin.read()  # Read the state of the button (True, False, or None)
        print(f"Button state: {button_state}")  # Print the current button state to the console
        time.sleep(1)  # Wait for 1 second before reading the button state again

except KeyboardInterrupt:
    print("Program interrupted by user.")  # Print a message if the program is interrupted

finally:
    board.exit()  # Safely exit and close the connection to the Arduino
