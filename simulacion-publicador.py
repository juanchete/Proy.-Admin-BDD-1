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

    prodTienda1,prodTienda2 = getProductos(myConnection)

    print(len(prodTienda1))
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

    capacidadTienda1 = [] #30 personas
    capacidadTienda2 = [] #35 personas
    colaTienda1 = []
    colaTienda2 = []

    meanTemperatura = 28
    stdTemperatura = 2


    print('Comienza el frao')

    while(days>0):

        print('Dia numero ' + str(days))
        
        #Esto es mientras el Plaza este abierto
        print(horaBase)
        print(horaBase.hour)

        cuantosEntraran = int(np.random.uniform(0,len(genteConocida)))
        

        x = 0

        candidataEntrar = []

        while x < cuantosEntraran:

            if int(np.random.uniform(0,4)) < 4:

                entraran = random.choice(genteConocida)
                candidataEntrar.append(entraran)
            else:

                persona = crearPersona()

                candidataEntrar.append(persona)
                
            x += 1
        

        

        for x in candidataEntrar:

            distribuir(x,capacidadTienda1,colaTienda1,capacidadTienda2,colaTienda2)

        while(len(capacidadTienda1)!=0 and len(capacidadTienda2)!=0):

            print(len(capacidadTienda1))
            print(len(capacidadTienda2))
            print(len(colaTienda1))
            print(len(colaTienda2))

            temperatura = np.random.normal(meanTemperatura, stdTemperatura)


            print('Dia numero ' + str(days) + 'Hora numero '  +str(horaBase.hour) )
            

            orden = []

            tienda = int(np.random.uniform(0,2))

            checkarTemperatura(temperatura,tienda,horaBase)

            if(tienda == 1 and len(capacidadTienda1)>0):
                tienda = 1001
                persona = entrarTienda(1001,capacidadTienda1,conocidos,desconocidos,horaBase,myConnection)
                print('Entro a la teinda numero 1')
                x=0
                while x < len(prodTienda1):
                    print('Seleccionando productos')
                    agregarProductos(tienda,prodTienda1,orden,x,horaBase,myConnection)
                    x+=1
                pagar(persona, orden,tienda,myConnection)
                capacidadTienda1.remove(persona)
                print('La persona salio de la tienda')
                if len(colaTienda1)!=0:
                    entraran = random.choice(colaTienda1)
                    colaTienda1.remove(entraran)
                    capacidadTienda1.append(entraran)
                    print('La persona salio de la cola para entrar')

            if(tienda == 0 and len(capacidadTienda2)>0):
                tienda = 1000
                persona = entrarTienda(1000,capacidadTienda2,conocidos,desconocidos,horaBase,myConnection)
                print('Entro a la teinda numero 2')
                x=0
                while x < len(prodTienda2):
                    print('Seleccionando productos')
                    agregarProductos(tienda,prodTienda2,orden,x,horaBase,myConnection)
                    x+=1
                pagar(persona, orden,tienda,myConnection)
                capacidadTienda2.remove(persona)
                print('La persona salio de la tienda')
                if len(colaTienda2)!=0:
                    entraran = random.choice(colaTienda2)
                    colaTienda2.remove(entraran)
                    capacidadTienda2.append(entraran)
                    print('La persona salio de la cola para entrar')
            

            horaBase = horaBase + datetime.timedelta(hours=1)



            time.sleep(0.2)
            
        horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
        horaBase = horaBase + datetime.timedelta(days=1)
        print(horaBase)
        print(horaBase.hour)
        
        days = days - 1
    #Variables de la BDD

def checkarTemperatura(temperatura,tienda,hora):
    if temperatura< 24 or temperatura>31:

        mensaje = temperatura - 28

        temperatura = str(temperatura) + '°C'

        alerta = {
            'rellenar': 'La temperatura esta ' + str(mensaje)+ '°C sobre el deseado, ajustelo en la tienda ' +  str(tienda),
            'temperatura': temperatura,
            'ID_Sucursal ': tienda,
            'fecha': str(hora.date())
        }

        client.publish('plaza/tienda/'+str(tienda)+'/temperatura',json.dumps(alerta),qos=1)
        



def distribuir (persona,capacidadTienda1,colaTienda1,capacidadTienda2,colaTienda2) :


    if(int(np.random.uniform(0,2)) == 1):

        if len(capacidadTienda1) < 30:

            capacidadTienda1.append(persona)
        
        else:

            colaTienda1.append(persona)

    else:

        if len(capacidadTienda2) < 35:

            capacidadTienda2.append(persona)
        
        else:

            colaTienda2.append(persona)






def pagar (persona, orden,tienda,myConnection) :
    
    total = 0
    x=0
    lista = []
    cantidad = []
    if len(orden) > 0:
        while x < len(orden):
            total = total + int(orden[x]['precio'])
            tempLista = str(orden[x]['id'])
            tempCantidad = int(orden[x]['cantidad'])
            lista.append(tempLista)
            cantidad.append(tempCantidad)
            print('Se añadio una cantidad de '+ str(total) + 'se estan comprando el producto '+str(tempLista) + ' por una cantidad de '+str(tempCantidad))
            x+=1

        cuenta =  int(np.random.uniform(0,3)+1)

        if cuenta == 1:
            banco = 'Mercantil'
        elif cuenta == 2:
            banco = 'Banesco'
        else:
            banco = 'Provincial'

        if persona['afiliado'] == True:
            aumentarPuntos(persona,myConnection)

    

        ejecutarPago(lista,cantidad,str(cuenta),str(persona['id']),str(tienda),myConnection) 

        print('Pago satisfactoriamente por la cantidad de '+ str(total))

    else:

        print('No hay punto, no se pudo ejecutar el pago ')
    
    
        #mandar señal de aumentar puntos

    # payload = {
    #     'id_persona' : persona,
    #     'tienda' : tienda,
    #     'banco' : cuenta,

    # }

def entrarTienda (tienda,lista,conocidos,desconocidos,hora,myConnection):

    checkAfiliado = random.choice([a for a in lista if a['afiliado'] ==True])
    checkNoAfiliado = [a for a in lista if a['afiliado'] ==False]


    stop = False

    while stop == False:

        opcion = int(np.random.uniform(0,2))

        if(opcion == 0 and len(checkAfiliado)>0):

            
        
        
            
            persona = random.choice([a for a in lista if a['afiliado'] ==True])
            if len(persona) > 0:
                print('Se escogera una persona conocida')
                conocidos += 1
                print(persona)
                stop = True
                
        elif(opcion == 1 and len(checkNoAfiliado)>0):
            desconocidos += 1
            persona = [a for a in lista if a['afiliado'] ==False]
            if int(np.random.uniform(0,1)) == 0 and len(persona)>0:
                persona = random.choice(persona)
                print('Se escogera una persona desconocida')
                print(persona)
                stop = True

    
    
    
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


def checkarSiMandoSeñal(produccion,tienda,estante,hora,myConnection):

    
    popo = int(produccion[estante]['capacidad'])*0.2
    if popo >= int(produccion[estante]['cantidad_actual']):
        alerta = {
            'rellenar': 'El estante numero ' + str(estante)+ 'de la tienda' +  str(tienda) + 'tiene que ser rellenado',
            'estante': estante,
            'sucursal': tienda,
            'fecha': str(hora.date())
        }

        client.publish('plaza/tienda/'+str(tienda)+'/almacen',json.dumps(alerta),qos=1)
        produccion[estante]['cantidad_actual'] = produccion[estante]['capacidad']
            
        x=0
        while x < len(produccion[estante]['productos']):
            produccion[estante]['productos'][x]['cantidad'] = produccion[estante]['productos'][x]['restock']
            x += 1
        aux = str(produccion[estante]['estante'])
        query= f"""UPDATE INVENTARIO SET cantidad = promedio_inventario where id_estante = '{aux}';"""
        cur = myConnection.cursor()
        cur.execute(query)
        myConnection.commit()
            

def agregarProductos (tienda,produccion, orden, estantes,hora,myConnection):
    checkarSiMandoSeñal(produccion,tienda,estantes,hora,myConnection)
    if tienda == 1:
        prod = random.choice(produccion[estantes]['productos'])
        indice = produccion[estantes]['productos'].index(prod)
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int(prod['cantidad'])))
        aux = int(prod['cantidad']) - cantidad
        if aux >=0: 
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
            
        
    else:
        prod = random.choice(produccion[estantes]['productos'])
        indice = produccion[estantes]['productos'].index(prod)
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int (prod['cantidad'])))
        aux = int(prod['cantidad']) - cantidad
        precio = 0
        if aux >=0:
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
            
    

    

    
    return orden

def getClientes(lista,myConnection ):

    query = """SELECT id_cliente, nombre, apellido, CASE WHEN id_cliente not in (Select id_cliente from afiliado) 
                                                          THEN False ELSE True END afiliado FROM cliente"""
    df = pd.read_sql_query(query, myConnection)
    for index, row in df.iterrows():
        producto = {

        'id' : row["id_cliente"],
        'nombre' : row["nombre"],
        'apellido' : row["apellido"],
        'afiliado': row["afiliado"]
        } 
    
        lista.append(producto)
    

def getProductos(myConnection):

    prodTienda1 = []
    prodTienda2 = []

    query = """with aux (id, cheat,value ) as (SELECT  id_producto, MAX(id_costo_producto) ,MAX(fecha) FROM costo_producto group by id_producto order by id_producto)
                SELECT e.id_estante, e.max_capacidad, e.id_sucursal, p.id_producto, p.nombre, i.promedio_inventario, c.precio, i.cantidad from estante e
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
                        'cantidad' : row["cantidad"],
                        'restock' : row["promedio_inventario"]
                        }],
                'cantidad_actual' : row["cantidad"],
                'capacidad' : row["max_capacidad"]
                }
                
                prodTienda1.append(temp)

            else:
                
                temp = {
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["cantidad"],
                        'restock' : row["promedio_inventario"]
                        }

                momento = prodTienda1[pepe]['cantidad_actual']  + temp['cantidad']
                
                prodTienda1[pepe]['productos'].append(temp)
                prodTienda1[pepe]['cantidad_actual'] : momento
                
        else:
            
            pepe = next((i for i, item in enumerate(prodTienda2) if item["estante"] == row["id_estante"]), None)
            if pepe == None:
                
                temp = {

                'estante' : row["id_estante"],
                'productos' : [{
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["cantidad"],
                        'restock' : row["promedio_inventario"]
                        }],
                'cantidad_actual' : row["cantidad"],
                'capacidad' : row["max_capacidad"]
                }
                
                prodTienda2.append(temp)

            else:
                
                temp = {
                        'id' : row["id_producto"],
                        'producto' : row["nombre"],
                        'precio': row["precio"],
                        'cantidad' : row["cantidad"],
                        'restock' : row["promedio_inventario"]
                        }

                momento = prodTienda2[pepe]['cantidad_actual']  + temp['cantidad']
                
                prodTienda2[pepe]['productos'].append(temp)

                prodTienda2[pepe]['cantidad_actual'] : momento

    print(prodTienda1)
    print(prodTienda2)

    return prodTienda1,prodTienda2

def aumentarPuntos(persona,myConnection):

    aux = str(persona['id'])
    query= f"""UPDATE afiliado SET puntos = puntos*1.1 where id_cliente = '{aux}';"""
    cur = myConnection.cursor()
    cur.execute(query)
    myConnection.commit()


def ejecutarPago(lista, cantidades, banco, cliente, sucursal,myConnection ):
    
    
    query= f"""select realizar_compra(array {lista}::text[],ARRAY{cantidades}::INTEGER[],CAST({banco} AS VARCHAR),CAST({cliente} AS VARCHAR) ,CAST({sucursal} AS VARCHAR))"""
    cur = myConnection.cursor()
    cur.execute(query)
    cur.close()                                                                                                                                                                       
    myConnection.commit()

def camaraSend(a,myConnection):
    cur = myConnection.cursor()
    cur.execute("INSERT INTO visita (ID_Cliente, fecha, ID_Sucursal) VALUES (%s, %s, %s);",
                (a["id_cliente"],a["fecha"],a["id_sucursal"]))
    myConnection.commit()

if __name__ == "__main__":
    main()