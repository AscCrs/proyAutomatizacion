import project.data.constantes as createConst
from project import app, db

with app.app_context(): 
    db.create_all()
    #Insercion de los valores para las constantes en la DB
    createConst.actConst()

if __name__ == "__main__":
    app.run()