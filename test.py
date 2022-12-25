import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

LED_pin = 2
sw_pin = 17
gpio.setup(LED_pin, gpio.OUT)
gpio.setup(sw_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

try:
    while True:
        if gpio.input(sw_pin) == gpio.HIGH:
            gpio.output(LED_pin, gpio.HIGH)
        else:
            gpio.output(LED_pin, gpio.LOW)

finally:
    gpio.cleanup()