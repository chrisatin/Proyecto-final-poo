#Diseña un sistema de gestión de proyectos:
#Crear un sistema de gestión de proyectos que permita crear proyectos, asignar tareas a los miembros del equipo, 
#realizar seguimiento del progreso y generar informes. Utiliza clases como "Proyecto", "Tarea" y "Equipo" para modelar 
#el sistema y utiliza métodos para gestionar las operaciones. 
class Proyecto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas = []
        self.urgencia = "Normal"  # Urgencia por defecto: Normal

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas
#--IMPORTANTE---- Metodo añadido, define tipo de prioridad tiene el proyecto
    def definir_urgencia(self, urgencia):
        opciones_urgencia = ["Urgente", "Prioritario", "Normal"]
        if urgencia in opciones_urgencia:
            self.urgencia = urgencia
        else:
            print(f"Error: {urgencia} no es una opción válida para la urgencia.")

    def __str__(self):
        return f"Proyecto: {self.nombre}\nDescripción: {self.descripcion}\nUrgencia: {self.urgencia}"
    

class Tarea:
    def __init__(self, nombre, descripcion, responsable, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.descripcion = descripcion
        self.responsable = responsable
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "Pendiente"  # Estado inicial de la tarea

    def marcar_como_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nResponsable: {self.responsable}\nEstado: {self.estado}\nFecha de inicio: {self.fecha_inicio}\nFecha de fin: {self.fecha_fin}"

class Equipo:
    def __init__(self):
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def obtener_miembros(self):
        return self.miembros

# Prueba de ejecución 

# Creamos el equipo
equipo_proyecto = Equipo()
equipo_proyecto.agregar_miembro("Sebas")
equipo_proyecto.agregar_miembro("Mateo")
equipo_proyecto.agregar_miembro("Christian")

# Creamos un proyecto
proyecto1 = Proyecto("Desarrollo de Aplicación Web", "Proyecto para crear una aplicación web")
print(proyecto1)

# Creamos tareas y las asignamos al proyecto
tarea1 = Tarea("Diseño de interfaz", "Diseñar la interfaz de usuario", "Mateo", "2023-07-20", "2023-07-25")
tarea2 = Tarea("Implementación de funcionalidades", "Desarrollar las funcionalidades principales", "Sebas", "2023-07-26", "2023-08-05")

proyecto1.agregar_tarea(tarea1)
proyecto1.agregar_tarea(tarea2)

# Marcar tarea1 como completada
tarea1.marcar_como_completada()

# Obtener información del proyecto y sus tareas
print("\nInformación del Proyecto:")
print(proyecto1)

print("\nTareas del Proyecto:")
for tarea in proyecto1.obtener_tareas():
    print(tarea)

# Obtener información del equipo
print("\nMiembros del Equipo:")
for miembro in equipo_proyecto.obtener_miembros():
    print(miembro)
    
print("\n")
# Ejemplo de uso del método de urgencia:

proyecto2 = Proyecto("Actualización de Infraestructura de Red", "Mejora de la infraestructura de red de la empresa.")
print(proyecto2)

# Definir urgencia del proyecto como "Urgente"
proyecto2.definir_urgencia("Urgente")
print(proyecto2)
