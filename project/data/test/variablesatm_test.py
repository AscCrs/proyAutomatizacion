from project.data.models import VariablesAtm
from project import db

def delete_all_variablesatm():
    db.session.query(VariablesAtm).delete()
    db.session.commit()

# Definicion de las constantes sobre las cuales se va a trabajar
af = 0.7
waf = 1.1
Taf = 317.95

def actVaratm():
    delete_all_variablesatm()
    it = 1

    if db.session.query(VariablesAtm).count() == 0:
        atm = VariablesAtm(
            it,
            af,
            waf,
            Taf
        )
        db.session.add(atm)
        db.session.commit()

    else:
        print('Elemento duplicado')