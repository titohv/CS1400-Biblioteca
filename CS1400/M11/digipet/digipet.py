"""
Proyecto: Simulacion de DigiPet
Estudiante: Tito Huerta
Proposito: Cuidar una mascota virtual y mantener sus niveles de felicidad, comida y salud por encima de cero
"""


class DigiPet:
    """Representa una mascota con estado y acciones propias."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.hambre = 100  # Reserva de comida: 100 = lleno; 0 = sin comida
        self.salud = 100
        self.edad = 0

    def alimentar(self):
        self.hambre = min(100, self.hambre + 30)
        print(f"{self.nombre} ha comido. ¡Qué rico!")

    def jugar(self):
        self.felicidad = min(100, self.felicidad + 25)
        self.hambre -= 8
        print(f"{self.nombre} se divirtió jugando.")

    def pasear(self):
        self.felicidad = min(100, self.felicidad + 15)
        self.salud = min(100, self.salud + 10)
        self.hambre -= 12
        print(f"{self.nombre} disfrutó el paseo.")

    def acariciar(self):
        self.felicidad = min(100, self.felicidad + 15)
        print(f"{self.nombre} está feliz con tus caricias.")

    def pasar_tiempo(self):
        # Cada turno representa un día de la vida de la mascota.
        self.edad += 1
        self.felicidad -= 8
        self.hambre -= 10
        self.salud -= 5

    def esta_vivo(self):
        return self.felicidad > 0 and self.hambre > 0 and self.salud > 0

    def mostrar_estado(self):
        print(f"\n--- Estado de {self.nombre} | Día {self.edad} ---")
        print(f"Felicidad: {max(0, self.felicidad)} | "
              f"Comida: {max(0, self.hambre)} | "
              f"Salud: {max(0, self.salud)}")

    def causa_muerte(self):
        if self.hambre <= 0:
            return "hambre"
        if self.salud <= 0:
            return "enfermedad"
        return "soledad"


def main():
    print("=== DIGIPET: MI MASCOTA VIRTUAL ===")
    nombre = input("¿Cómo se llama tu mascota? ").strip()
    if not nombre:
        nombre = "Luna"

    mascota = DigiPet(nombre)
    print(f"¡Bienvenido! Ahora debes cuidar a {mascota.nombre}.")

    while mascota.esta_vivo():
        mascota.mostrar_estado()
        print("\n1. Jugar")
        print("2. Alimentar")
        print("3. Pasear")
        print("4. Acariciar")
        print("5. Salir")
        opcion = input("¿Qué deseas hacer? ").strip()

        if opcion == "5":
            print(f"¡Hasta pronto! {mascota.nombre} te espera.")
            return
        elif opcion == "1":
            mascota.jugar()
        elif opcion == "2":
            mascota.alimentar()
        elif opcion == "3":
            mascota.pasear()
        elif opcion == "4":
            mascota.acariciar()
        else:
            print("Opción inválida. Elige un número del 1 al 5.")
            continue

        # Solo una acción válida hace avanzar un día.
        mascota.pasar_tiempo()

    mascota.mostrar_estado()
    print(f"\n{mascota.nombre} murió por {mascota.causa_muerte()}.")
    print("Fin del juego.")


if __name__ == "__main__":
    main()
