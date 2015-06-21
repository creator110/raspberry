# Zwei LED's blinken abwechselnd
# die gruene LED kann so angeschlossen werden
# bei der roten LED wird ein 200 Ohm Wiederstand angschlossen,
# weil die LED sonst zerstoert wird

import time
import RPi.GPIO as GPIO

# Pin-Nummer wie auf dem Raspberry verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 40 (GPIO 21) und Pin 33 (GPIO 13) als Output deklarieren
GPIO.setup(40, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

# Dauerschleife fuer das Blinken
while True:
        # LED-gruen aus, LED-rot an
        GPIO.output(40, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        # 0,2 Sekunden warten
        time.sleep(0.2)
        # LED-gruen an, LED-rot aus
        GPIO.output(40, GPIO.HIGH)
		GPIO.output(7, GPIO.LOW)
		# 0,2 Sekunden warten
		time.sleep(0.2)
