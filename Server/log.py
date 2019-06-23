#registro de eventos
import datetime
import re
from io import open


def sucesosHoy():
	dt = datetime.datetime.now()
	fecha = dt.strftime('%d/%m/%Y')

	with open("log.txt", "r") as fichero:
		for linea in fichero:			

			if linea.find(str(fecha)) != -1:
				print(linea)


def sucesosAyer():
	dt = datetime.datetime.now()	
	t = datetime.timedelta(days=1)
	ayer = dt -t
	fecha = ayer.strftime('%d/%m/%Y')

	with open("log.txt", "r") as fichero:
		for linea in fichero:			

			if linea.find(str(fecha)) != -1:
				print(linea)


def createLog(evento):
	fichero = open('log.txt','a')
	dt = datetime.datetime.now()
	fecha = dt.strftime('%d/%m/%Y')
	hora = dt.strftime('%H:%M:%S')
	evento = str(fecha)+" - "+str(hora)+" - "+evento+"\n"
	fichero.write(evento.decode('utf-8'))
	fichero.close()

def readLog(time):

	if time == "t":		
		sucesosHoy()

	elif time == "y":
		sucesosAyer()

	else:
		fichero = open('log.txt','r')
		contenido = fichero.readlines()
		fichero.close
		return contenido

