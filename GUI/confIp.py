
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import commands

class TestApp(App):
    def build(self):

        oct1 = 0
        layout = BoxLayout(orientation='vertical')
	
    	octetos = GridLayout(cols=4, row_force_default=True, row_default_height=40)
    	
    	self.new1oct = TextInput(multiline=False, width=100)
        self.new1oct.text = str(oct1)
    	octetos.add_widget(self.new1oct)
        
            
        self.new2oct = TextInput(multiline=False)
        octetos.add_widget(self.new2oct)
        
        self.new3oct = TextInput(multiline=False)
        octetos.add_widget(self.new3oct)
            
        self.new4oct = TextInput(multiline=False)
        octetos.add_widget(self.new4oct)

        botonera = GridLayout(cols=8, row_force_default=True, row_default_height=40)
        botonera.add_widget(Button(text='+', size_hint_x=None, width = 80))
        
        btnIncrementoOct1 = Button(text='-', size_hint_x=None, width = 80)
        botonera.add_widget(btnIncrementoOct1)
        btnIncrementoOct1.bind(on_press=self.aumentarOctetoUno)

        botonera.add_widget(Button(text='+', size_hint_x=None, width = 80))
        botonera.add_widget(Button(text='-', size_hint_x=None, width = 80))
        botonera.add_widget(Button(text='+', size_hint_x=None, width = 80))
        botonera.add_widget(Button(text='-', size_hint_x=None, width = 80))
        botonera.add_widget(Button(text='+', size_hint_x=None, width = 80))
        botonera.add_widget(Button(text='-', size_hint_x=None, width = 80))
            # use a (r, g, b, a) tuple
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)

        self.label = Label(text="Cambiar IP", font_size='50sp')
    	#self.newIP = TextInput(multiline=False)
        opciones = GridLayout(cols=8, row_force_default=True, row_default_height=40)
    	btnAceptar =  Button(text='Guardar', font_size=40)
        btnAceptar.bind(on_press=self.aceptar)

    	btnCancelar = Button(text='Cancelar', font_size=40)
    	btnCancelar.bind(on_press=self.cancelar)

        opciones.add_widget(btnAceptar)
        opciones.add_widget(btnCancelar)

        layout.add_widget(self.label)
        layout.add_widget(octetos)
    	layout.add_widget(botonera)
        layout.add_widget(opciones)
    	
    	


        return layout

    def cancelar(self, event):
        print("Cambio cancelado")  # test
        self.label.text = "Cancelado"
	#subprocess.call(['./home/pi/LCD-show/LCD-hdmi']) python3
	commands.getoutput('python interfaz.py')

    def aceptar(self,event):
	print("Cambiando IP")
	self.label.text="Cambiando..."
	#subrpocess.call(['sudo shutdown', '-h 1']) python3
	#python2
	commands.getoutput('sudo ifconfig eth0 down')
	commands.getoutput('sudo ifconfig eth0 192.168.1.12')
	commands.getoutput('sudo ifconfig eth0 up')

    def aumentarOcteto(cuadroOCteto,valor):
        valor = valor + 1
        cuadroOCteto.text = valor

    def aumentarOctetoUno(self,event):
        oct1 = oct1 + 1
        new1oct.text = oct1
        print(oct1)


TestApp().run()
