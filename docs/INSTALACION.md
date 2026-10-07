# 🚀 Guía de instalación

## Requisitos

- Windows 11 x64 (o Windows 10 x64)
- Python 3.11 o 3.12 (64-bit)
- Conexión a internet (solo para instalar dependencias)

## Paso 1 — Instalar Python

1. Descargar de https://www.python.org/downloads/
2. Marcar ✅ **Add python.exe to PATH**
3. Install Now

Verificar:

```bash
python --versión

Paso 2:

git clone https://github.com/Jzusmd/keylogger-phishing-lab.git
cd keylogger-phishing-lab

Paso 3:

python -m pip install --upgrade pip
python -m pip install flask requests pillow pynput pygetwindow

Paso 4:

python -c "import flask, requests, PIL, pynput, pygetwindow; print('TODO OK')"

Paso 5:

terminal 1:

cd 02-phishing
python servidor.py

terminal 2:

cd 03-panel-atacante
python panel.py

terminal 3:

cd 01-keylogger
python keylogger_exfiltra.py

Paso 6:

taskkill /IM python.exe /F




---

## 📄 `docs/MITIGACION.md`

```markdown
# 🛡️ Cómo defenderse de estos ataques

## Contra keyloggers

- **Antivirus con heurística** (no solo firma).
- **EDR** (Endpoint Detection and Response).
- **Teclados virtuales** en sitios sensibles.
- **2FA** con app autenticadora o hardware.
- **Monitoreo de procesos** que acceden al teclado.

## Contra phishing

- **Verificar siempre la URL** antes de ingresar datos.
- **HTTPS no garantiza legitimidad** (cualquiera puede tenerlo hoy).
- **Gestores de contraseñas** con autocompletado (detectan dominios falsos).
- **Educación del usuario** — simulacros de phishing.
- **Filtros antiphishing** en correo y DNS.

## Contra bypass de AV

- **No confiar solo en AV basado en firma.**
- **Aplicar listas blancas de ejecutables** (AppLocker, WDAC).
- **Restringir intérpretes** (Python, PowerShell) en entornos corporativos.
- **Registrar ejecución de procesos** (Sysmon, Event ID 4688).
- **Habilitar ASR** (Attack Surface Reduction) en Defender.

## Técnicas MITRE cubiertas por estas mitigaciones

| Mitigación | Técnica mitigada |
|---|---|
| WDAC / AppLocker | T1218 |
| MFA hardware | T1056.001 |
| Filtro DNS | T1566.002 |
| EDR | Todas las anteriores |