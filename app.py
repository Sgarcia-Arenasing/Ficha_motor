from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/generar-ficha', methods=['POST'])
def generar_ficha():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    imagen_url = data.get("imagen_url")
    modelo = data.get("modelo")
    matriculacion = data.get("matriculacion")
    motor = data.get("motor")
    traccion = data.get("traccion")
    potencia = data.get("potencia")
    procedencia = data.get("procedencia")

    if not imagen_url:
        return jsonify({"error": "Falta imagen_url"}), 400

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
