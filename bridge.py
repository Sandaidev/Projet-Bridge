# Projet Jardin Autonome STI2D
# Bridge.py - Convert Serial Requests to HTTP GET requests
# Made to work with Projet-Arduino

# Needs the pyserial and requests module
# The Arduino Board MUST be on /dev/ttyUSB0

import time
import socket
import requests

from pyfirmata import Arduino, util, STRING_DATA

JA_VERSION = "1.03"
board = Arduino("/dev/ACM0")
acquisition = util.Iterator(board)
acquisition.start()

INJECT_URL = "http://localhost/Jardin-Autonome-git/inject.php"


def msg(text):
    """
    Sends a message to the LCD screen
    """

    if text:
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))


# Définition des capteurs
capteur_cuve_1 = board.get_pin("d:2:i")  # Digital:pin-2:Input
capteur_cuve_2 = board.get_pin("d:3:i")
capteur_cuve_3 = board.get_pin("d:4:i")
capteur_cuve_4 = board.get_pin("d:5:i")
capteur_humidite = board.get_pin("a:0:i")  # Analog:pin-0:Input

msg("  Connexion OK  ")
msg(" ")
time.sleep(2)
msg("  JA - Arduino  ")
msg("  version " + JA_VERSION)
time.sleep(5)

print("Analog : " + str(capteur_humidite.read()))


while True:
    # Toutes les 15 minutes, on envoie les données des capteurs à la BDD

    for minutes_left in range(15):
        msg("Envoi des donnes")
        msg("dans " + str(15 - minutes_left) + " minutes")
        time.sleep(60)

    msg("    Envoi en    ")
    msg("    cours...    ")

    capteur_data = {
        "cuve1": capteur_cuve_1.read(),
        "cuve2": capteur_cuve_2.read(),
        "cuve3": capteur_cuve_3.read(),
        "cuve4": capteur_cuve_4.read(),
        "humidite": capteur_humidite.read(),
    }

    requests.get(INJECT_URL, params=capteur_data)

    msg("   Donnees OK   ")
    msg(" ")
    time.sleep(10)
