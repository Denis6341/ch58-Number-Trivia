#Programa creado en Python el cual utiliza una API llamada NumbersApi la cual nos arroja 
#datos curiosos sobre cualquier numero. Este script pide al usuario un numero y recupera
#el dato curioso para mostrarlo en pantalla en formato Json

import requests #Importa la libreria http

def trivia_fetch(number):
    url = "http://numbersapi.com/" + number + "?json"
    print(f"La url consultada es: {url}")
    trivia_fetch = requests.get(url)

    if trivia_fetch.status_code == 200:
        print(f"Válido: Código {trivia_fetch.status_code}")
        trivia = trivia_fetch.json() #Convierte la trivia a formato json
    else:
        print(f"Error: {trivia_fetch.status_code}")
    return trivia

number = input("Give me the number to consult: ")
response = trivia_fetch(number)
print(response)
print(type(response))
