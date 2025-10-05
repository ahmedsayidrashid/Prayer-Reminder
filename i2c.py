"""
This script checks if it's time for any prayer and displays a message on an LCD.
"""

import time

import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

from main import put_all_together


# Initialize the LCD (adjust parameters as needed)
lcd = CharLCD(i2c_expander="PCF8574", address=0x27, port=1, cols=16, rows=2, charmap="A00")

# Setup GPIO

USER_BUTTON_GPIO_PIN = 27  # GPIO pin number for the user button

GPIO.setmode(GPIO.BCM)

# Use GPIO USER_BUTTON_GPIO_PIN for the button input
GPIO.setup(USER_BUTTON_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def write_to_lcd(message: str, display_time: int = 5) -> None:
    """
    This method writes a message to the LCD display for the specified display time (default is 5).

    :param message: Message to display on the LCD
    :param display_time: Time in seconds to display the message (default is 5)
    :return: None
    """
    lcd.clear()
    lcd.write_string(message)
    time.sleep(display_time)
    lcd.clear()


def bring_gpio_high(pin_number: int) -> None:
    """
    This method brings a GPIO pin high(for LED) until the user button is pressed. Meant to be a ack signal of prayer time.
    :param pin_number: GPIO pin number to bring high
    :return: None
    """
    print(f"Bringing GPIO {pin_number} high.")
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number, GPIO.HIGH)


def ack_prayer_time(pin_number: int) -> None:
    """
    This method waits for the user button to be pressed to bring the GPIO pin low.
    :param pin_number: GPIO pin number to bring low
    :return: None
    """
    while True:
        time.sleep(1)
        if GPIO.input(pin_number) == GPIO.LOW:  # Button pressed
            print("Button pressed, bringing GPIO low and exiting...")
            GPIO.output(22, GPIO.LOW)
            break
        else:
            print("Waiting for button press to bring GPIO low...")


if __name__ == "__main__":
    try:
        message = put_all_together()
        if message:
            bring_gpio_high(22)
            ack_prayer_time(USER_BUTTON_GPIO_PIN)
        write_to_lcd(message)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
        # Clean up GPIO settings
        lcd.close()  # Close the LCD when done
