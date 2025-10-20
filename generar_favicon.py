from PIL import Image, ImageDraw, ImageFont
import math

def crear_favicon_matematico():
    """Crea un favicon personalizado con tema matemático"""
    
    # Tamaño estándar para favicon
    tamaño = (32, 32)
    
    # Crear imagen con fondo azul (color de confianza/matemáticas)
    img = Image.new('RGB', tamaño, color=(25, 118, 210))  # Azul material design
    draw = ImageDraw.Draw(img)
    
    # Dibujar símbolo matemático (π) en el centro
    try:
        # Intentar usar fuente del sistema
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        # Fuente por defecto si no hay arial
        font = ImageFont.load_default()
    
    # Dibujar el símbolo π (pi) o + si no se puede
    try:
        draw.text((8, 6), "π", fill=(255, 255, 255), font=font)
    except:
        draw.text((12, 8), "+", fill=(255, 255, 255), font=font)
    
    # Guardar como favicon
    img.save("static/favicon.ico", format="ICO", sizes=[(32, 32)])
    print("✅ Favicon creado: static/favicon.ico")

def crear_logo():
    """Crea un logo más grande para la documentación"""
    tamaño = (128, 128)
    img = Image.new('RGB', tamaño, color=(25, 118, 210))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 60)
        draw.text((32, 34), "π", fill=(255, 255, 255), font=font)
    except:
        font = ImageFont.load_default()
        draw.text((54, 54), "+", fill=(255, 255, 255), font=font)
    
    # Dibujar círculo alrededor
    draw.ellipse([10, 10, 118, 118], outline=(255, 255, 255), width=3)
    
    img.save("static/logo.png", format="PNG")
    print("✅ Logo creado: static/logo.png")

if __name__ == "__main__":
    crear_favicon_matematico()
    crear_logo()
    print("🎨 Assets gráficos creados exitosamente!")