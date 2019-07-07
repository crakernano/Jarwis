"""Acceso a los sensores locales """
import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def getTemerature():
    temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if temperature is not None: 
        return temperature

def getHumedity():
    humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None: 
        return humidity

