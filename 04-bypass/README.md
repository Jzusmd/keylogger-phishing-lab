# 🔬 Prueba de bypass de antivirus

## Objetivo

Demostrar que el keylogger compilado con PyInstaller es bloqueado por
Bitdefender, mientras que el mismo código ejecutado vía `python.exe`
**NO es bloqueado**.

## Hipótesis

El binario `python.exe` está firmado digitalmente por la Python Software
Foundation. Bitdefender confía en él y no analiza el script que ejecuta.

## Procedimiento

### 1. Compilar con PyInstaller

```bash
pyinstaller --onefile --noconsole --name malware_demo keylogger_defender.py