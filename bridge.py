# Projet Jardin Autonome STI2D
# Bridge.py - Convert Serial Requests to HTTP GET requests
# Made to work with Projet-Arduino

# Needs the pyserial and requests module
# The Arduino Board MUST be on /dev/ttyUSB0

import serial
import time
import socket
import requests

print("Initializing...")
ser = serial.Serial("COM4")

# Attend 10 secondes
time.sleep(10)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 1))  # connect() for UDP doesn't send packets
local_ip_address = "I"
local_ip_address += s.getsockname()[0]
local_ip_address += "P"

# On envoie notre adresse IP locale
ser.write(local_ip_address.encode("utf-8"))

# Add empty param at the end of the URL
inject_url = "http://localhost/Jardin-Autonome-git/inject.php?"
print("Reached Master While loop.")
while True:

    data = ""

    while ser.in_waiting > 0:
        # Tant qu'on a des données dans le buffer...
        data += ser.read().decode()

        # Attendre un peu le temps que le buffer soit OK.
        time.sleep(0.1)

    if data != "":
        print("DATA RECEIVED")
        print("\t" + data)
        # On fait la requête à la page inject.php
        url = inject_url + data
        print(requests.get(url))
        print("------------------")

    time.sleep(0.5)
