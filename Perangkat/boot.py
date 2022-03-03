import network as MOD_NETWORK
from time import sleep
from bme680 import *
from machine import Pin, I2C
import esp
esp.osdebug(None)

import gc
gc.collect()
#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("kosan", "pwnyagakada")

while not GLOB_WLAN.isconnected():
  pass

#firebase example
import ufirebase as firebase
firebase.setURL("https://tugas-akhir-694bd-default-rtdb.firebaseio.com/")

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME680_I2C(i2c=i2c)
led = Pin(2, Pin.OUT)

while True:
  try:
    temp = float(round(bme.temperature, 2))
    #temp = (bme.temperature) * (9/5) + 32
    #temp = str(round(temp, 2)) + 'F'
    
    hum = float(round(bme.humidity, 2))
    led.value(1)
    gas = float(round((bme.gas/1000)/500, 2))
    firebase.patch("web", {"Temp": temp, "Hum": hum, "Voc": gas } )
    #firebase.addto("riwayat", {"Suhu": temp, "Hum": hum, "Voc": gas } )
    
  except OSError as e:
    print('Failed to read sensor.')
    led.value(0)
 
  sleep(10)























