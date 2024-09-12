estudiantes: dict = {
    'Xavier':['POO', 'Base de Datos', 'Patrones de diseño'],
    'Juan':['POO', 'Matematica', 'redes']
}


def devolver_materias(estudiante: str) -> list[str]:
    return estudiantes[estudiante]