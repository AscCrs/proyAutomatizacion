from project.data.models import Constantes
from project import db

propiedades_aire = [
    (0, 1.292, 1006),
    (5, 1.269, 1006),
    (10, 1.246, 1006),
    (15, 1.225, 1007),
    (20, 1.204, 1007),
    (25, 1.184, 1007),
    (30, 1.164, 1007),
    (35, 1.145, 1007),
    (40, 1.127, 1007),
    (45, 1.109, 1007),
    (50, 1.092, 1007)
]   
def delete_all_constantes():
    db.session.query(Constantes).delete()
    db.session.commit()

def actConst():
    delete_all_constantes()
    it = 1
    # Verificar si los datos ya existen en la tabla Constantes
    if db.session.query(Constantes).count() == 0:
        # Agregar los datos a la tabla
        for temperatura, densidad, calorEspecif in propiedades_aire:
            constantes = Constantes(
                it,
                temperatura, 
                densidad, 
                calorEspecif
            )
            db.session.add(constantes)
            it += 1;
        db.session.commit()
    else:
        print('Elemento duplicado')