# Run this if you want to have this as a service
import os

def main():
	print("Setting the openVPN")
	os.system("cp send_mqtt.service /etc/systemd/system")
	os.system("systemctl enable send_mqtt.service")
	os.system("systemctl start send_mqtt.service")

	os.system("pip3 install -r requirements.txt")

	print("done")
if __name__ == '__main__':
	main()