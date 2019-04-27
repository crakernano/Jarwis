/*
  Example for receiving
  
  https://github.com/sui77/rc-switch/
  
  If you want to visualize a telegram copy the raw data and 
  paste it into http://test.sui.li/oszi/
*/

#include <RCSwitch.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "MiFibra-6FD8";
const char* password = "anjx3Z3c";
const int id = ESP.getChipId();

String dato = "";
int temperatura= 0;
int humedad= 0;
int luz= 0;
int suelo= 0;
int modulo_id = 0;

RCSwitch mySwitch = RCSwitch();
ESP8266WebServer server(80);
  
void pagina(){
  String web = "<!doctype html> <html> <head> <meta charset=utf-8 /> <meta name=description content='Resumen del contenido de la página'> <meta charset=utf-8> <meta name=viewport content='width=device-width, initial-scale=1'> <link rel=stylesheet href=https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css> <script src=https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js></script> <script src=https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js></script> <title>Modulo Jarwis - Jarwis Garden Guarduan - Modulo Jarwis</title> <style type=text/css>.progressbar{-moz-orient:vertical;display:inline}label{background-color:green;padding:10px;border:2px black solid;color:white}.container{width:400px;height:200px;position:relative;top:30%;left:50%;overflow:hidden;text-align:center;transform:translate(-50%,-50%)}.GaugeMeter{position:Relative;text-align:Center;overflow:Hidden;cursor:Default;display:inline-block}.GaugeMeter SPAN,.GaugeMeter B{width:54%;position:Absolute;text-align:Center;display:Inline-Block;color:RGBa(0,0,0,.8);font-weight:100;font-family:'Open Sans',Arial;overflow:Hidden;white-space:NoWrap;text-overflow:Ellipsis;margin:0 23%}.GaugeMeter[data-style='Semi'] B{width:80%;margin:0 10%}.GaugeMeter S,.GaugeMeter U{text-decoration:None;font-size:.60em;font-weight:200;opacity:.6}.GaugeMeter B{color:#000;font-weight:200;opacity:.8}.representaciones{padding-left:30%;padding-top:10%;padding-bottom:30%}article{margin-top:5%;align-content:center}.btn-circle.btn-xl{width:70px;height:70px;padding:10px 16px;border-radius:35px;font-size:24px;line-height:1.33}.btn-circle{width:30px;height:30px;padding:6px 0;border-radius:15px;text-align:center;font-size:12px;line-height:1.42857}</style> </head> <body> <header> <div class=row style=margin-right:0> <div class=col-md-2> <span class=badge style=background:#FFF;margin-top:10%;margin-left:10%><img src=https://raw.githubusercontent.com/trastejant/jarwis/master/Fotos/jarvisLogo.svg.png height=53px></span> </div> <div class=col-md-10 style=background:#2f323e;color:#FFF> <div class=page-header> <h1> <small>Panel Control</small> </h1> </div> </div> </div> </header> <nav class='navbar navbar-inverse'> <div class=container-fluid> <div class=navbar-header> <a class=navbar-brand href=#>Opciones</a> </div> <ul class='nav navbar-nav'> <li class=active><a href=.>Estado</a></li> <li><a href=/config>Configuracion</a></li> </ul> </div> </nav><div class='alert alert-success'><strong>Ok </strong> El módulo funciona con normalidad</div><div class='container-fluid'> <div class='row'> <div class='col-md-8'> <div class='panel panel-default'> <div class='panel-heading'>Datos actuales</div> <div class='panel-body'><div class=GaugeMeter id=PreviewGaugeMeter_1 data-percent='"+String(suelo)+"' data-append=% data-size=180 data-theme=Blue data-back=RGBa(0,200,0,.1) data-animate_gauge_colors=1 data-animate_text_colors=5 data-width=5 data-label=Terreno data-label_color=#F00 data-stripe=5></div><div class=GaugeMeter id=PreviewGaugeMeter_2 data-percent='30' data-append=% data-size=180 data-theme=Blue data-back=RGBa(0,0,0,.1) data-animate_gauge_colors=1 data-animate_text_colors=1 data-width=5 data-label=Luminosidad data-label_color=#000 data-stripe=2></div><div class=GaugeMeter id=PreviewGaugeMeter_3 data-percent='10' data-append=ºC data-size=180 data-theme=Blue data-back=RGBa(0,0,0,.1) data-animate_gauge_colors=1 data-animate_text_colors=1 data-width=15 data-label=Temperatura data-label_color=#000 data-stripe=2></div><div class=GaugeMeter id=PreviewGaugeMeter_4 data-percent='20' data-append=% data-size=180 data-theme=Blue data-back=RGBa(0,0,0,.1) data-animate_gauge_colors=1 data-animate_text_colors=1 data-width=15 data-label=Humedad data-label_color=#000 data-stripe=2></div> </div></div> </div><div class='col-md-4'> <div class='panel panel-primary'> <div class='panel-heading'>Control</div> <div class='panel-body'> <center> <form action=''> <button type='button' class='btn btn-primary' style='margin-bottom:3%'>Estado actual <span class='badge'>Desconectado</span></button> <br><button type='submit' value='1' name='led' class='btn btn-success'>Encender</button></form> </center> </div> </div></div> </div> </div> <script src=http://code.jquery.com/jquery-2.1.4.min.js></script> <script src=http://www.jqueryscript.net/demo/Customizable-Animated-jQuery-HTML5-Gauge-Meter-Plugin/jquery.AshAlom.gaugeMeter-2.0.0.min.js></script> <script>$('.GaugeMeter').gaugeMeter();</script> <script type=text/javascript>var _gaq=_gaq||[];_gaq.push(['_setAccount','UA-36251023-1']);_gaq.push(['_setDomainName','jqueryscript.net']);_gaq.push(['_trackPageview']);(function(){var c=document.createElement('script');c.type='text/javascript';c.async=true;c.src=('https:'==document.location.'https://ssl':'http://www')+'.google-analytics.com/ga.js';var a=document.getElementsByTagName('script')[0];a.parentNode.insertBefore(b,a)})();</script> <footer style='background:#2f323e;color:#FFF;padding:5px'><div class='row'> <div class='col-md-4'> chipID:16334344 </div> <div class='col-md-4'> <div class='col-sm-6'><center><a href='https://github.com/trastejant/jarwis'><img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGQ9Ik05IDE5Yy01IDEuNS01LTIuNS03LTNtMTQgNnYtMy44N2EzLjM3IDMuMzcgMCAwIDAtLjk0LTIuNjFjMy4xNC0uMzUgNi40NC0xLjU0IDYuNDQtN0E1LjQ0IDUuNDQgMCAwIDAgMjAgNC43NyA1LjA3IDUuMDcgMCAwIDAgMTkuOTEgMVMxOC43My42NSAxNiAyLjQ4YTEzLjM4IDEzLjM4IDAgMCAwLTcgMEM2LjI3LjY1IDUuMDkgMSA1LjA5IDFBNS4wNyA1LjA3IDAgMCAwIDUgNC43N2E1LjQ0IDUuNDQgMCAwIDAtMS41IDMuNzhjMCA1LjQyIDMuMyA2LjYxIDYuNDQgN0EzLjM3IDMuMzcgMCAwIDAgOSAxOC4xM1YyMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIvPgo8L3N2Zz4K' width='32px'></a></center></div> </div> <div class='col-md-4'> IP:192.168.1.37</div> </div> </footer> </body> </html>";
  server.send(200, "html",web);
}
void setup() {
  Serial.begin(9600);  

  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);



  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    Serial.print ( "." );

  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  //Configuracion de la navegacion
  server.on("/", pagina);
  
  //Inicializacion del servidor web
  server.begin();

  delay(5000);
  
  mySwitch.enableReceive(D3);  // Receiver on interrupt 0 => that is pin #2
}

void loop() {
  if (mySwitch.available()) {
    dato = mySwitch.getReceivedValue();
    Serial.print("DATO:");
    Serial.println(dato);

    if(dato[0]=='2'){
      Serial.print("Temperatura: ");
      temperatura = dato.toInt() - 200;
      Serial.println(temperatura);
    }else if(dato[0]=='3'){
      Serial.print("Humedad: ");
      humedad = dato.toInt() - 300;
      Serial.println(humedad);
    }else if(dato[0]=='4'){
      Serial.print("Luminosidad: ");
      luz = dato.toInt() - 400;
      Serial.println(temperatura);
    }else if(dato[0]=='5'){
      Serial.print("Humedad del terreno: ");
      suelo = dato.toInt() - 500;
      Serial.println(suelo);
    }else if(dato.toInt()>1000){            
      Serial.print("ID: ");
      Serial.println(dato);
    }
    mySwitch.resetAvailable();
  }
  server.handleClient();
}
