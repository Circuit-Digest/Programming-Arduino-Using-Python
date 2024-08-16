"""
This Python script controls a servo motor connected to an Arduino board using the PyFirmata library.
The servo motor is connected to digital pin 9 on the Arduino, and the script makes the servo sweep back and forth between 0 and 180 degrees.

Features:
- Connects to an Arduino board via the specified COM port.
- Utilizes PyFirmata to control the servo motor's position.
- Sweeps the servo motor smoothly from 0 to 180 degrees and back.
- Gracefully handles user interruption and ensures proper cleanup.

Working:
- The script establishes a connection with the Arduino board using PyFirmata.
- The servo motor is controlled by sending angles (0 to 180 degrees) to the specified pin.
- The script continuously sweeps the servo from 0 to 180 degrees and back to 0 degrees in a loop.
- The loop runs indefinitely until a KeyboardInterrupt (Ctrl+C) is detected, at which point the program safely exits.
"""

import time
from pyfirmata import Arduino

# Change the port to the one your Arduino is connected to
board = Arduino('COM8')

# Set the pin where the servo is connected (e.g., pin 9)
servo_pin = board.get_pin('d:9:s')  # 'd' for digital, 9 is the pin number, 's' for servo

def sweep_servo():
    try:
        while True:
            # Sweep from 0 to 180 degrees
            for angle in range(0, 181, 1):
                servo_pin.write(angle)  # Move servo to the specified angle
                time.sleep(0.001)  # Adjust the speed of the sweep

            # Sweep back from 180 to 0 degrees
            for angle in range(180, -1, -1):
                servo_pin.write(angle)  # Move servo to the specified angle
                time.sleep(0.001)

    except KeyboardInterrupt:
        # Handle the program interruption by the user (Ctrl+C)
        print("Sweep interrupted by user.")

    finally:
        # Safely exit the program and close the connection to the Arduino
        board.exit()

# Run the sweep function
sweep_servo()
