def generar_ficha_con_datos(datos, imagen_coche_path, output_path):
    base = Image.open(PLANTILLA_PATH).convert("RGBA")
    ancho, alto = base.size

    coche = Image.open(imagen_coche_path).convert("RGBA")
    coche = coche.resize((int(ancho * 0.9), int(alto * 0.35)))
    base.paste(coche, (int(ancho * 0.05), int(alto * 0.2)))

    draw = ImageDraw.Draw(base)
    fuente = ImageFont.truetype("DejaVuSans-Bold.ttf", 25)

    agregar_datos(draw, fuente, datos, x=80, y_inicial=int(alto * 0.67), espaciado=60)

    base.save(output_path)
