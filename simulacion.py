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
genteConocida = [{
    'nombre': 'Neji Hyuga',
    'cedula': '565456',
    'gende': 'M',
    'afiliado': True
}]

prodTienda1 = {
    'frutas': {
        'cantidad': 5,
        'maximo': 44
    },

    'Curda' : {
        'cantidad': 5,
        'maximo': 44
    }
}

prodTienda2 = [{
    'Enlatados': {
        'cantidad': 5,
        'maximo': 44
    }

    'Refrescos' : {
        'cantidad': 5,
        'maximo': 44
    }
}]

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
                    agregarProductos(tienda,prodTienda1,orden)
            else:
                persona = entrarTienda(2)
                while x in len(prodTienda2):
                    agregarProductos(tienda,prodTienda2,orden)

            
            
            pagar(persona, orden)

            horaBase = horaBase + datetime.timedelta(hour=1)
            
    horaBase = datetime.datetime.now().replace(hour=8, minute=0, second=0)
    days -= 1

    #Variables de la BDD

def pagar (persona, orden) :

    total = 0
    while x in len(orden):
        total + = orden[x]
    
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
            persona = random.choice(genteConocida)
            if x > len(persona):
                persona = crearPersona()
                scape = True
                desconocidos += 1
            if persona[0]['afiliado']==True:
                scape = True
                conocidos += 1
        
    else:
        desconocidos += 1
        if int(np.random.uniform(0,1)) == 0 and len(genteNoAfiliada)>=0:
            scape = False
            while scape == False:
                persona = random.choice(genteConocida)
                if persona['afiliado']==False:
                    scape = True
        else:
            persona = crearPersona()
    return persona

def crearPersona (tienda):
    cedula = int(np.random.uniform(1000000,30000000)
    gender = random.choice(['M','F'])
    payload = {
        "cedula": str(cedula),
        "gender": str(gender),
        "afiliado": False
    }
    genteConocida.append(person)
    return person 


def checkarSiMandoSeñal(tienda,estante):
    
    if tienda['estante']['maximo']*.2 <= tienda['estante']['cantidad']
        alerta = {
            'rellenar': 'El estante numero ' + str(estante)+ 'de la tienda' +  str(tienda) + 'tiene que ser rellenado'
        }
        client.publish('plaza/tienda/'+str(tienda),json.dumps(alertaPersonal),qos=1)
        tienda['estante']['cantidad'] = tienda['estante']['maximo']


def agregarProductos (tienda,estante, orden):
    if tienda == 1:
        prod = random.choice(prodTienda1[estante])
        cantidad = int(np.random.uniform(0,prodTienda1[estante][cantidad])
    else:
        prod = random.choice(prodTienda2[estante])
        cantidad = int(np.random.uniform(0,prodTienda2[estante][cantidad])
    

    orden.append(prod,cantidad)

    checkarSiMandoSeñal(tienda,estante)






