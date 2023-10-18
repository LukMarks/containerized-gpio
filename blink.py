import RPi.GPIO as gpio
import time
import logging
import os


log_levels = {
	"info": logging.INFO,
	"warning": logging.WARNING,
	"debug": logging.DEBUG
}

logging.basicConfig(
                    filename=os.getenv("LOG_FILE", "/home/lucas/projects/container-gpio/logs/local_blink.log"),
                    format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=log_levels.get(os.getenv("LOGLEVEL", "").lower(),
                                         logging.INFO)
                   )

led_pin = int(os.getenv("LEDPIN", 8))


logging.info("Start Board Setup")
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
logging.info("Finished Board Setup")

def blink_led(pin:int, interval:int) -> None:

	gpio.output(pin, gpio.HIGH)
	logging.info("Set Pin " + str(pin) + " to HIGH")
	time.sleep(interval)
	gpio.output(pin, gpio.LOW)
	logging.info("Set Pin " + str(pin) + " to LOW")
	time.sleep(interval)

try:

	gpio.cleanup()
	gpio.setup(led_pin, gpio.OUT, initial=gpio.LOW)

	while True:
		blink_interval = int(os.getenv("INTERVAL", 1))
		blink_led(pin=led_pin, interval=blink_interval)
except KeyboardInterrupt:
	logging.info("Closing blink_pin.py routine")
	gpio.cleanup()
	logging.info("Cleared Board Configurations")
