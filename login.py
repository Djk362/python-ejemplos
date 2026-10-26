class Usuario:
    def __init__(self, nombre, apellido, correo):
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
    self.intentos_inicio = 0 #valor por defecto
    
def describir_usuario(self):
    print(f"\n--- Perfil del Usuario ---")
    print(f"Nombre completo: {self.nombre.title()} {self.apellido.title()}")
    print(f"Correo: {self.correo}")
def saludar_usuario(self):
    print(f"Hola de nuevo, {self.nombre.title()}")
def incrementar_intentos(self):
    self.intentos_inicio += 1
def restablecer_intentos_inicio(self):
    self.intentos_inicio = 0

nuevo_usuario = usuario('Andres', 'gomez', 'andres@correo.com')
print("simulando ingresos fallidos...")
nuevo_usuario.incrementar_intentos_inicio()
nuevo_usuario.incrementar_intentos_inicio()
nuevo_usuario.incrementar_intentos_inicio()
print(f"Intentos de inicio registrados: {nuevo_usuario.intentos_inicio}")
print("\nInicio de secion exitoso, reestableciendo contador...")
nuevo_usuario.restablecer_intentos_inicio()
print(f"Intentos  de inicio tras el  exito: {nuevo_usuario.intentos_inicio}")


"""Un modelo para representar el perfil del usuario."""
