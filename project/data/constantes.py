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

def actConst():
    for temperatura, densidad, calorEspecif in propiedades_aire:
        constantes = Constantes(
            temperatura, 
            densidad, 
            calorEspecif
        )
        db.session.add(constantes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    db.session.commit()