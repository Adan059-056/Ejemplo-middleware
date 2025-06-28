from flask import Flask, request, jsonify

app = Flask(__name__)
alertas = []

@app.route('/evaluar', methods=['POST'])
def evaluar():
    data = request.get_json()
    colonia = data['colonia']
    temp = data['temperatura']
    calidad = data['calidad_aire']

    if temp > 35 or calidad > 60:
        alerta = f"ALERTA en {colonia}: Temp={temp} °C, Calidad aire={calidad}"
        alertas.append(alerta)
        print(alerta)

    return jsonify({"status": "evaluado"})

@app.route('/alertas', methods=['GET'])
def ver_alertas():
    return jsonify(alertas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012)