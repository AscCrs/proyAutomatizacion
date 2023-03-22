from project import app, db
import project.data.constantes as createConst
import project.data.test.sensores_test as testSens 
import project.data.test.variables_test as testVar
import project.data.test.variablesatm_test as testVaratm
#from multiprocessing import Process
#import project.data.getdata as gd

with app.app_context(): 
    #Insercion de los valores para las constantes en la DB
    createConst.actConst()
    testVar.actVariables()
    testVaratm.actVaratm()
    testSens.actSensores()
    db.create_all()

if __name__ == "__main__":
    continue_exec = True
    #sensores_Temp = Process(target=gd.getTemperature(continue_exec))
    #sensores_Temp.start()

    app.run()

    continuar_ejecucion = False
    #sensores_Temp.join()  # Esperar a que el proceso en segundo plano termine de ejecutarse

    #! Segunda forma de continuar con el proceso de recoleccion de temp
    # try:
    #     app.run()
    # except KeyboardInterrupt:
    #     # Si el usuario presiona Ctrl+C, detener el proceso en segundo plano
    #     sensores_Temp.terminate()
    #     sensores_Temp.join()

    # # Si ocurre algún otro error, detener el proceso en segundo plano
    # sensores_Temp.terminate()
    # sensores_Temp.join()
