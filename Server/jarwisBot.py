
#!/usr/bin/python
# -*- coding: <encoding name> -*-
import telebot 
import subprocess
import urllib

TOKEN = "619324955:AAEUM8yFEeXv-l8nCYrJN7Nh97UdYzvf0hQ"
bot = telebot.TeleBot(TOKEN)              

def public_ip():
	lista = "0123456789."
	ip=""

	datos = urllib.urlopen('http://checkip.dyndns.org').read() # esta URL puede ser reemplazada con otra que preste similar servicio
	for x in str(datos):
        	if x in lista:
                	ip += x
	return ip

def leeMensaje(mensajes):
    for mensaje in mensajes: #Este for each recorre cada mensaje dentro de la estructura que obtiene el bot de Telegram
        id_chat = mensaje.chat.id #Se necesita obtener el id del mensaje para saber a quien responder
        #Aqui se pueden hacer muchas cosas como por ejemplo saludar...
        bot.send_message(id_chat, 'Recibido') 

bot.set_update_listener(leeMensaje)

@bot.message_handler(commands=['ayuda'])
def ayudar(mensaje):
     id_chat= mensaje.chat.id #El id del chat para saber el destino de la respuesta que va a enviar el bot
     bot.send_message( id_chat, 'ayuda => Envia la lista de comandos.\napagar=> Permite apagar luces y enchufes. \nyourIp=>Muestra la IP publica.') 

@bot.message_handler(commands=['apagar'])
def apagar(mensaje):
	id_chat= mensaje.chat.id 
     	bot.send_message( id_chat, 'Apagando...')
	subprocess.call(['sudo','rpi-rf_send', '-g', '21', '-t', '2', '2729587968'])

@bot.message_handler(commands=['yourIp'])
def yourIp(mensaje):
	id_chat= mensaje.chat.id 
        bot.send_message( id_chat, 'Mi IP es: '+public_ip())

bot.polling(none_stop=True)
