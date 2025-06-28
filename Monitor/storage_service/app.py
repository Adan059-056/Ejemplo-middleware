from flask import Flask, request, jsonify

app = Flask(__name__)
datosColonia = {}

@app.route('/guardar', methods=['POST'])
def guardar():
    data = request.get_json()
    colonia = data['colonia']

    if colonia not in datosColonia:
        datosColonia[colonia] = []
    datosColonia[colonia].append(data)

    print(f"Guardado en {colonia}: {data}")
    return jsonify({"status": "guardado"})

@app.route('/colonia/<colonia>', methods=['GET'])
def obtener_datos(colonia):
    return jsonify(datosColonia.get(colonia, []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)