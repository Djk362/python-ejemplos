"""Hay varias formas para describir una mascota"""
def describir_mascota(tipo, nombre):
    print(f"Tengo un {tipo} llamando {nombre.title()}")
describir_mascota('toby', 'perro')
#Aqui por ejemplo depende del orden, nos dira el perro se llama toby o el toby se llama perro.
describir_mascota(nombre='toby', tipo='perro')
#si usamos este, podemos pasar el argumento directamente con el nombre
