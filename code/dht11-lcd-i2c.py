import lcddriver
# from time import *
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
 
lcd = lcddriver.lcd()
lcd.lcd_clear()

while True:
    time.sleep(1)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
            lcd.lcd_display_string('Temp.: {0:0.1f} C'.format(temperature), 1)
            lcd.lcd_display_string('Humidity: {0:0.1f} %'.format(humidity), 2)
    else:
            print('Fehler beim Einlesen der Daten. Starte einen weiteren Versuch!')
 
time.sleep(1)
