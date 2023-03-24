import paho.mqtt.client as mqtt
import json
import random
import time
from threading import Thread 

# Configuración del cliente MQTT
THINGSBOARD_HOST = '67.205.184.64'
ACCESS_TOKEN = 'ymQYDnqXHea2HhfTWtti'
TOPIC = 'v1/devices/me/telemetry'


client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

# Conexión al servidor MQTT de Thingsboard
client.connect(THINGSBOARD_HOST, 1883, 60)


def thread1(): 
    while True:
        data = {'estimated_speed': random.randint(0, 100)}
        print(data)
        # Envío de los datos por MQTT
        client.publish(TOPIC, json.dumps(data))

        time.sleep(0.1)

    
def thread2():
    while True:
        data2 = {'obd_speed': random.randint(0, 100)}
        print(data2)
        # Envío de los datos por MQTT
        client.publish(TOPIC, json.dumps(data2))
        # Pausa del script por 5 segundos
        time.sleep(0.2)


def thread3():
    while True:
        data3 = {'gps_speed': random.randint(0, 100)}
        print(data3)
        # Envío de los datos por MQTT
        client.publish(TOPIC, json.dumps(data3))
        # Pausa del script por 5 segundos
        time.sleep(1)


Thread(target = thread1).start() 
Thread(target = thread2).start()
Thread(target = thread3).start()