import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import json
import random

def main():
    myConnection = psycopg2.connect(host = 'ruby.db.elephantsql.com',
                                user= 'uicdhpnp', password ='Kfp61NZwnYQVCSDf-zl7Jae836R2u0Fn',
                                dbname= 'uicdhpnp')
    
    host = "broker.hivemq.com"

    client = paho.mqtt.client.Client()

    client.on_connect = on_connect

    client.message_callback_add('plaza/tienda/1', on_message_postgre)

    client.message_callback_add('plaza/tienda/2', on_message)

    client.connect(host=host) 

    client.loop_forever()


def on_connect(client, userdata, flags, rc):    
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='plaza/#', qos = 1)  
    

def on_message(client, userdata, message):   
    a = json.loads(message.payload)
    print(a) 
    print(message.qos)   
    print('------------------------------')     
    
def on_message_postgre(client, userdata, message):   
    a = json.loads(message.payload)
    print(a) 
    print(message.qos)   
    doQuery(a)
    print('------------------------------')  



def doQuery(a):
    cur = myConnection.cursor()
    cur.execute("INSERT INTO rotacion (fecha, estante, sucursal) VALUES (%s, %s, %s);",
                (a["fecha"],a["estante"],a["sucursal"]))
    myConnection.commit()

if __name__ == "__main__":
    main()