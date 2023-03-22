from project.data.models import Variables
from project import db

def delete_all_constantes():
    db.session.query(Variables).delete()
    db.session.commit()

# Definicion de constantes temporales
hum_super   = 0.2
altura_cv   = 0.38
desp_cv     = 0.27 
long_rugv   = 0.05
LAI      = 0.0253
dens_plant  = 542.63
dens_tierra = 950
qa = 0.072
qf = dens_tierra / dens_plant

def actVariables():
    delete_all_constantes()
    # Verificar si los datos ya existen en la tabla Constantes
    if db.session.query(Variables).count() == 0:
        # Agregar los datos a la tabla
        variables = Variables(
            hum_super, 
            altura_cv, 
            desp_cv, 
            long_rugv,
            LAI, 
            qf,
            qa
        )
        db.session.add(variables)
        it += 1;
        db.session.commit()
    else:
        print('Elemento duplicado')