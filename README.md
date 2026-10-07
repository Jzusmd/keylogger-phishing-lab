<!-- BANNER DE ADVERTENCIA -->
<div align="center">

# 🔐 Laboratorio de Keylogger + Phishing + Bypass de Antivirus

### Proyecto de Ciberseguridad Ofensiva — Entorno Controlado

[![Purpose](https://img.shields.io/badge/Purpose-Educational-blue?style=for-the-badge)](./DISCLAIMER.md)
[![Platform](https://img.shields.io/badge/Platform-Windows%2011%20x64-lightgrey?style=for-the-badge)]()
[![Hypervisor](https://img.shields.io/badge/Hypervisor-VMware-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python%203.12-yellow?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT--Educational-green?style=for-the-badge)](./LICENSE)

---

> ⚠️ **ADVERTENCIA** ⚠️
>
> Este repositorio contiene código con **fines exclusivamente educativos**.
> Todo el laboratorio se ejecuta dentro de una **máquina virtual aislada**,
> **sin acceso a internet** y con **datos ficticios**.
>
> **NO usar contra sistemas sin autorización expresa por escrito.**
>
> Ver [`DISCLAIMER.md`](./DISCLAIMER.md) antes de continuar.

---

</div>

## 📖 Tabla de contenidos

- [Descripción](#-descripción)
- [Objetivos de aprendizaje](#-objetivos-de-aprendizaje)
- [Arquitectura del laboratorio](#-arquitectura-del-laboratorio)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Entorno de laboratorio](#-entorno-de-laboratorio)
- [Instalación](#-instalación)
- [Ejecución de la demo](#-ejecución-de-la-demo)
- [Evidencia del experimento](#-evidencia-del-experimento)
- [Técnicas MITRE ATT&CK](#-técnicas-mitre-attck)
- [Cómo defenderse](#-cómo-defenderse)
- [Documentación adicional](#-documentación-adicional)
- [Advertencia legal](#-advertencia-legal)
- [Licencia](#-licencia)
- [Autores](#-autores)

---

## 📌 Descripción

Este repositorio documenta un **laboratorio práctico de ciberseguridad ofensiva**
que integra tres vectores de ataque clásicos sobre una **máquina virtual Windows 11 x64**:

| # | Vector | Tecnología | Estado |
|---|--------|-----------|--------|
| 1 | **Keylogger de sistema** | Python + pynput | ✅ Funcional |
| 2 | **Phishing web con exfiltración** | Flask + HTML/CSS/JS | ✅ Funcional |
| 3 | **Bypass de antivirus** | Ejecución vía intérprete firmado | ✅ Confirmado |

Todo el tráfico se mantiene en **`localhost`**, dentro de una VM aislada
gestionada con **VMware Workstation**. **No hay conexión con sistemas externos.**

El objetivo **no es atacar**, sino **comprender** cómo funcionan estas técnicas
para poder **diseñar mejores defensas**.

---

## 🎯 Objetivos de aprendizaje

Al completar este laboratorio, el estudiante es capaz de:

- ✅ Entender el funcionamiento técnico de un **keylogger** en Python.
- ✅ Comprender el **ciclo de vida de un ataque de phishing** (cebo → captura → exfiltración).
- ✅ Analizar las **limitaciones de los antivirus basados en firma**.
- ✅ Identificar **técnicas de evasión** basadas en binarios firmados.
- ✅ Documentar hallazgos usando el **framework MITRE ATT&CK**.
- ✅ Proponer **controles de mitigación** realistas.

---

## 🏗️ Arquitectura del laboratorio

```
┌─────────────────────────────────────────────────────────────┐
│                    VM Windows 11 x64 (VMware)               │
│                                                             │
│  ┌──────────────┐         ┌────────────────────────────┐    │
│  │   Edge       │────────▶│  Flask :8080               │    │
│  │  (víctima)   │         │  Banco falso (phishing)    │    │
│  └──────────────┘         └──────────────┬─────────────┘    │
│                                          │                  │
│                                          ▼                  │
│  ┌──────────────┐         ┌────────────────────────────┐    │
│  │  Keylogger   │────────▶│  Flask :5000               │    │
│  │   Python     │         │  Panel del atacante        │    │
│  └──────────────┘         └──────────────┬─────────────┘    │
│                                          │                  │
│                                          ▼                  │
│                           ┌────────────────────────────┐    │
│                           │  Chrome (atacante)         │    │
│                           │  Visualización en vivo     │    │
│                           └────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Flujo del ataque

1. **La víctima** abre `http://localhost:8080` en Edge.
2. **El keylogger** captura cada tecla presionada y la envía al panel.
3. Al pulsar **"Ingresar"**, el navegador envía las credenciales al servidor Flask.
4. **Flask** reenvía las credenciales al panel del atacante (`:5000`).
5. **El atacante** ve todo en tiempo real en `http://localhost:5000`.
6. **Cada 10 segundos**, el keylogger toma una captura de pantalla.

---

## 📂 Estructura del repositorio

```
keylogger-phishing-lab/
│
├── README.md                      ← Este archivo
├── DISCLAIMER.md                  ← Advertencia legal y ética
├── LICENSE                        ← Licencia MIT con cláusula educativa
├── .gitignore                     ← Exclusiones para Git
│
├── docs/
│   ├── ARQUITECTURA.md            ← Detalles técnicos
│   ├── INSTALACION.md             ← Guía de instalación paso a paso
│   └── MITIGACION.md              ← Controles defensivos
│
├── capturas/                      ← Evidencia visual (opcional)
│   ├── 01-login-falso.png
│   ├── 02-panel-atacante.png
│   ├── 03-bitdefender-bloqueo.png
│   └── 04-bypass-exitoso.png
│
├── 01-keylogger/
│   ├── keylogger.py               ← Keylogger básico
│   ├── keylogger_exfiltra.py      ← Keylogger con exfiltración
│   └── requirements.txt
│
├── 02-phishing/
│   ├── servidor.py                ← Servidor Flask del banco falso
│   ├── templates/
│   │   └── bcp_falso.html         ← Página falsa (con banner DEMO)
│   └── requirements.txt
│
├── 03-panel-atacante/
│   ├── panel.py                   ← Servidor Flask del panel
│   ├── templates/
│   │   └── panel.html             ← Panel visual de recepción
│   └── requirements.txt
│
└── 04-bypass/
    ├── keylogger_defender.py      ← Intento de evasión (bloqueado por AV)
    └── README.md                  ← Explicación del bypass
```

---

## 💻 Entorno de laboratorio

| Componente | Versión / Detalle |
|---|---|
| **Hipervisor** | VMware Workstation Pro / Player |
| **Sistema operativo** | Windows 11 x64 |
| **Arquitectura** | x64 (Intel / AMD) |
| **Python** | 3.11 o 3.12 (64-bit) |
| **Antivirus** | Bitdefender Antivirus Free |
| **Red** | NAT o Host-Only (sin acceso externo) |
| **RAM asignada** | 4 GB mínimo / 8 GB recomendado |
| **CPU** | 2 cores mínimo / 4 cores recomendado |
| **Disco** | 60 GB (single file) |

> ⚠️ **El laboratorio también fue probado exitosamente en macOS con UTM
> (Apple Silicon, ARM64)**, obteniendo los mismos resultados en cuanto a
> detección por parte del antivirus.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/keylogger-phishing-lab.git
cd keylogger-phishing-lab
```

### 2. Instalar Python 3.12 (x64)

Descargar desde: https://www.python.org/downloads/

> ⚠️ Marcar **"Add python.exe to PATH"** durante la instalación.

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
python -m pip install flask requests pillow pynput pygetwindow
```

### 4. Verificar instalación

```bash
python -c "import flask, requests, PIL, pynput, pygetwindow; print('TODO OK')"
```

Si imprime **`TODO OK`**, estás listo. 🎯

> 📖 Para una guía detallada paso a paso, ver [`docs/INSTALACION.md`](./docs/INSTALACION.md).

---

## 🎬 Ejecución de la demo

Se necesitan **3 terminales** dentro de la VM:

### Terminal 1 — Servidor del banco falso

```bash
cd 02-phishing
python servidor.py
```

Salida esperada:
```
 * Running on http://127.0.0.1:8080
```

### Terminal 2 — Panel del atacante

```bash
cd 03-panel-atacante
python panel.py
```

Salida esperada:
```
 * Running on http://127.0.0.1:5000
```

### Terminal 3 — Keylogger con exfiltración

```bash
cd 01-keylogger
python keylogger_exfiltra.py
```

Salida esperada:
```
Keylogger activo con exfiltración y screenshots. Ctrl+C para detener.
```

### En los navegadores

| Navegador | URL | Rol |
|---|---|---|
| **Microsoft Edge** | `http://localhost:8080` | Víctima (ve el banco falso) |
| **Google Chrome** | `http://localhost:5000` | Atacante (ve el panel) |

### Simulación del ataque

1. En **Edge**, escribe usuario `walker` y contraseña `qwerty`.
2. Pulsa **Ingresar** → verás "Verificando seguridad...".
3. En **Chrome**, aparecerán las credenciales **en tiempo real**.
4. En la pantalla de tarjeta, ingresa datos ficticios.
5. Pulsa **Verificar** → verás los datos capturados.
6. Espera ~10 segundos → verás la **captura de pantalla** actualizarse.

### Detener el laboratorio

En cada terminal:

```
Ctrl + C
```

O matar todos los procesos Python de golpe:

```powershell
taskkill /IM python.exe /F
```

---

## 🔬 Evidencia del experimento

### Experimento del bypass de antivirus

**Hipótesis:** Bitdefender bloqueará el keylogger compilado, pero no el
script ejecutado directamente por `python.exe`.

#### ❌ Antes — Compilación con PyInstaller

```powershell
cd 04-bypass
pyinstaller --onefile --noconsole --name malware_demo keylogger_defender.py
```

**Resultado:** Bitdefender detecta y pone en cuarentena el `.exe` generado.

```
⚠️ Amenaza bloqueada: Gen:Variant.Malware.Keylogger
Estado: Desinfección en curso
```

#### ✅ Después — Ejecución vía intérprete firmado

```powershell
cd 01-keylogger
python keylogger_exfiltra.py
```

**Resultado:** ✅ **El keylogger se ejecuta sin ser bloqueado.**

#### 📌 Conclusión técnica

El binario `python.exe` está **firmado digitalmente** por la Python Software
Foundation. Bitdefender confía en él y **no analiza en profundidad el script
que ejecuta**, permitiendo la evasión.

**Técnica MITRE:** [`T1218 — System Binary Proxy Execution`](https://attack.mitre.org/techniques/T1218/).

---

## 🛡️ Técnicas MITRE ATT&CK documentadas

| ID | Técnica | Aplicación en el laboratorio |
|---|---|---|
| [T1566.002](https://attack.mitre.org/techniques/T1566/002/) | Spearphishing Link | Página falsa del banco |
| [T1056.001](https://attack.mitre.org/techniques/T1056/001/) | Keylogging | Captura de teclas con pynput |
| [T1113](https://attack.mitre.org/techniques/T1113/) | Screen Capture | Screenshots cada 10 segundos |
| [T1041](https://attack.mitre.org/techniques/T1041/) | Exfiltration Over C2 Channel | HTTP a `localhost:5000` |
| [T1218](https://attack.mitre.org/techniques/T1218/) | System Binary Proxy Execution | Bypass vía `python.exe` |

---

## 🛡️ Cómo defenderse

| Amenaza | Mitigación |
|---|---|
| **Keylogger** | EDR con heurística, 2FA con hardware, teclados virtuales |
| **Phishing** | Filtros DNS, gestores de contraseñas, educación del usuario |
| **Bypass de AV** | WDAC / AppLocker, restricción de intérpretes, ASR en Defender |
| **Exfiltración HTTP** | DLP, proxies con inspección TLS, segmentación de red |

Ver [`docs/MITIGACION.md`](./docs/MITIGACION.md) para detalles.

---

## 📚 Documentación adicional

| Documento | Contenido |
|---|---|
| [`docs/ARQUITECTURA.md`](./docs/ARQUITECTURA.md) | Diagramas y flujo técnico detallado |
| [`docs/INSTALACION.md`](./docs/INSTALACION.md) | Guía paso a paso de instalación |
| [`docs/MITIGACION.md`](./docs/MITIGACION.md) | Controles defensivos recomendados |
| [`04-bypass/README.md`](./04-bypass/README.md) | Explicación técnica del bypass |

---

## ⚖️ Advertencia legal

> **El uso de estas técnicas contra sistemas sin autorización expresa por
> escrito constituye un DELITO INFORMÁTICO** en la mayoría de jurisdicciones.
>
> En Perú, la **Ley N.º 30096 — Ley de Delitos Informáticos** tipifica como
> delito el acceso no autorizado a sistemas.
>
> Legislaciones similares existen en todo el mundo: **CFAA** (EE. UU.),
> **Computer Misuse Act** (Reino Unido), **Convenio de Budapest**, etc.
>
> Este repositorio se publica **exclusivamente con fines educativos y de
> investigación**. Los autores **no se hacen responsables** del uso indebido
> del material aquí expuesto.

Ver [`DISCLAIMER.md`](./DISCLAIMER.md) para más detalles.

---

## 📜 Licencia

Distribuido bajo **MIT License con cláusula educativa**.

Ver [`LICENSE`](./LICENSE) para el texto completo.

---

## 👥 Autores

| Nombre | Rol | Contacto |
|---|---|---|
| **[William Miranda]** | Desarrollo y documentación | [wilu.miranda.25@gmail.com] |
| **[William Miranda]** | Análisis de evasión | — |
| **[Walker Chavez]** | Documentación MITRE | — |

**Curso:** [Hacking Ético]
**Institución:** [Universidad Privada de Ciencias Aplicadas]
**Año:** 2026

---

## 🙏 Agradecimientos

- **Python Software Foundation** por Python.
- **Pallets Projects** por Flask.
- **Moses Palmér** por `pynput`.
- **MITRE Corporation** por el framework ATT&CK.
- **Bitdefender** por la versión Free utilizada en las pruebas.

---

<div align="center">

### ⭐ Si este laboratorio te resultó útil, dale una estrella ⭐

**Hecho con fines educativos — Úsalo con responsabilidad.**

</div>
