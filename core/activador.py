""" Modulo de activacion de modulos Jarwis """
import urllib2
import sys

modulo = str(sys.argv[1])

def activador(url):
	""" Recibe una URL y envia una orden de activacion al modulo. """
	print(url)
	f = urllib2.urlopen(url)
	print f.read()
	f.close()

activador(modulo)

