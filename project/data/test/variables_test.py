from project.data.models import Variables
from project import db

def delete_all_constantes():
    db.session.query(Variables).delete()
    db.session.commit()

# Definicion de constantes temporales
r_pr        = 0.2
Za          = 0.38
Zd          = 0.27 
Zo          = 0.05
LAI         = 0.0253
dens_plant  = 542.63
dens_tierra = 950
qa          = 0.072
qf          = dens_tierra / dens_plant

def actVariables():
    delete_all_constantes()
    # Verificar si los datos ya existen en la tabla Constantes
    if db.session.query(Variables).count() == 0:
        # Agregar los datos a la tabla
        variables = Variables(
            r_pr, 
            Za, 
            Zd, 
            Zo,
            LAI, 
            qf,
            qa
        )
        db.session.add(variables)
        db.session.commit()
    else:
        print('Elemento duplicado')