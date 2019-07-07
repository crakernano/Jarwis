import urllib2

class Modulos:

    # Constructor de clase
    def __init__(self, id, tipo, estado, ubicacion):
        self.id = id
        self.tipo = tipo
        self.estado = estado
        self.ubicacion = ubicacion
        print('Nuevo modulo',self.id)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.tipo, self.ubicacion)


def statusModulo(id):
	dt = datetime.datetime.now()	
	t = datetime.timedelta(hours=3)
		
	if getUltimoRegistro(id) < dt+t:
		return true
	else:
		return false

def checkModulos(modulos):
   	for modulo in modulos:
   		if statusModulo(modulo.id):
   			yield modulo

def checkAlive(ip):
	try:
   		f = urllib2.urlopen("http://"+ip)		
		f.close()
		return 1
	except urllib2.URLError:
		return -1
