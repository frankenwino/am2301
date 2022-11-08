#!/usr/bin/env python

"""Tests for `am2301` package."""
from am2301.am2301 import AM2301 as AM2301
import platform
import subprocess

def test_temperature_humidity():
    # Arrange
    gpio_pin=14
    a = AM2301(gpio_pin=gpio_pin)

    # Act
    temp_celsius = a.temperature
    humidity = a.humidity

    # Assert
    assert isinstance(temp_celsius, float)
    assert isinstance(humidity, float)
