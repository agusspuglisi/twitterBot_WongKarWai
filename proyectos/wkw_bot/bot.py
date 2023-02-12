import tweepy
import requests
import random
import time
from bs4 import BeautifulSoup
from auxiliares import convertir_thumbnail
from auxiliares import seleccionar_url
from auxiliares import urls_repetidas
import keys

# Cuantas imagenes seguidas quiero que sean distintas

CANT_IMAGENES = 250

# Autenticación en Twitter

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

imagenes_publicadas = urls_repetidas()

while True:

    url, nombre_pelicula = seleccionar_url()

    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, 'html.parser')

    imagenes = soup.find_all('img')

    if imagenes:

        # Twiteo la imagen

        imagen_random = random.choice(imagenes)
        imagen_url = imagen_random['src']
        url_final = convertir_thumbnail(imagen_url)
        
        if url_final not in imagenes_publicadas:
            response = requests.get(url_final)
            if response.status_code == 200:
                api.update_status_with_media(filename = None, file = response.content, status = nombre_pelicula)
                
            with open("urls_file.txt", "a") as file:
                file.write(url_final + "\n")

            imagenes_publicadas.append(url_final)
            
            if len(imagenes_publicadas) == CANT_IMAGENES:
                imagenes_publicadas = []
                 with open("urls_file.txt", 'w') as file:
                    file.truncate()
                    
        else:
            continue

    print("Imagen publicada de: " + nombre_pelicula)

    time.sleep(12500)