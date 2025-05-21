from flask import Flask, request, jsonify, send_file
from generar_ficha import generar_ficha_con_datos
import requests

app = Flask(__name__)

@app.route('/api/generar-ficha', methods=['POST'])
def generar_ficha():
    try:
        payload = request.get_json()
        app.logger.info(f"Payload recibido: {payload!r}")          # <-- Añade este log
        imagen_url = payload.pop('imagen_url', None)
        app.logger.info(f"imagen_url: {imagen_url}")               # <-- Y este

        if not imagen_url:
            return jsonify({"status":"error","message":"No se recibió campo imagen_url"}), 400

        # Descarga de la imagen (aquí fallaba)
        coche_path = 'imagen_coche.jpg'
        resp = requests.get(imagen_url)
        resp.raise_for_status()                                   # <-- Para atrapar 4xx/5xx
        with open(coche_path, 'wb') as f:
            f.write(resp.content)

        # Genera la ficha  
        output_path = 'ficha_final.png'
        generar_ficha_con_datos(payload, coche_path, output_path)

        return send_file(output_path, mimetype='image/png')

    except requests.exceptions.RequestException as rex:
        app.logger.exception("Error al descargar la imagen")
        return jsonify({"status":"error","message":f"Error descargando imagen: {rex}"}), 400

    except Exception as e:
        app.logger.exception("Error al generar ficha")
        return jsonify({"status":"error","message":str(e)}), 500
