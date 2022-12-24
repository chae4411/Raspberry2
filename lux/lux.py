import serial
import time 
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb

port = '/dev/ttyACM0'
brate = 9600

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)


while True:
    time.sleep(1)
    if seri.in_waiting !=0:
        content = seri.readline()
        data =[{
             'measurement' :'lux',
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'lux' : int(content.decode()),
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','lux')
    except Exception as e:
        print ("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print ("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")


         

