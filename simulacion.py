import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import json
import random

host = "broker.hivemq.com"
client = paho.mqtt.client.Client("Juancholo", False)
client.qos = 1
client.connect(host=host)

#Arreglos de utilidad

nameList = ['Pedro', 'Lana', 'Albert', 'Yangel','Sasuke', 'Elvis']

genteConocida = [{
    'nombre': 'Neji Hyuga',
    'cedula': '565456',
    'gende': 'M',
    'afiliado': True
}]

prodTienda1 = [{
        
    'departamento' : 'frutas',
    'productos' : [{
            'id' : '5445',
            'producto' : 'pizza',
            'cantidad' : '55',
            'restock' : '60'
            }],
    'capacidad' : '66'
    },{
        'departamento' : 'alcohol',
    'productos' : [{
            'id' : '6868',
            'producto' : 'Santa Teresa',
            'cantidad' : '22',
            'restock' : '30'
            }],
    'capacidad' : '42'
    }
    ]

prodTienda2 = [{
        
    'departamento' : 'Enlatados',
    'productos' : [{
            'id' : '56645',
            'producto' : 'atun',
            'cantidad_actual' : '55',
            'restock' : '55'
            }],
    'cantidad_actual' : '60',
    'capacidad' : '66'
    },{
        'departamento' : 'alcohol',
    'productos' : [{
            'id' : '6868',
            'producto' : 'Santa Teresa',
            'cantidad' : '22',
            'restock' : '30'
            }],
    'capacidad' : '42'
    }
    ]


conocidos= 0
desconocidos =0 
#Arreglos con data de la BDD
idProd = [] #Aca traigo el id, cantidad de productos, precio en cada tienda
prodTienda = []
prodTienda1 = []
prodTienda2 = []

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

    cantHoras = 24
    hora =0
    horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
    days = 30

    nameList = ['Pedro', 'Lana', 'Albert', 'Yangel','Sasuke', 'Elvis']

    genteConocida = [{
        'nombre': 'Neji Hyuga',
        'cedula': '565456',
        'gende': 'M',
        'afiliado': True
    }]

    prodTienda1 = [{
            
        'departamento' : 'frutas',
        'productos' : [{
                'id' : '5445',
                'producto' : 'pizza',
                'precio': '6',
                'cantidad' : '55',
                'restock' : '60'
                }],
        'cantidad_actual' : '55',
        'capacidad' : '66'
        },{
            'departamento' : 'alcohol',
        'productos' : [{
                'id' : '6868',
                'producto' : 'Santa Teresa',
                'precio': '6',
                'cantidad' : '22',
                'restock' : '30'
                }],
        'cantidad_actual' : '22',
        'capacidad' : '42'
        }
        ]

    prodTienda2 = [{
            
        'departamento' : 'Enlatados',
        'productos' : [{
                'id' : '56645',
                'producto' : 'atun',
                'precio': '6',
                'cantidad' : '55',
                'restock' : '55'
                }],
        'cantidad_actual' : '60',
        'capacidad' : '66'
        },{
            'departamento' : 'alcohol',
        'productos' : [{
                'id' : '686558',
                'producto' : 'Santa Teresa',
                'precio': '6',
                'cantidad' : '22',
                'restock' : '30'
                }],
                'cantidad_actual' : '22',
        'capacidad' : '42'
        }
        ]


    conocidos == 0
    desconocidos ==0 
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
                persona = entrarTienda(1)
                print('Entro a la teinda numero 1')
                x=0
                while x < len(prodTienda1):
                    agregarProductos(tienda,prodTienda1,orden,x)
                    x+=1
            else:
                persona = entrarTienda(2)
                print('Entro a la teinda numero 1')
                x=0
                while x < len(prodTienda2):
                    agregarProductos(tienda,prodTienda2,orden,x)
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

def entrarTienda (tienda):
    if(int(np.random.uniform(0,2)) == 0 and genteConocida!=0):

        
       
     
        
        persona = random.choice([a for a in genteConocida if a['afiliado'] ==True])
        if len(persona) > 0:
            print('Se escogera una persona conocida')
            print(persona)
            return persona
        else:
            print('Se creara una persona')
            persona = crearPersona()
            # desconocidos += 1
            
        
    else:
        # desconocidos += 1
        persona = [a for a in genteConocida if a['afiliado'] ==False]
        if int(np.random.uniform(0,1)) == 0 and len(persona)>0:
            persona = random.choice(persona)
            
        else:
            persona = crearPersona()
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


def checkarSiMandoSeñal(produccion,tienda,estante):

    print(estante)
    popo = int(produccion[estante]['capacidad'])*0.2
    if popo >= int(produccion[estante]['cantidad_actual']):
        alerta = {
            'rellenar': 'El estante numero ' + str(estante)+ 'de la tienda' +  str(tienda) + 'tiene que ser rellenado'
        }
        client.publish('plaza/tienda/'+str(tienda),json.dumps(alerta),qos=1)
        produccion[estante]['cantidad_actual'] = produccion[estante]['capacidad']
            
        x=0
        while x < len(produccion[estante]['productos']):
            produccion[estante]['productos'][x]['cantidad'] = produccion[estante]['productos'][x]['restock']
            x += 1
            
    





def agregarProductos (tienda,produccion, orden, estantes):
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
    print(estantes)
    checkarSiMandoSeñal(produccion,tienda,estantes)
    return orden

if __name__ == "__main__":
    main()