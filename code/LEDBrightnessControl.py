"""
This Python script uses the PyFirmata library to control the brightness of an LED based on the reading from a potentiometer.
The LED is connected to a PWM-enabled digital pin, and the potentiometer is connected to an analog input pin on the Arduino.

Features:
- Connects to an Arduino board via the specified COM port.
- Reads analog input from a potentiometer to determine the LED brightness.
- Maps the potentiometer value (0 to 1) to a PWM value (0 to 255) to adjust the LED brightness.
- Continuously updates the LED brightness based on the potentiometer input.
- Gracefully handles user interruptions and ensures proper cleanup.

Working:
- Establishes a connection with the Arduino board and sets up pin configurations.
- Starts an iterator thread to manage data flow between the board and the script.
- Continuously reads the analog value from the potentiometer.
- Maps the potentiometer value to a PWM range suitable for LED brightness control.
- Adjusts the LED brightness in real-time based on the potentiometer input.
- Safely exits the program on user interruption (Ctrl+C) and closes the board connection.

"""

from pyfirmata import Arduino, util

# Change the port to the one your Arduino is connected to
board = Arduino('COM3')

# Define the pin numbers
led_pin = board.get_pin('d:9:p')  # 'd' for digital, 9 is the pin number, 'p' for PWM
potentiometer_pin = board.get_pin('a:0:i')  # 'a' for analog, 0 is the pin number, 'i' for input

# Start an iterator thread so that the board doesn't overflow with data
it = util.Iterator(board)
it.start()

try:
    while True:
        # Read the value from the potentiometer (0 to 1.0)
        pot_value = potentiometer_pin.read()

        if pot_value is not None:
            # Map the potentiometer value (0-1) to a PWM value (0-255)
            brightness = pot_value * 255
            led_pin.write(brightness / 255)  # Write PWM value to LED

except KeyboardInterrupt:
    # Handle user interruption (Ctrl+C) gracefully
    print("Program interrupted by user.")

finally:
    # Safely exit the program and close the connection to the Arduino
    board.exit()
