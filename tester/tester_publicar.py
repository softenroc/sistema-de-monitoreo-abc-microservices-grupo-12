import requests
endpoint_to_test =  'publicar'
url = 'http://127.0.0.1:5000/'+endpoint_to_test
messages = 20
count = 0
condition = True

while condition == True:
    print(f' envío # ->'+str(count))
    data = '{    "tipo" : "boton_panico",    "mensaje" : "Alerta # '+str(count)+'! Activacion de boton de panico",    "cliente" : "'+str(count)+'"}'
    response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
    print(f'rta envío # -> '+str(response.status_code))
    count = count+1
    if(count>=messages):
        condition = False 
