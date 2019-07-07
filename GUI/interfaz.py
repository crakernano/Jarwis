from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import commands
import socket
#import netifaces as ni
import fcntl
import struct



def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


class TestApp(App):


    def build(self):
        layout = BoxLayout(orientation='vertical')

        #(r, g, b, a) tuple
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)
	yellow = (2.5, 2.5, 0, 2.5)

        btnChangeDisplay =  Button(text='HDMI', background_color=blue, font_size=40)
        btnChangeDisplay.bind(on_press=self.callback)

	btnShutdown = Button(text='Apagar', background_color=red, font_size=40)
	btnShutdown.bind(on_press=self.apagador)

	btnChangeIP = Button(text='Cambiar IP', background_color=yellow, font_size=40)
	btnChangeIP.bind(on_press=self.change_IP)

	ipLabel = Label(text=get_ip_address(), font_size ='30sp')
        self.label = Label(text="OpenToll 0.1", font_size='40sp')

        layout.add_widget(btnChangeDisplay)
	layout.add_widget(btnShutdown)
        layout.add_widget(self.label)
	layout.add_widget(ipLabel)
	layout.add_widget(btnChangeIP)

	return layout

    def callback(self, event):
        print("Pasando a HDMI...")  # test
        self.label.text = "Transfiriendo a HDMI"
	#subprocess.call(['./home/pi/LCD-show/LCD-hdmi']) python3
	commands.getoutput('./home/pi/LCD-show/LCD-hdmi')

    def apagador(self,event):
	print("Apagando")
	self.label.text="Apagando..."
	#subrpocess.call(['sudo shutdown', '-h 1']) python3
	#commands.getoutput('sudo shutdown -h 0') #python2

    def change_IP(self,event):
	print("Ventana de configuracion de la IP")
	self.label.text = "Configurar IP"
	commands.getoutput('python confIp.py') #python2


TestApp().run()
