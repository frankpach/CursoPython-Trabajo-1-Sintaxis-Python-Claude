"""Calculadora de promedios escolares - Trabajo 1: Sintaxis Python."""


def ingresar_calificaciones():
    """Pide materias y calificaciones al usuario hasta que decida terminar.

    Devuelve dos listas paralelas: nombres de materias y sus calificaciones.
    """
    materias = []
    calificaciones = []

    while True:
        nombre = input("Ingresa el nombre de la materia: ").strip()
        while nombre == "":
            nombre = input("El nombre no puede estar vacío. Ingresa el nombre de la materia: ").strip()

        while True:
            entrada = input(f"Ingresa la calificación de {nombre} (0-10): ").strip()
            try:
                nota = float(entrada)
            except ValueError:
                print("Debes ingresar un número válido.")
                continue

            if nota < 0 or nota > 10:
                print("La calificación debe estar entre 0 y 10.")
                continue

            break

        materias.append(nombre)
        calificaciones.append(nota)

        while True:
            continuar = input("¿Deseas ingresar otra materia? (s/n): ").strip().lower()
            if continuar in ("s", "si", "sí"):
                break
            elif continuar in ("n", "no"):
                return materias, calificaciones
            else:
                print("Respuesta no reconocida. Responde 's' o 'n'.")


def calcular_promedio(calificaciones):
    """Devuelve el promedio de una lista de calificaciones (0.0 si está vacía)."""
    if len(calificaciones) == 0:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """Separa los índices de las calificaciones en aprobadas y reprobadas."""
    aprobadas = []
    reprobadas = []

    for indice, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """Devuelve el índice de la calificación más alta y el de la más baja."""
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min


def main():
    print("=== Calculadora de Promedios Escolares ===\n")

    materias, calificaciones = ingresar_calificaciones()

    if len(materias) == 0:
        print("\nNo se ingresó ninguna materia. Finalizando el programa.")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas, reprobadas = determinar_estado(calificaciones, 5.0)
        indice_max, indice_min = encontrar_extremos(calificaciones)

        print("\n=== Resumen Final ===")
        print("\nMaterias y calificaciones:")
        for indice, nombre in enumerate(materias):
            print(f"  - {nombre}: {calificaciones[indice]:.1f}")

        print(f"\nPromedio general: {promedio:.2f}")

        print("\nMaterias aprobadas:")
        if len(aprobadas) == 0:
            print("  Ninguna")
        else:
            for indice in aprobadas:
                print(f"  - {materias[indice]}: {calificaciones[indice]:.1f}")

        print("\nMaterias reprobadas:")
        if len(reprobadas) == 0:
            print("  Ninguna")
        else:
            for indice in reprobadas:
                print(f"  - {materias[indice]}: {calificaciones[indice]:.1f}")

        print(f"\nMejor materia: {materias[indice_max]} con {calificaciones[indice_max]:.1f}")
        print(f"Peor materia: {materias[indice_min]} con {calificaciones[indice_min]:.1f}")

    print("\n¡Gracias por usar la calculadora de promedios! Hasta pronto.")


if __name__ == "__main__":
    main()
