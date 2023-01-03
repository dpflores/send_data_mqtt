import paho.mqtt.client as mqtt
import random
import time

# Dirección IP del servidor MQTT y puerto
MQTT_SERVER = "192.168.88.187"
MQTT_PORT = 1883

# Usuario y contraseña
username = "test1"
password = "1234567890"

# Nombres de los tópicos a los que se publicarán los datos
topic1 = "datos/dato1"
topic2 = "datos/dato2"
topic3 = "datos/dato3"

# Crea una instancia del cliente MQTT y autenticación
client = mqtt.Client()
client.username_pw_set(username, password)


# Conecta el cliente al servidor
client.connect(MQTT_SERVER, MQTT_PORT)
print("sending data...")
# Envía los datos en un loop infinito
while True:
    # Genera tres valores aleatorios entre 0 y 100
    data1 = random.randint(0, 100)
    data2 = random.randint(0, 100)
    data3 = random.randint(0, 100)

    # Publica los datos en los tópicos correspondientes
    client.publish(topic1, data1)
    client.publish(topic2, data2)
    client.publish(topic3, data3)

    # Espera 5 segundos antes de enviar los siguientes datos
    time.sleep(5)

# Cierra la conexión
client.disconnect()