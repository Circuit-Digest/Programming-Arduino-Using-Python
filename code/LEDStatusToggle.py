import time
from pyfirmata import Arduino, util

# Change the port to the one your Arduino is connected to
board = Arduino('COM3')

# Define the pin numbers
led_pin = board.get_pin('d:13:o')  # 'd' for digital, 13 is the pin number, 'o' for output
button_pin = board.get_pin('d:2:i')  # 'd' for digital, 2 is the pin number, 'i' for input

# Start an iterator thread so that the board doesn't overflow with data
it = util.Iterator(board)
it.start()

# Initialize variables
led_state = False  # Track the state of the LED
button_state = False  # Track the previous button state

def toggle_led():
    global led_state
    if led_state:
        led_pin.write(0)  # Turn off LED
    else:
        led_pin.write(1)  # Turn on LED
    led_state = not led_state

try:
    while True:
        current_button_state = button_pin.read()  # Read the state of the button

        if current_button_state is True and button_state is False:
            # Button was pressed
            toggle_led()
            time.sleep(0.2)  # Debounce delay

        button_state = current_button_state  # Update the button state

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    board.exit()  # Gracefully close the board connection
