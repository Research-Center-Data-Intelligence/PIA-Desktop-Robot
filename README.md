# README P.I.A.

Let op:
De kleuren van kabels binnen het ontwerprapport komen niet meer overeen met de werkelijke verbindingen binnen de P.I.A na assemblage.

## Om de P.I.A aan de praat te krijgen.
Binnen het project is gebruikt gemaakt van Remote vs. code + Python en met behulp van een mobiele hotspot een SSH verbinding gemaakt met de P.I.A voor remote aansturing
1.  Verbinding
- Sluit Externe 5V kabel aan op je PC (Voor stroom) 	
- Zet de Mobiele hotspot van het verbonden apparaat aan zodat de RPI een remote SSH verbinding kan maken met je PC met behulp van remote VS. 
- Verbind remote toetsenbord + Muis + Beeldscherm en verbind tot je eigen Hotspot
- Configureer de RPI tot je eigen hotspot


2. Alternatief voor huidige configuratie
- Hotspotnaam: BorkLaptop
- Wachtwoord: 84a}N737
  
3. Indien geen connectie micro sd kaart herconfigureren (Zoek bestaande documenten van RPI)

4. Verbind met de RPI via remote VS 

5. Start main.py

## Gebruikte Libraries binnen Python virtual Environment.
Voor de Raspberry Pi:
•	sudo apt install -y python3-full git python3-pip python3-pil
•	pip3 install --upgrade pip setuptools
•	sudo apt update
•	sudo apt upgrade
Voor het aansturen van de sensoren binnen de Python Virtual Environment:
•	pip install adafruit-blinka (voor de servomotors)
•	pip install libcamera (voor de camera)
•	pip install RPicam-apps (voor de camera)
•	pip install RPi.GPIO
Voor verdere informatie is binnen het Ontwerprapport van het portfolio meer te vinden.
