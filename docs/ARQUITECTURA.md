# 🏗️ Arquitectura del laboratorio

## Diagrama de flujo

┌─────────────────┐ ┌──────────────────────┐
│ VM Windows 11 │ │ VM Windows 11 │
│ │ │ │
│ ┌───────────┐ │ │ ┌────────────────┐ │
│ │ Edge │──┼────────┼─▶│ Flask :8080 │ │
│ │ (víctima) │ │ │ │ phishing │ │
│ └───────────┘ │ │ └────────┬───────┘ │
│ │ │ │ │
│ ┌───────────┐ │ │ ▼ │
│ │ Keylogger │──┼────────┼─▶┌────────────────┐ │
│ │ Python │ │ │ │ Flask :5000 │ │
│ └───────────┘ │ │ │ panel atacante│ │
│ │ │ └────────────────┘ │
│ ┌───────────┐ │ │ │
│ │ Chrome │──┼────────┼─▶ Visualización │
│ │ (atacante)│ │ │ │
│ └───────────┘ │ │ │
└─────────────────┘ └──────────────────────┘


## Flujo del ataque

1. La víctima abre `http://localhost:8080` en Edge.
2. El keylogger (Python) captura cada tecla presionada.
3. Al pulsar "Ingresar", el navegador envía las credenciales al servidor Flask (`:8080`).
4. Flask reenvía las credenciales al panel del atacante (`:5000`).
5. El atacante ve todo en `http://localhost:5000` en tiempo real.

## Componentes

| Componente | Tecnología | Puerto | Función |
|---|---|---|---|
| Keylogger | Python + pynput | — | Captura teclas |
| Screenshots | Python + Pillow | — | Captura pantalla cada 10s |
| Servidor phishing | Flask | 8080 | Sirve página falsa |
| Panel atacante | Flask | 5000 | Recibe y muestra datos |