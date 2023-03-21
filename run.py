from project import app, db
import project.data.constantes as createConst

with app.app_context(): 
    #Insercion de los valores para las constantes en la DB
    createConst.actConst()
    db.create_all()

if __name__ == "__main__":
    app.run()