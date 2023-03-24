import paho.mqtt.client as mqtt
import json
import random
import time

# Configuración del cliente MQTT
THINGSBOARD_HOST = '67.205.184.64'
ACCESS_TOKEN = 'ymQYDnqXHea2HhfTWtti'
TOPIC = 'v1/devices/me/telemetry'



client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

# Conexión al servidor MQTT de Thingsboard
client.connect(THINGSBOARD_HOST, 1883, 60)

# Ciclo principal del script
while True:
    # Generación de un dato aleatorio
    data = {'value': random.randint(0, 100)}
    print(data)
    # Envío de los datos por MQTT
    client.publish(TOPIC, json.dumps(data))

    time.sleep(2)
    data2 = {'value2': random.randint(0, 100)}
    print(data2)
    # Envío de los datos por MQTT
    client.publish(TOPIC, json.dumps(data2))
    # Pausa del script por 5 segundos
    time.sleep(5)

# Desconexión del cliente MQTT
client.disconnect()