 #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    from kivy.app import App
    from kivy.clock import Clock
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.uix.boxlayout import BoxLayout
    from kivy.properties import ObjectProperty, StringProperty
    import paho.mqtt.client as mqtt
    import RPi.GPIO as GPIO
    import json
    import time, datetime

    class ScreenManagement(ScreenManager):
        pass

    class Main(Screen):
        inoutflow = StringProperty()
        freshexh = StringProperty()
        tacho = StringProperty()
        co2 = StringProperty()
        def setVent(self,percent):
            print('button state is: ', percent)
            message = "{\"flow-rate\":\"" + str(percent) + "\"}"
            mqttc.publish('weigus/attic/attic/ventilation',message)

    class Setup(Screen):
        pass

    class pitouconApp(App):
        def build(self):
            global SM #ScreenManager
            global s
            SM = self.root
            s = SM.get_screen('main')

        def on_start(self):
            global mqttc
            global switch_pin
            switch_pin = 3
            global switch_old
            switch_old = 1
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(switch_pin, GPIO.IN)
            clientID   = "pitoucon"
            brokerIP   = "192.168.1.111"
            brokerPort = 1883
            topic      = "mytopic"
            # Callback if CONNACK response from the server.
            def onConnect(client, userdata, flags, rc):
                print("Connected with result code " + str(rc))
                mqttc.subscribe(topic, 0)  # Subscribe (topic name, QoS)
            # Callback that is executed when we disconnect from the broker.
            def onDisconnect(client, userdata, message):
                print("Disconnected from the broker.")
            # Callback that is executed when subscribing to a topic
            def onSubscribe(client, userdata, mid, granted_qos):
                print('Subscribed on topic.')
            # Callback that is executed when unsubscribing to a topic
            def onUnsubscribe(client, userdata, mid, granted_qos):
                print('Unsubscribed on topic.')
            # Callback that is executed when a message is received.
            def onMessage(client, userdata, message):
                io=message.payload.decode("utf-8")
                if (io[2:6] != "flow") and (io[2:7] != "alive"):
                    try:
                        ioj=json.loads(io)
                        inflowTxt = ioj["inflow"]
                        outflowTxt = ioj["outflow"]
                        inOutTxt = "Temp   Hum      \n" + inflowTxt + "  IN \n\n" + outflowTxt + "  OUT"
                        s.inoutflow = inOutTxt
                        freshTxt = ioj["fresh"]
                        exhaustTxt = ioj["exhaust"]
                        freExTxt = "        Temp   Hum\nFRESH   " + freshTxt + "\n\nEXHAUST " + exhaustTxt
                        s.freshexh = freExTxt
                        tinTxt = ioj["tacho-in"]
                        if tinTxt[2]  == "%":
                            tinTxt = tinTxt[0:2]
                        else:
                            tinTxt = tinTxt[0:3]
                        toutTxt = ioj["tacho-out"]
                        if toutTxt[2]  == "%":
                            toutTxt = toutTxt[0:2]
                        else:
                            toutTxt = toutTxt[0:3]
                        tachoTxt = "Tacho I/O : " + tinTxt + "% " + toutTxt + "%"
                        s.tacho = tachoTxt
                        co2Txt = ioj["co2"]
                        co2Txt = "CO: " + co2Txt
                        s.co2 = co2Txt
                    except:
                       print("json error")
                else:
                    pass
            # Callback every 500ms to poll the backlight switch and act accordingly
            def poll_switch(dt):
                global switch_old
                switch = GPIO.input(switch_pin)
                if (switch != switch_old):
                    if switch:
                        with open("/sys/class/backlight/soc:backlight/brightness", "w") as f:
                            f.write('0')
                    else:
                        with open("/sys/class/backlight/soc:backlight/brightness", "w") as f:
                            f.write('1')
                switch_old = switch
            def send_alive(dt):
                samessage = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                samessage = "{\"alive\":\"" + samessage + "\"}"
                mqttc.publish('weigus/attic/attic/ventilation',samessage)

            mqttc = mqtt.Client(client_id=clientID, clean_session=True)
            mqttc.on_connect      = onConnect   # define the callback functions
            mqttc.on_disconnect   = onDisconnect
            mqttc.on_subscribe    = onSubscribe
            mqttc.on_unsubscribe  = onUnsubscribe
            mqttc.on_message      = onMessage
            mqttc.connect(brokerIP, brokerPort, keepalive=60, bind_address="")
            mqttc.loop_start() # start loop to process callbacks! (new thread!)
            event = Clock.schedule_interval(poll_switch, 1 / 2.) # poll switch 500ms
            event = Clock.schedule_interval(send_alive, 600) # send alive 10 min.
    if __name__ == "__main__":
        pitouconApp().run()
