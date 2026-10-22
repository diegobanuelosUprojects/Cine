def cancelar_reservacion_sin_sesion(cine):
    import os

    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 50)
    print("          CANCELAR RESERVACIÓN")
    print("=" * 50)

    reservas_activas = [
        asiento
        for asiento, reservado in cine.SeatsReserved.items()
        if reservado is True
    ]

    if not reservas_activas:
        print("No tienes reservaciones activas.")
        input("\nPresiona Enter para continuar...")
        return

    print("Tus reservaciones actuales:")
    print("-" * 50)

    for asiento in reservas_activas:
        tipo = cine.obtenerTipoAsiento(asiento)
        precio = cine.obtenerPrecioAsiento(asiento)
        print(f"Asiento: {asiento} | Tipo: {tipo} | Precio: ${precio:.2f}")

    print("-" * 50)
    print("Escribe 'salir' para regresar al menú.")

    asiento = input("\n¿Qué asiento deseas cancelar?: ").strip().upper()

    if asiento == "SALIR":
        return

    if asiento not in reservas_activas:
        print("\nEl asiento no está entre tus reservaciones activas.")
        input("\nPresiona Enter para continuar...")
        return

    cine.SeatsReserved[asiento] = False
    cine.SeatsAvailable[asiento] = True

    print(f"\nLa reservación del asiento {asiento} se canceló correctamente.")
    print(f"Nuevo total: ${cine.calcularTotalReservacion():.2f}")

    input("\nPresiona Enter para continuar...")
