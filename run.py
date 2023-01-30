from project import app, db
from project.data import getdata

with app.app_context(): 
    db.create_all()

if __name__ == "__main__":
    app.run()