from axotec.accelerometer import Accelerometer
import paho.mqtt.client as mqtt
import time

accel = Accelerometer()



# Dirección IP del servidor MQTT y puerto
MQTT_SERVER = "192.168.88.187"
MQTT_PORT = 1883

# Nombres de los tópicos a los que se publicarán los datos
topic1 = "datos/accelx"
topic2 = "datos/accely"
topic3 = "datos/accelz"

# Crea una instancia del cliente MQTT
client = mqtt.Client()
client.set_timeout(30)
# Conecta el cliente al servidor
client.connect(MQTT_SERVER, MQTT_PORT)
print("sending data...")
# Envía los datos en un loop infinito
while True:
    # Genera tres valores aleatorios entre 0 y 100
    data1 = round(accel.getAx(),5)
    data2 = round(accel.getAy(),5)
    data3 = round(accel.getAz(),5)

    # Publica los datos en los tópicos correspondientes
    client.publish(topic1, data1)
    client.publish(topic2, data2)
    client.publish(topic3, data3)

    # Espera 5 segundos antes de enviar los siguientes datos
    time.sleep(0.1)
    print(data1)

# Cierra la conexión
client.disconnect()