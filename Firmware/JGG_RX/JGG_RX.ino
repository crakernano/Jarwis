/*
  Simple example for receiving
  
  https://github.com/sui77/rc-switch/
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

int mensaje=0;
String msg = "";
String lastMsg = "";
int recibido;

void setup() {
  Serial.begin(9600);
  Serial.println("READY");
  mySwitch.enableReceive(D3);  // Receiver on interrupt 0 => that is pin #2
  
}

void loop() {

    
  if (mySwitch.available()) {

    recibido = mySwitch.getReceivedValue(); 
    msg = (char)recibido;
    if(!msg.equals(lastMsg)){
      if(mySwitch.getReceivedBitlength() == 16){
        //cabecera        
        if(msg.equals("t")){
          Serial.println("Temperatura: ");
        }else if(msg.equals("h")){
          Serial.println("Humedad: ");
        }else if(msg.equals("l")){
          Serial.println("Luz: ");
        }else if(msg.equals("s")){
          Serial.println("Humedad del suelo: ");
        }else if(msg.equals("i")){
          Serial.println("ID: ");
        }else{
          Serial.print("bad header: ");
          Serial.println(msg);
        }
      }else if(mySwitch.getReceivedBitlength() == 24){
        
        //dato
        Serial.println(recibido);
      }
      
     
     
    }
    
  lastMsg = msg;
    mySwitch.resetAvailable();
  }
}
