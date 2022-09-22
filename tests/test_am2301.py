#!/usr/bin/env python

"""Tests for `am2301` package."""
from am2301 import am2301


def test_temperature_humidity():
    # Arrange
    gpio_pin=4

    # Act
    temp_celsius, humidity = am2301.temperature_humidity(gpio_pin=gpio_pin)

    # Assert
    assert type(temp_celsius) is float
    assert type(humidity) is float
