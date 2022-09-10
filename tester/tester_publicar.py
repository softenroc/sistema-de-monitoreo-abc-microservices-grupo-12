import requests
import threading

def publicar():
    endpoint_to_test =  'publicar'
    url = 'http://127.0.0.1:5000/'+endpoint_to_test
    messages = 10
    count = 0
    condition = True

    while condition == True:
        print(f' envío # ->'+threading.current_thread().name+str(count))
        data = '{    "tipo" : "boton_panico",    "mensaje" : "Alerta # '+threading.current_thread().name+str(count)+'! Activacion de boton de panico",    "cliente" : "'+threading.current_thread().name+str(count)+'"}'
        response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
        print(f'rta envío # -> '+str(response.status_code))
        count = count+1
        if(count>=messages):
            condition = False 


hilo1 = threading.Thread(name = '1',target=publicar)
hilo2 = threading.Thread(name = '2',target=publicar)
hilo1.start()
hilo2.start()