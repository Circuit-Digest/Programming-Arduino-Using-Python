"""
This Python script controls the brightness of an LED connected to an Arduino board using the PyFirmata library. 
The LED is connected to digital pin 5, which supports PWM (Pulse Width Modulation).
The script gradually increases and decreases the LED brightness, creating a fading effect.

Features:
- Connects to an Arduino board via the specified COM port.
- Utilizes PyFirmata to control the PWM output on a digital pin.
- Smoothly increases and decreases LED brightness in a loop.
- Gracefully handles user interruption and ensures proper cleanup.

Working:
- The script establishes a connection with the Arduino board using PyFirmata.
- An iterator is started to continuously update the pin values from the Arduino.
- The LED brightness is adjusted using PWM, cycling through values from 0 (off) to 255 (full brightness).
- The script creates a fading effect by incrementing and then decrementing the brightness in a loop.
- The loop runs indefinitely until a KeyboardInterrupt (Ctrl+C) is detected, at which point the program safely exits.
"""

from pyfirmata import Arduino, util
import time

# Establish connection to the Arduino board (replace 'COM8' with your specific port)
board = Arduino('COM8')

# Set up the LED on digital pin 5 as a PWM output
led_pin = board.get_pin('d:5:p')  # Digital pin 5 as PWM output

# Start an iterator to continuously update the pin values from the Arduino
it = util.Iterator(board)
it.start()

try:
    while True:
        # Gradually increase the LED brightness from 0 to 255
        for brightness in range(256):
            led_pin.write(brightness / 255.0)  # Set LED brightness (0 to 1.0 scale)
            # time.sleep(0.01)  # Small delay for a visible effect

        # Gradually decrease the LED brightness from 255 to 0
        for brightness in range(255, -1, -1):
            led_pin.write(brightness / 255.0)  # Set LED brightness (0 to 1.0 scale)
            # time.sleep(0.01)  # Small delay for a visible effect

except KeyboardInterrupt:
    # Handle the program interruption by the user (Ctrl+C)
    print("Program interrupted by user.")

finally:
    # Safely exit the program and close the connection to the Arduino
    board.exit()
