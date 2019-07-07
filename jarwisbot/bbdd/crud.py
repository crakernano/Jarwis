import pymysql


# Abre conexion con la base de datos
db = pymysql.connect("localhost","jarwis","d24m31989","jarwis")


# prepare a cursor object using cursor() method
cursor = db.cursor()

# ejecuta el SQL query usando el metodo execute().
cursor.execute("SELECT * FROM registros;")

# procesa una unica linea usando el metodo -> fetchone().
data = cursor.fetchall()
print ("Database version : {0}".format(data))

# desconecta del servidor
db.close()