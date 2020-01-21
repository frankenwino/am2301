"""Main module."""
import Adafruit_DHT # https://github.com/adafruit/Adafruit_Python_DHT
from time import sleep

def temperature_humidity():
    """
    Returns
        humidity    float
                    humidity data generated by AM2301
        temperature float
                    temperature data in celsius generated by AM2301
    """
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    while humidity > 100 or humidity is None:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        sleep(1)
    humidity = round(humidity, 1)
    temperature = round(temperature, 1)

    return temperature, humidity


pin = 21 # GPIO21 aka Pin 40
sensor = Adafruit_DHT.AM2302 

if __name__ == '__main__':
    temperature, humidity = temperature_humidity()
    print('Humidity:\t{}%'.format(humidity))
    print('Temperature:\t{}c'.format(temperature))
