from estudiante import devolver_materias;

def estudiante_registrado_en_materia(estudiante: str ,materia: str) -> bool:
    materias: list = devolver_materias(estudiante);
    if(materias.count == 0): raise Exception()
    print(materias.__contains__(materia))
    
    
    
try:
    estudiante_registrado_en_materia('Xavier', 'POO');
except:
    print('El estudiante no se encuentra registrado')