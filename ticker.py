# wenn der Taster auf Pin betaetigt wird, 
# dann wird die Variable "Counter" um 1 erhoet
# und es wird der Text: Counter + (die aktuelle Zahl)
# ausgegeben
import RPi.GPIO as GPIO
import time

# Variable Counter definieren
Counter = 0

# Pin-Nummer wie auf dem Raspberry verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 18 als Input deklarieren und Pull-Down Widerstand aktivieren
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# ISR
def Interrupt(channel):
        # Zugriff auf globale Variablen
       global Counter

        # Counter um eins erhoehen und ausgeben
       Counter = Counter + 1
       print "Counter " + str(Counter)

# Interrupt Event hinzufuegen. Pin 18, auf steigende Flanke reagieren und ISR "Interrupt" deklarieren
GPIO.add_event_detect(18, GPIO.RISING, callback = Interrupt, bouncetime = 200)

# Endlosschleife
while True:
        time.sleep(1)
