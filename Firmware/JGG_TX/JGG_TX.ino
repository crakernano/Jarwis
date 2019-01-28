/*
  ######################################################################################################################################################
  #                                                 Programa para la placa Jarvis Garden Guardian (JGG)                                                #
  ######################################################################################################################################################
  #                                                                                                                                                    # 
  # Programa cargado en el Attiny85 que emplea el módulo JGG                                                                                           #
  # Este programa lee los sensores de humedad del terreno, temperatura, humedad ambiental y luz y los devuelve por I2C para transmitirlos via WiFi o   #
  # los envia via por por RF a 433Mhz.                                                                                                                 #
  #                                                                                                                                                    #
  #    ____                                                                                                                                            #
  # Rst-|   |-Vcc   0 -> SDA                                                                                                                           #
  # A3 -|   |-2     1 -> MÓDULO 433 Mhz                                                                                                                #
  # A2 -|   |-1     2 -> SCL                                                                                                                           # 
  # GND-|___|-0     A2 -> LDR                                                                                                                          # 
  #                 A3 -> SENSOR DE HUMEDAD DEL TERRENO                                                                                                # 
  ######################################################################################################################################################

*/

#include "Arduino.h"
#include <RCSwitch.h>
#include "DHT12.h"


#define LDR_PIN A2
#define GND_PIN A3
#define TX_PIN 1
#define SDA 0
#define SCL 2

bool dht12Read = false;
unsigned long previousMillis = 0; 
unsigned long frecuencia = 3000;//1 seg
uint32_t T_DeepSleep = 1800e6; //30Min

DHT12 dht12(SDA,SCL);
RCSwitch mySwitch = RCSwitch();


void setup() {
  
  mySwitch.enableTransmit(TX_PIN);//Establecemos el pin al que está conectado el emisor  

  
  dht12.begin();//Inicialización del sensor de humedad y temperatura

}


void loop() {
  if ((millis() - previousMillis) >= frecuencia){
    previousMillis = millis();
/*
  if (isnan(dht12.readTemperature()) || isnan(dht12.readHumidity())) {

      dht12Read = false;
    }
*/
  if (dht12Read){

    mySwitch.send('t', 16);//la cabecera 't' indica temperatura
    mySwitch.send(dht12.readTemperature(), 24);//enviamos la lectura correspondiente a la temperatura 
    delay(1000);
  
    mySwitch.send('h', 16);// la cabecera 'h' indica humedad AMBIENTAL
    mySwitch.send(dht12.readHumidity(), 24);//lectura de humedad del sensor
    delay(1000);
  }

  mySwitch.send('l', 16);// la cabecera 'l' luz
  mySwitch.send(analogRead(LDR_PIN), 24);//lectura de la LDR
  delay(1000);

  mySwitch.send('s', 16);// la cabecera 's' humedad del SUELO
  mySwitch.send(analogRead(GND_PIN), 24);//lectura de humedad del sensor
  delay(1000);

  
  }
  
}
