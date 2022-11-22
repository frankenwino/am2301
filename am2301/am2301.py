import Adafruit_DHT  # https://github.com/adafruit/Adafruit_Python_DHT
from time import sleep
from typing import Tuple

class AM2301:
    """AM2301 Uses an AM2301 sensor to get ambient temperature and humidity."""

    def __init__(self, gpio_pin: int) -> None:
        """__init__ Constructor

        Args:
            gpio_pin (int): the GPIO pin the sensor is attached to.
        """
        self.gpio_pin = gpio_pin
        self.temp_celsius, self.humidity_percent = self.temperature_humidity()

    def temperature_humidity(self) -> Tuple[float, float]:
        """temperature_humidity uses the AM2301 sensor to get ambient temperature and humidity.

        Returns:
            tuple[float,float]: humidity, temperatre in celsius
        """
        sensor = Adafruit_DHT.AM2302
        successful_reading = False

        while successful_reading is False:
            humidity, temp_celsius = Adafruit_DHT.read_retry(sensor, self.gpio_pin)
            if humidity is None:
                print(f"Humidity sensor returning {humidity}, Trying again...")
                sleep(1)
            elif humidity > 100 or humidity < 0:
                print(
                    f"Humidity sensor returning {humidity}% humidity. Trying again..."
                )
                sleep(1)
            else:
                successful_reading = True

        # humidity, temp_celsius = Adafruit_DHT.read_retry(sensor, gpio_pin)

        humidity = round(humidity, 1)
        temp_celsius = round(temp_celsius, 1)

        return temp_celsius, humidity

    def temperature(self) -> float:
        """temperature gets the ambient temperature in celsius

        Returns:
            float: temperature in celsius
        """
        return self.temp_celsius

    def humidity(self) -> float:
        """humidity gets the ambient humidity

        Returns:
            float: humidity %
        """
        return self.humidity_percent


if __name__ == "__main__":
    gpio_pin = 14
    a = AM2301(gpio_pin=gpio_pin)

    temp_celsius = a.temperature()
    humidity = a.humidity()

    print("Humidity:\t{}%".format(humidity))
    print("Celsius:\t{}c".format(temp_celsius))