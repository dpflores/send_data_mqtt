from axotec.accelerometer import Accelerometer
import paho.mqtt.client as mqtt
import time

accel = Accelerometer()


USERNAME = 'AxotecPiloto'
PASSWORD = '1234567890'

# Server de ACME
MQTT_SERVER = 'soldier.cloudmqtt.com'
MQTT_PORT = 15258

# Nombres de los tópicos a los que se publicarán los datos
topic1 = "datos/accelx"
topic2 = "datos/accely"
topic3 = "datos/accelz"

# Crea una instancia del cliente MQTT
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

# Conecta el cliente al servidor
client.connect(MQTT_SERVER, MQTT_PORT,60)
client.loop_start()
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
    time.sleep(5)
    print(data1)
    client.loop()
    

# Cierra la conexión
client.disconnect()
