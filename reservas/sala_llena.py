def seleccionar_asiento(self):
    if not any(self.SeatsAvailable.values()):
        print("\nLo sentimos. La sala esta llena. No hay asientos disponibles.")
        input("\nPresione Enter para volver al menu...")
        return

    while True:
        pass