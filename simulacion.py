import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import json

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
            'cantidad' : '55'
            }],
    'capacidad' : '66'
    },{
        'departamento' : 'alcohol',
    'productos' : [{
            'id' : '6868',
            'producto' : 'Santa Teresa',
            'cantidad' : '22'
            }],
    'capacidad' : '42'
    }
    ]

prodTienda2 = [{
        
    'departamento' : 'Enlatados',
    'productos' : [{
            'id' : '56645',
            'producto' : 'atun',
            'cantidad' : '55'
            }],
    'cantidad_actual' : '60',
    'capacidad' : '66'
    },{
        'departamento' : 'alcohol',
    'productos' : [{
            'id' : '6868',
            'producto' : 'Santa Teresa',
            'cantidad' : '22'
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
    client = paho.mqtt.client.Client("Publicador", False)
    client.qos = 1
    client.connect(host=host)

    days = 30

    while(days>0):

        #Esto es mientras el Plaza este abierto
        while(horaBase.hour < 22):

            orden : []

            tienda = int(np.random.uniform(0,1))

            if(tienda == 0):
                persona = entrarTienda(1)
                while x in len(prodTienda1):
                    agregarProductos(tienda,prodTienda1,orden,estantes)
            else:
                persona = entrarTienda(2)
                while x in len(prodTienda2):
                    agregarProductos(tienda,prodTienda2,orden,estantes)

            
            
            pagar(persona, orden)

            horaBase = horaBase + datetime.timedelta(hour=1)
            
    horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
    days -= 1

    #Variables de la BDD

def pagar (persona, orden) :

    total = 0
    while x in len(orden):
        total += orden[x]
    
    cuenta =  int(np.random.uniform(0,2))

    if cuenta == 0:
        cuenta = 'Mercantil'
    elif cuenta == 1:
        cuenta = 'Banesco'
    else:
        cuenta = 'Provincial'

    if persona['afiliado'] == True:
        puntos = total * 1.1
        #mandar señal de aumentar puntos

    payload = {
        'id_persona' = persona,
        'tienda' = tienda,
        'banco' = cuenta,

    }

def entrarTienda (tienda):
    if(int(np.random.uniform(0,1)) == 0 and genteConocida!=0):

        scape = False
        x=0
        while scape == False:
            persona = random.choice([a for a in genteConocida if a['afiliado'] ==True])
            if len(persona) > 0:
                return persona
            else:
                 persona = crearPersona()
                 desconocidos += 1
            
        
    else:
        desconocidos += 1
        persona = random.choice([a for a in genteConocida if a['afiliado'] ==False])
        if int(np.random.uniform(0,1)) == 0 and len(persona)>=0:

            pass
        else:
            persona = crearPersona()
    return persona

def crearPersona (tienda):
    cedula = int(np.random.uniform(1000000,30000000)
    gender = random.choice(['M','F'])
    name = random.choice(nameList)
    payload = {
        "cedula": str(cedula),
        "gender": str(gender),
        "afiliado": False
    }
    genteConocida.append(person)
    return person 


def checkarSiMandoSeñal(tienda,estante):

    if tienda = 1:

    
        if prodTienda1[estantes]['capacidad']*.2 <= tienda['estante']['cantidad']
            alerta = {
                'rellenar': 'El estante numero ' + str(estante)+ 'de la tienda' +  str(tienda) + 'tiene que ser rellenado'
            }
            client.publish('plaza/tienda/'+str(tienda),json.dumps(alertaPersonal),qos=1)
            tienda['estante']['cantidad'] = tienda['estante']['maximo']


def agregarProductos (tienda,estante, orden, estantes):
    if tienda == 1:
        prod = random.choice(prodTienda1[estantes]['productos'])
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int (prod['cantidad'])))
        prodTienda1[estantes]['productos']['cantidad'] -= cantidad
        prodTienda1[estantes]['cantidad_actual'] -= cantidad
    else:
        prod = random.choice(prodTienda2[estantes]['productos'])
        id_prod = prod['id']
        cantidad = int(np.random.uniform(0,int (prod['cantidad'])))
        prodTienda2[estantes]['productos']['cantidad'] -= cantidad
        prodTienda2[estantes]['cantidad_actual'] -= cantidad

    producto = {

        'id' = id_prod,
        'cantidad' = cantidad

    }
    

    orden.append(producto)

    checkarSiMandoSeñal(tienda,estante)






