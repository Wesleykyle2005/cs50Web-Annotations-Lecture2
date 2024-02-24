
class Flight():
    # crear un nuevo vuelo y especificar la capacidad
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Añadir pasajeros
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Asientos disponibles
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

# Añadir una lista de personas al vuelo
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"{person} ha sido añadida al vuelo ")
    else:
        print(f"No hay sillas para {person}")