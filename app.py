from flask import Flask, request, jsonify
from generar_ficha import generar_ficha_con_datos
import requests

app = Flask(__name__)

@app.route('/api/generar-ficha', methods=['POST'])
def generar_ficha():
    data = request.get_json()
    imagen_url = data.pop('imagen_url')
    
    # Descarga imagen del coche
    imagen_path = 'imagen_coche.jpg'
    with open(imagen_path, 'wb') as f:
        f.write(requests.get(imagen_url).content)

    generar_ficha_con_datos(data, imagen_path)

    return jsonify({"status": "ok", "mensaje": "Ficha generada con éxito"})

if __name__ == '__main__':
    app.run()
