import pymysql
import sqlite3

def limpiar(cadena):
	return cadena.strip('\n')

def datosConexion():
	fichero = open("conf.jws","r")
	datos = fichero.readlines()
	fichero.close()
	return map(limpiar,datos)

def verRegistros():
	datos = datosConexion()	
	db = pymysql.connect(datos[0],datos[1],datos[2],datos[3])
	cursor = db.cursor()
	cursor.execute("SELECT * FROM registros;")
	data = cursor.fetchall()	
	db.close()
	return data

def getUltimoRegistro(id):
	db = pymysql.connect(datos[0],datos[1],datos[2],datos[3])
	cursor = db.cursor()		
	cursor.execute("SELECT fecha FROM registros WHERE id_modulo="+id)
	resultado = cursor.fetchone()	
	db.close()
	return resultado

def datosLugar(id):
	db = pymysql.connect(datos[0],datos[1],datos[2],datos[3])
	cursor = db.cursor()		
	cursor.execute("SELECT * FROM registros WHERE id_modulo="+id)
	resultado = cursor.fetchall()	
	db.close()
	return resultado

def estadoLugar(id):
	db = pymysql.connect(datos[0],datos[1],datos[2],datos[3])
	cursor = db.cursor()		
	cursor.execute("SELECT * FROM registros WHERE id_modulo="+id)
	resultado = cursor.fetchone()	
	db.close()
	return resultado

#--

#crear base de datos
def crear_bd():
    conexion = sqlite3.connect("jarwis.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE modulos(
                id INTEGER PRIMARY KEY,
                tipo VARCHAR(100) NOT NULL,
                estado VARCHAR(20),
                ubicacion VARCHAR(50)
                )''')
    except sqlite3.OperationalError:
        print("La tabla modulos ya existe.")
    else:
        print("La tabla se ha creado correctamente.")
   
    conexion.close()

#insertar
def agregarModulo(modulo):    

    conexion = sqlite3.connect("jarwis.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO modulos VALUES (?,?,?,?)",modulo)

    except sqlite3.IntegrityError:
        print("El modulo ya existe")
    else:
        print("Modulo agregado correctamente")

    conexion.commit()
    conexion.close()

#consultar
def verModulos():
	conexion = sqlite3.connect("jarwis.db")
	cursor = conexion.cursor()  
	listaModulos=[]
	modulos = cursor.execute("SELECT * FROM modulos").fetchall()   
	for modulo in modulos:
		print(modulo)        
		listaModulos.append(modulo)

	conexion.close()

def verModulo(id):
	conexion = sqlite3.connect("jarwis.db")
	cursor = conexion.cursor()  

	modulo = cursor.execute("SELECT * FROM modulos WHERE id="+id).fetchone()   
	print(modulo)      
	return(modulo)


	conexion.close()