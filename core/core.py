import log
import modulos
import crud
import localSensors
import temporizadores

#log.createLog("hola mundo")
#print(log.readLog("y"))

#print(modulos.checkAlive("192.168.1.119"))
#print(crud.verRegistros())
#print(crud.getUltimoRegistro("1431241"))
#print(crud.datosConexion())

#crud.crear_bd()

#modulo = ('1431241','EM','activo','terraza')
#crud.agregarModulo(modulo)

#crud.verModulo("1431241")

#print(localSensors.getHumedity())
#print(localSensors.getTemerature())

temporizadores.timeActive("192.168.1.23", 2)