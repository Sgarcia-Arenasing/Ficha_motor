from PIL import Image, ImageDraw, ImageFont
import os

# === CONFIGURACIÓN ===
PLANTILLA_PATH = "plantilla_base.png"   # Reemplaza con tu ruta a la plantilla generada
IMAGEN_COCHE_PATH = "imagen_coche.jpg"  # Ruta a la imagen del usuario
OUTPUT_PATH = "ficha_final.png"         # Resultado generado

# Datos del formulario (simulados aquí)
datos = {
    "Modelo": "Wolkswagen Escarabajo",
    "Matriculación": "1968",
    "Motor": "1.6 TwinCam",
    "Tracción": "Trasera",
    "Potencia": "115 CV",
    "Procedencia": "Italia"
}

# === FUNCIONES ===

def agregar_datos(draw, font, datos, x, y_inicial, espaciado):
    for clave, valor in datos.items():
        draw.text((x+50, y_inicial), f"{clave}", font=font, fill=(208, 205, 183))
        draw.text((x + 350, y_inicial), f"{valor}", font=font, fill=(208, 205, 183))
        y_inicial += espaciado

def ajustar_fuente(draw, texto, fuente_base, max_ancho):
    fuente = fuente_base
    while draw.textlength(texto, font=fuente) > max_ancho and fuente.size > 10:
        fuente = ImageFont.truetype(fuente.path, fuente.size - 1)
    return fuente

def generar_ficha():
    # Abrir plantilla
    base = Image.open(PLANTILLA_PATH).convert("RGBA")
    ancho, alto = base.size

    # Cargar imagen del coche
    coche = Image.open(IMAGEN_COCHE_PATH).convert("RGBA")
    coche = coche.resize((int(ancho * 0.9), int(alto * 0.35)))  # Ajustamos a tamaño plantilla
    base.paste(coche, (int(ancho * 0.05), int(alto*0.2 )))  # Pegar imagen coche

    # Dibujar texto
    draw = ImageDraw.Draw(base)
    fuente = ImageFont.truetype("DejaVuSans-Bold.ttf", 25)

    agregar_datos(draw, fuente, datos, x=80, y_inicial=int(alto * 0.67), espaciado=60)

    # Guardar resultado
    base.save(OUTPUT_PATH)
    print(f"Ficha guardada en: {OUTPUT_PATH}")

# === EJECUCIÓN ===
if __name__ == "__main__":
    generar_ficha()
