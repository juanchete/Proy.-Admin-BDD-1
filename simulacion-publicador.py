import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import json
import random
import psycopg2
import pandas as pd

host = "broker.hivemq.com"
client = paho.mqtt.client.Client("Juancholo", False)
client.qos = 1
client.connect(host=host)

#Arreglos de utilidad

nameList = ['Pedro', 'Lana', 'Albert', 'Yangel','Sasuke', 'Elvis']


#Arreglos con data de la BDD
genteConocida = []
prodTienda1 = []
prodTienda2 = []


conocidos= 0
desconocidos =0 
#Arreglos con data de la BDD


meanAlimentosEnlatados = 2
stdAlimentosEnlatados = 1
meanAlimentosFrescos = 6
stdAlimentosFrescos = 3
meanAlimentosNoPerecederos = 3
stdAlimentosNoPerecederos = 1
meanAlcohol = 1
stdAlcohol = 1
meanSnacks = 6
stdSnacks = 4

capacidadEstanteEnlatados = 50
capacidadEstanteFrescos = 30
capacidadEstanteNoPerecederos = 90
capacidadEstanteAlcohol = 100
capacidadEstanteSnacks = 50

cantHoras = 24
hora =0
horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)

def main():
    host = "broker.hivemq.com"
    client = paho.mqtt.client.Client("Publicador", False)
    client.qos = 1
    client.connect(host=host)

    myConnection = psycopg2.connect(host = 'ruby.db.elephantsql.com',
                                user= 'uicdhpnp', password ='Kfp61NZwnYQVCSDf-zl7Jae836R2u0Fn',
                                dbname= 'uicdhpnp')

    cantHoras = 24
    hora =0
    horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
    days = 30

    nameList = ['Pedro', 'Lana', 'Albert', 'Yangel','Sasuke', 'Elvis']

    getClientes(genteConocida,myConnection)

    getProductos(prodTienda1,prodTienda2,myConnection)


    conocidos = 0
    desconocidos =0 
    #Arreglos con data de la BDD


    meanAlimentosEnlatados = 2
    stdAlimentosEnlatados = 1
    meanAlimentosFrescos = 6
    stdAlimentosFrescos = 3
    meanAlimentosNoPerecederos = 3
    stdAlimentosNoPerecederos = 1
    meanAlcohol = 1
    stdAlcohol = 1
    meanSnacks = 6
    stdSnacks = 4

    capacidadEstanteEnlatados = 50
    capacidadEstanteFrescos = 30
    capacidadEstanteNoPerecederos = 90
    capacidadEstanteAlcohol = 100
    capacidadEstanteSnacks = 50

    print('Comienza el frao')

    while(days>0):

        print('Dia numero ' + str(days))
        
        #Esto es mientras el Plaza este abierto
        print(horaBase)
        print(horaBase.hour)
        while(horaBase.hour < 22):

            print('Dia numero ' + str(days) + 'Hora numero '  +str(horaBase.hour) )
            
            orden = []

            tienda = int(np.random.uniform(0,1))

            if(tienda == 0):
                persona = entrarTienda(1,conocidos,desconocidos,horaBase)
                print('Entro a la teinda numero 1')
                x=0
                while x < len(prodTienda1):
                    agregarProductos(tienda,prodTienda1,orden,x)
                    x+=1
            else:
                persona = entrarTienda(2,conocidos,desconocidos,horaBase)
                print('Entro a la teinda numero 1')
                x=0
                while x < len(prodTienda2):
                    agregarProductos(tienda,prodTienda2,orden,x,horaBase)
                    x+=1
            pagar(persona, orden)

            horaBase = horaBase + datetime.timedelta(hours=1)
            time.sleep(0.2)
            
        horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
        horaBase = horaBase + datetime.timedelta(days=1)
        print(horaBase)
        print(horaBase.hour)
        
        days = days - 1
    #Variables de la BDD

def pagar (persona, orden) :
    
    total = 0
    x=0
    while x < len(orden):
        total = total + int(orden[x]['precio'])
        print('Se añadio una cantidad de '+ str(total))
        x+=1
    
    cuenta =  int(np.random.uniform(0,2))

    if cuenta == 0:
        cuenta = 'Mercantil'
    elif cuenta == 1:
        cuenta = 'Banesco'
    else:
        cuenta = 'Provincial'

    if persona['afiliado'] == True:
        puntos = total * 1.1

    print('Pago satisfactoriamente por la cantidad de '+ str(total))
        #mandar señal de aumentar puntos

    # payload = {
    #     'id_persona' : persona,
    #     'tienda' : tienda,
    #     'banco' : cuenta,

    # }

def entrarTienda (tienda,conocidos,desconocidos,hora):
    if(int(np.random.uniform(0,2)) == 0 and genteConocida!=0):

        
       
     
        
        persona = random.choice([a for a in genteConocida if a['afiliado'] ==True])
        if len(persona) > 0:
            print('Se escogera una persona conocida')
            conocidos += 1
            print(persona)
            return persona
        else:
            print('Se creara una persona')
            persona = crearPersona()
            desconocidos += 1
            
        
    else:
        desconocidos += 1
        persona = [a for a in genteConocida if a['afiliado'] ==False]
        if int(np.random.uniform(0,1)) == 0 and len(persona)>0:
            persona = random.choice(persona)
            
        else:
            persona = crearPersona()
    
    
    
    payload = {

        'id_cliente' : str(persona['id']),
        'fecha' : hora.date(),
        'id_sucursal': tienda



    }

    camaraSend(payload,myConnection)

    return persona

def crearPersona ():
    cedula = int(np.random.uniform(1000000,30000000))
    gender = random.choice(["M","F"])
    name = random.choice(nameList)
    payload = {
        "name" : str(name),
        "cedula": str(cedula),
        "gender": str(gender),
        "afiliado": False
    }
    print('Se crea a la persona')
    print(payload)
    genteConocida.append(payload)
    return payload 


def checkarSiMandoSeñal(produccion,tienda,estante,hora):

    
    popo = int(produccion[estante]['capacidad'])*0.2
    if popo >= int(produccion[estante]['cantidad_actual']):
        alerta = {
            'rellenar': 'El estante numero ' + str(estante)+ 'de la tienda' +  str(tienda) + 'tiene que ser rellenado',
            'estante': estante,
            'sucursal': tienda,
            'fecha': hora.date()
        }

        client.publish('plaza/tienda/'+str(tienda),json.dumps(alerta),qos=1)
        produccion[estante]['cantidad_actual'] = produccion[estante]['capacidad']
            
        x=0
        while x < len(produccion[estante]['productos']):
            produccion[estante]['productos'][x]['cantidad'] = produccion[estante]['productos'][x]['restock']
            x += 1
            
    





def agregarProductos (tienda,produccion, orden, estantes,hora):
    if tienda == 1:
        prod = random.choice(produccion[estantes]['productos'])
        indice = produccion[estantes]['productos'].index(prod)
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int (prod['cantidad'])))
        precio = int(prod['precio']) * cantidad
        print('escogio el producto con el id' + prod['id'] + ' cantidad '+ str(prod['cantidad']) + ' Cada uno cuesta' +str(prod['precio']) + ' el total a pagar es de '+ str(precio))
        produccion[estantes]['productos'][indice]['cantidad'] = int(produccion[estantes]['productos'][indice]['cantidad']) - cantidad
        produccion[estantes]['cantidad_actual'] = int(produccion[estantes]['cantidad_actual']) - cantidad
    else:
        prod = random.choice(produccion[estantes]['productos'])
        indice = produccion[estantes]['productos'].index(prod)
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int (prod['cantidad'])))
        precio = int(prod['precio']) * cantidad
        print('escogio el producto con el id' + prod['id'] + ' cantidad '+ str(prod['cantidad']) + ' Cada uno cuesta' +str(prod['precio']) + ' el total a pagar es de '+ str(precio))
        produccion[estantes]['productos'][indice]['cantidad'] = int(produccion[estantes]['productos'][indice]['cantidad']) - cantidad
        produccion[estantes]['cantidad_actual'] = int(produccion[estantes]['cantidad_actual']) - cantidad

    producto = {

        'id' : id_prod,
        'cantidad' : cantidad,
        'precio' : precio

    }
    

    orden.append(producto)
    checkarSiMandoSeñal(produccion,tienda,estantes)
    return orden

def getClientes(lista,myConnection ):

    query = """SELECT id_cliente, nombre, apellido, CASE WHEN id_cliente not in (Select id_cliente from afiliado) 
                                                          THEN False ELSE True END afiliado FROM cliente"""
    df = pd.read_sql_query(query, myConnection)
    for index, row in df.iterrows():
        producto = {

        'id' : row["id_cliente"],
        'cantidad' : row["nombre"],
        'precio' : row["apellido"],
        'afiliado': row["afiliado"]
        } 
    
        lista.append(producto)
    print(lista[0])

def getProductos(prodTienda1,prodTienda2,myConnection):
    query = """with aux (id, cheat,value ) as (SELECT  id_producto, MAX(id_costo_producto) ,MAX(fecha) FROM costo_producto group by id_producto order by id_producto)
                SELECT e.id_estante, e.max_capacidad, e.id_sucursal, p.id_producto, p.nombre, i.promedio_inventario, c.precio from estante e
                                INNER JOIN inventario i on e.id_estante= i.id_estante 
                                INNER JOIN producto p on i.id_producto = p.id_producto
                                INNER JOIN costo_producto c on p.id_producto = c.id_producto
                                INNER JOIN aux on c.id_costo_producto= aux.cheat
                order by id_estante asc"""

    df = pd.read_sql_query(query, myConnection)
    prodTienda1 = []
    prodTienda2 = []
    for index, row in df.iterrows():
    
    
    
        if row["id_sucursal"] == '1001':
        
        
            pepe = next((i for i, item in enumerate(prodTienda1) if item["estante"] == row["id_estante"]), None)
            if pepe == None:

                temp = {

                'estante' : row["id_estante"],
                'productos' : [{
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["promedio_inventario"],
                        'restock' : row["promedio_inventario"]
                        }],
                'cantidad_actual' : row["id_estante"],
                'capacidad' : row["id_estante"]
                }
                
                prodTienda1.append(temp)

            else:
                
                temp = {
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["promedio_inventario"],
                        'restock' : row["promedio_inventario"]
                        }
                
                prodTienda1[pepe]['productos'].append(temp)
                
        else:
            
            pepe = next((i for i, item in enumerate(prodTienda2) if item["estante"] == row["id_estante"]), None)
            if pepe == None:

                temp = {

                'estante' : row["id_estante"],
                'productos' : [{
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["promedio_inventario"],
                        'restock' : row["promedio_inventario"]
                        }],
                'cantidad_actual' : row["id_estante"],
                'capacidad' : row["id_estante"]
                }
                
                prodTienda2.append(temp)

            else:
                
                temp = {
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["promedio_inventario"],
                        'restock' : row["promedio_inventario"]
                        }
                
                prodTienda2[pepe]['productos'].append(temp)
        

    print( prodTienda1)
            
    print( '--------------------------------------------------------------')
            
    print( prodTienda2)

def camaraSend(a,myConnection):
    cur = myConnection.cursor()
    cur.execute("INSERT INTO visita (ID_Cliente, fecha, ID_Sucursal) VALUES (%s, %s, %s);",
                (a["id_cliente"],a["fecha"],a["id_sucursal"]))
    myConnection.commit()

if __name__ == "__main__":
    main()