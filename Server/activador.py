import urllib2
import sys

modulo = str(sys.argv[1])

def activador(url):
	print(url)
	f = urllib2.urlopen(url)
	print f.read()
	f.close()

activador(modulo)
