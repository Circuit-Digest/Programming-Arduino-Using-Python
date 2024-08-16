"""
This Python script reads analog sensor values from an Arduino board using the PyFirmata library. 
The sensor is connected to analog pin A0, and the program continuously reads and prints the sensor values to the console. 
The code runs in an infinite loop until interrupted by the user.

Features:
- Connects to an Arduino board via the specified COM port.
- Utilizes PyFirmata to read analog values from the sensor.
- Prints sensor values every second to the console.
- Gracefully handles user interruption and ensures proper cleanup.

Working:
- The script establishes a connection with the Arduino board using PyFirmata.
- An iterator is started to continuously update the input values from the analog pin.
- The sensor value is read in a loop and printed to the console.
- The loop runs indefinitely until a KeyboardInterrupt (Ctrl+C) is detected, at which point the program safely exits.
"""

from pyfirmata import Arduino, util
import time

# Establish connection to the Arduino board (replace 'COM8' with your specific port)
board = Arduino('COM8')

# Set up the sensor on analog pin A0 as an input
sensor_pin = board.get_pin('a:0:i')

# Start an iterator to continuously update the pin values from the Arduino
it = util.Iterator(board)
it.start()

try:
    while True:
        # Read the current sensor value from analog pin A0
        sensor_value = sensor_pin.read()
        
        # Print the sensor value to the console
        print(f"Sensor value: {sensor_value}")
        
        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    # Handle the program interruption by the user (Ctrl+C)
    print("Program interrupted by user.")

finally:
    # Safely exit the program and close the connection to the Arduino
    board.exit()
