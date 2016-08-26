# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
"""
Incluir:
https://dev.mysql.com/doc/connector-python/en/ para MySQL he descargado mysql-connector-python-2.1.3
http://mosquitto.org el mqtt server para recepcion de los datos de los ESP
pip install paho-mqtt en el edison o similar:
git clone https://github.com/eclipse/paho.mqtt.python.git
cd org.eclipse.paho.mqtt.python.git
python setup.py install
en mosquitto.conf en el edison -> bind_dir 192.168.1.41

"""
import sys
import mysql.connector
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("hola")


def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.1.39", 1883, 60)
client.connect(host='192.168.1.39', port=1883, keepalive=60)
for i in Range(1,1000):
    client.publish('hola', 'asssss', qos=0)

if __name__ == "__main__":
    print("Hello World")

