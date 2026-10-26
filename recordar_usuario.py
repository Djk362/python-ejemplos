import json
from pathlib import Path

ruta = Path('usuario.json')
if ruta.exists():
    contenido = ruta.read_text()
    nombre = json.loads(contenido)
    print(f"Bienvenido de nuevo, {nombre.title()}")
    
else:
    nombre = input("Como te llamas?: ")
    contenido = json.dumps(nombre)
    ruta.write_text(contenido)
    print(f"Te recordaremos cuando vuelvas {nombre.title()}")
