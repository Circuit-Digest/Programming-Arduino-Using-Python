"""
This Python script controls an LED connected to an Arduino board using PyFirmata.
The LED is connected to digital pin 3, and it will blink on and off with a 1-second interval.
PyFirmata is used to communicate with the Arduino, and the script is designed to run indefinitely until interrupted by the user.

Features:
- Turns the LED on and off in a loop with a 1-second delay.
- Utilizes the PyFirmata Iterator to continuously update pin states.
- Includes exception handling to gracefully stop the program when interrupted.

Required:
- An Arduino board connected to your computer.
- An LED connected to digital pin 3 on the Arduino.
- The PyFirmata library installed in your Python environment.

Working:
- The program starts by establishing a connection with the Arduino on the specified port.
- It then initializes the iterator, which continuously reads data from the Arduino.
- The main loop toggles the LED on and off with a 1-second delay.
- The program listens for a KeyboardInterrupt (Ctrl+C) to safely terminate and disconnect from the Arduino.
"""

from pyfirmata import Arduino, util
import time

# Replace 'COM8' with your Arduino port
board = Arduino('COM8')

# Set up digital pin 3 as an output pin for the LED
led_pin = board.get_pin('d:3:o')

# Start the iterator to continuously read and update pin states
it = util.Iterator(board)
it.start()

try:
    while True:
        led_pin.write(1)  # Turn LED on
        time.sleep(1)     # Wait for 1 second
        led_pin.write(0)  # Turn LED off
        time.sleep(1)     # Wait for 1 second

except KeyboardInterrupt:
    print("Program interrupted by user.")  # Print a message when interrupted

finally:
    board.exit()  # Safely exit and close the connection to the Arduino
