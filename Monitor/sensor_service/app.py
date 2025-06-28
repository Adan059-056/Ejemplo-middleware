from flask import Flask
import requests, time, random

app = Flask(__name__)

def enviar_datos():
    while True:
        data = {
            "colonia": "cuajimalpa",
            "temperatura": round(random.uniform(20, 40), 2),
            "humedad": round(random.uniform(30, 80), 2),
            "calidad_aire": round(random.uniform(10, 100), 2)
        }
        try:
            response = requests.post("http://collector_service:5010/datos", json=data)
            print("Datos enviados:", data)
        except Exception as e:
            print("Error enviando datos:", e)
        time.sleep(5)

if __name__ == "__main__":
    enviar_datos()