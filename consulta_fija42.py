#Script que interactua con una API y nos da un dato curioso sobre el numero 42
#Prueba realizada en clase

#CODIGO MIO
import requests #Importa la libreria http

number = input("Give me the number to consult: ")
url = "http://numbersapi.com/42?json"
trivia_fetch = requests.get(url) #Utilizamos el metodo get para solicitar la url, que es la API de NumbersApi

#Validamos si la url y el metodo son correctos
if trivia_fetch.status_code == 200:
    print(f"Válido: Código {trivia_fetch.status_code}")
    trivia = trivia_fetch.json() #Convierte la trivia a formato json
    print("Información de la trivia", trivia) 
    print("Mensaje de la trivia:", trivia['text']) # acceder al valor de la clave 'text' en el JSON
    print("Número de la trivia:", trivia['number']) # acceder al valor de la clave 'number' en el JSON
else:
    print(f"Error: {trivia_fetch.status_code}")

"""
#CODIGO DE SERCH
# importar requests
import requests
# realizar una petición GET a la API de NumbersApi
trivia_fetch = requests.get("http://numbersapi.com/42?json")
# imprimir el código de estado de la respuesta, se espera 200
print("Código de estado:", trivia_fetch.status_code)

#Convierte la trivia a formato json
trivia = trivia_fetch.json()
print("Informacion de la trivia", trivia)

# acceder al valor de la clave 'text' en el JSON
print("Mensaje de la trivia:", trivia['text'])
# acceder al valor de la clave 'number' en el JSON
print("Número de la trivia:", trivia['number'])
"""
