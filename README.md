# Service working

Tu run the setup.py, you must clone this repository in the `/root` folder or change the directory in line 9 of the `.service` file. Then run

```
python3 setup.py
```

To watch the status run

```
systemctl status send_mqtt.service
```

If it is running, it's okay