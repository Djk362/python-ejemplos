class Restaurante:
    """Un modelo sencillo para representar un restaurante."""
    def __init__(self, nombre_restaurante, tipo_cocina):
        """atributos del restaurante"""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
    def describir_restaurante(self):
        print(f"\nEl restaurante '{self.nombre_restaurante}' ofrece comida de tipo '{self.tipo_cocina}'.")
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ya esta abierto al publico")
    def establecer_numero_servido(self, clientes):
        if clientes >= self.numero_servido:
            self.numero_servido = clientes
        else:
            print("No uedes reducir la cantidad de clientes atendidos.")
    def incrementar_numero_servido(self, nuevos_clientes):
        if nuevos_clientes > 0:
            self.numero_servido += nuevos_clientes
            
mi_restaurante = Restaurante('El Fogon paisa', 'Tipica Colombiana')
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()
print(f"Clientes atendidos al iniciar el dia {mi_restaurante.numero_servido}")
mi_restaurante.establecer_numero_servido(25)
print(f"Clientes atendidos por la tarde: {mi_restaurante.numero_servido}")
mi_restaurante.incrementar_numero_servido(10)
print(f"Total de clientes atendidos hoy al cierre: {mi_restaurante.numero_servido}")
