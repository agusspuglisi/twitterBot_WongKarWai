import random

def convertir_thumbnail(url_sin_convertir):
    # Agrego %20 y saco el thumb para que la imagen se vea completa.

    url_modificada = url_sin_convertir.replace(' ', '%20')
    url_final = url_modificada.replace('thumb/', '')

    return url_final

def seleccionar_url():

    dic_urls = {'https://film-grab.com/2014/10/20/chungking-express/' : 'Chungking Express (1994)', 
            'https://film-grab.com/2014/09/25/fallen-angels/' : 'Fallen Angels (1995)',
            'https://film-grab.com/2014/06/22/as-tears-go-by/' : 'As Tears Go By (1995)',
            'https://film-grab.com/2014/04/30/the-grandmaster/' : 'The Grandmaster (2013)',
            'https://film-grab.com/2014/02/19/happy-together/' : 'Happy Together (1997)',
            'https://film-grab.com/2014/02/17/days-of-being-wild/' : 'Days of Being Wild (1990)',
            'https://film-grab.com/2014/02/21/my-blueberry-nights/' : 'My Blueberry Nights (2007)',
            'https://film-grab.com/2014/02/18/ashes-of-time-redux/' : 'Ashes of Time Redux (1994)',
            'https://film-grab.com/2014/02/20/2046/' : '2046 (2000)',
            'https://film-grab.com/2013/03/09/in-the-mood-for-love/' : 'In the Mood for Love (2000)'
            }

    random_url, random_peli = random.choice(list(dic_urls.items()))
    return random_url, random_peli

