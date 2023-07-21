#Ejercicio 5:
#Desarrollo de un juego de rol (RPG):
#Crea un juego de rol utilizando programación orientada a objetos. 
#Diseña clases como "Personaje", "Enemigo" y "Arma", e implementa métodos
#para que los personajes puedan atacar, defenderse, adquirir experiencia y subir de nivel.

class Arma:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def __str__(self):
        return f"{self.nombre} - Poder: {self.poder}"


class Personaje:
    def __init__(self, nombre, salud, ataque, defensa, nivel=1, experiencia=0):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.experiencia = experiencia

    def atacar(self, enemigo):
        enemigo.recibir_ataque(self.ataque)

    def recibir_ataque(self, poder_ataque):
        dano_recibido = max(poder_ataque - self.defensa, 0)
        self.salud -= dano_recibido
        print(f"{self.nombre} recibió {dano_recibido} puntos de daño.")

    def subir_nivel(self):
        if self.experiencia >= self.nivel * 10:
            self.nivel += 1
            self.experiencia = 0
            self.ataque += 5
            self.defensa += 3
            print(f"{self.nombre} ha subido al nivel {self.nivel}.")

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia.")

    def __str__(self):
        return f"{self.nombre} - Nivel: {self.nivel}, Salud: {self.salud}, Ataque: {self.ataque}, Defensa: {self.defensa}, Experiencia: {self.experiencia}"


class Enemigo(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, nivel=1, experiencia=0):
        super().__init__(nombre, salud, ataque, defensa, nivel, experiencia)

    def atacar(self, personaje):
        poder_ataque = self.ataque * self.nivel
        personaje.recibir_ataque(poder_ataque)

#---IMPORTANTE----   Nuevo metodo fuera del enunciado
#le permite al monstruo evolucionar si el ataque no lo mata en un golpe.

    def recibir_ataque(self, poder_ataque):
        dano_recibido = max(poder_ataque - self.defensa, 0)
        self.salud -= dano_recibido
        print(f"{self.nombre} recibió {dano_recibido} puntos de daño.")
        if self.salud <= 0:
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado.")
            return
        self.evolucionar()

    def evolucionar(self):
        if self.nivel < 3:  # Se define un límite para la evolución, en este caso nivel 3.
            self.nivel += 1
            self.ataque += 5
            self.defensa += 3
            print(f"{self.nombre} ha evolucionado al nivel {self.nivel}.\n")

    def __str__(self):
        return f"Enemigo {self.nombre} - Nivel: {self.nivel}, Salud: {self.salud}, Ataque: {self.ataque}, Defensa: {self.defensa}, Experiencia: {self.experiencia}"


# Crear personajes y enemigos
personajes_disponibles = [
    Personaje("Héroe", 100, 30, 15),
    Personaje("Guerrero", 120, 25, 20),
    Personaje("Mago", 80, 40, 10),
]

print("Personajes disponibles:")
for index, personaje in enumerate(personajes_disponibles):
    print(f"{index + 1}. {personaje.nombre}")

opcion_elegida = int(input("Elige tu personaje (ingresa el número correspondiente): "))
personaje_elegido = personajes_disponibles[opcion_elegida - 1]

print(f"Has elegido a {personaje_elegido.nombre} como tu personaje.\n")

# Crear un arma
espada = Arma("Espada Épica", 20)

# Crear enemigos
enemigo1 = Enemigo("Goblin", 80, 20, 10)
#....

# Simulador de combate
print("Has encontrado a un enemigo, no tienes otra opción más que luchar")
print(enemigo1,"\n")
personaje_elegido.atacar(enemigo1)
enemigo1.atacar(personaje_elegido)
print(personaje_elegido,"\n")

# Ganar experiencia y subir de nivel
personaje_elegido.ganar_experiencia(20)
personaje_elegido.subir_nivel()
print(personaje_elegido,"\n")
