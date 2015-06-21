import RPi.GPIO as GPIO
import time
import os

# Pin-Nummer wie auf dem Raspberry verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 18 als Input deklarieren und Pull-Down Widerstand aktivieren
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# Pin 7 als Output deklarieren 
GPIO.setup(7, GPIO.OUT)

# ISR
def Interrupt(channel):
	os.system("sudo shutdown -h now")
		
# Interrupt Event hinzufuegen. Pin 18, auf steigende Flanke reagieren und ISR "Interrupt" deklarieren
GPIO.add_event_detect(18, GPIO.RISING, callback = Interrupt, bouncetime = 200)

# Endlosschleife
while True:
  time.sleep(1)
