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

    client.message_callback_add('plaza/tienda/1/almacen', on_message_almacen)

    client.message_callback_add('plaza/tienda/2/almacen', on_message_almacen)

    client.message_callback_add('plaza/tienda/1/temperatura', on_message_postgre)

    client.message_callback_add('plaza/tienda/2/temperatura', on_message_postgre)

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
    
def on_message_almacen(client, userdata, message):   
    a = json.loads(message.payload)
    print(a) 
    print(message.qos)   
    doQueryAlmacen(a)
    print('------------------------------')  



def doQueryAlmacen(a):
    cur = myConnection.cursor()
    cur.execute("INSERT INTO rotacion (fecha, estante, sucursal) VALUES (%s, %s, %s);",
                (a["fecha"],a["estante"],a["sucursal"]))
    myConnection.commit()

def on_message_temperatura(client, userdata, message):   
    a = json.loads(message.payload)
    print(a) 
    print(message.qos)   
    doQueryTemperatura(a)
    print('------------------------------')  



def doQueryTemperatura(a):
    cur = myConnection.cursor()
    cur.execute("INSERT INTO historico_temperatura  (fecha, estante, sucursal) VALUES (%s, %s, %s);",
                (a["fecha"],a["temperatura "],a["ID_Sucursal "]))
    myConnection.commit()

if __name__ == "__main__":
    main()