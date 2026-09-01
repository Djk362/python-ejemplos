invitados = ["Alice", "Bob", "Charlie", "David"]
cancelado = "Charlie"
invitados.remove(cancelado) #elimino a un invitado
invitados.append("Eve") #agregar un nuevo invitado al  final de lista
invitados.insert(1, "Frank") #agregar un invitado en una posición específica
eliminado = invitados.pop() #eliminar el último invitado
print(f"lo sentimos papu {eliminado} no hay espacio, debiste llegar mas temprano")
print(invitados)