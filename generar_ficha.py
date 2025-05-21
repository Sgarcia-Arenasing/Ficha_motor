from PIL import Image, ImageDraw, ImageFont

PLANTILLA_PATH = "plantilla_base.png"

def agregar_datos(draw, font, datos, x, y_inicial, espaciado):
    for clave, valor in datos.items():
        draw.text((x+50, y_inicial), f"{clave}", font=font, fill=(208, 205, 183))
        draw.text((x + 350, y_inicial), f"{valor}", font=font, fill=(208, 205, 183))
        y_inicial += espaciado

def generar_ficha_con_datos(datos, imagen_path):
    base = Image.open(PLANTILLA_PATH).convert("RGBA")
    ancho, alto = base.size

    coche = Image.open(imagen_path).convert("RGBA")
    coche = coche.resize((int(ancho * 0.9), int(alto * 0.35)))
    base.paste(coche, (int(ancho * 0.05), int(alto * 0.2)))

    draw = ImageDraw.Draw(base)
    fuente = ImageFont.truetype("DejaVuSans-Bold.ttf", 25)

    agregar_datos(draw, fuente, datos, x=80, y_inicial=int(alto * 0.67), espaciado=60)

    output_path = f"fichas/{datos['Modelo'].replace(' ', '_')}_{datos['Matriculación']}.png"
    base.save(output_path)
    print(f"Ficha generada: {output_path}")
