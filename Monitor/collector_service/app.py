from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/datos', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    print("Datos recibidos:", data)

    # Enviar a storage_service
    requests.post("http://storage_service:5011/guardar", json=data)

    # Enviar a alert_service
    requests.post("http://alert_services:5012/evaluar", json=data)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)