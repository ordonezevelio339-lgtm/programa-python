# =========================================
# Problema 5 - Horas trabajadas del equipo
# =========================================

# Matriz con los trabajadores y las horas de trabajo
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["María", 7, 8, 8, 7, 8],
    ["Andrés", 9, 10, 9, 8, 10],
    ["Luisa", 6, 7, 8, 7, 6]
]

# Función para calcular las horas totales
def calcular_horas(recurso):

    nombre = recurso[0]

    # Sumar las horas de lunes a viernes
    total_horas = (
        recurso[1] +
        recurso[2] +
        recurso[3] +
        recurso[4] +
        recurso[5]
    )

    # Revisar si hizo sobretiempo
    if total_horas > 40:
        jornada = "Sobretiempo"
    else:
        jornada = "Horario Estándar"

    # Mostrar resultados
    print("----------------------------")
    print("Nombre:", nombre)
    print("Horas trabajadas:", total_horas)
    print("Clasificación:", jornada)


# Recorrer la matriz y llamar la función
for recurso in recursos:
    calcular_horas(recurso)