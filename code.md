Para la obtención de datos desarrollamos un programa que interactúa con la interfaz que disponibiliza Twitter.
Específicamente para **Python** se hace uso de la librería **Tweepy** la cual permite hacer consultas a la API utilizando
el método **REST (POST, GET, PUT, DELETE)**.

Para construir este programa primero importamos las librerias necesarias, en este caso **Tweepy** para interactuar con
la API, la librería **json** para el formateo de datos y **MonkeyLearn** para la clasificación de los Tweets.


* Se importan los módulos necesarios
```python
import tweepy
import json
from requests_oauthlib import OAuth1
```
Para poder interactuar con estas interfazes es requerido autenticarse como un usuario valido,
cada API requiere de un **Token** para autenticar al usuario.

* Se agregan las credenciales para la autorización.
```python
#Monkerlearn Developer APP Credentials
ML = MonkeyLearn('44c6c8526ae93145ec2e9809fe307f0d1c07510c')
MODULE_ID = 'cl_u9PRHNzf'
# Twitter Developer APP Credentials
API_KEY = 'xMtlmTsU6CK6Z1nEHva4tMPkS6u6npS6u6npjZ'
API_SECRET = 'jbKHeL2cNGevilZVS6u6np2v5'
ACCESS_TOKEN = '8-W2bIaCbzS6u6npSQCcT5UKcZAEdNHBTgB6iA8S6u6npB'
ACCESS_TOKEN_SECRET = 'RrYXl0344712NcO1gX6LwOFd64cjJP'
```

Estos **Tokens** se pasan como parametros los objetos de autenticación.

```python
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token( ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Authentication
api = tweepy.API(auth)
```

* Se definen los valores del **Header** de la llamada:
    * **query** : Cuenta de interes de busqueda en twitter
    * **language**: Idioma de busqueda
    * **count_tweets**: cantidad de tweets relacionados a buscar

```python
query = "MasterchefUY"
language = "es"
count_tweets = 100
```

* Finalmente realizamos la consulta con todos los parametros, y agregamos los tweets
obtenidos a archivo **output.txt**, con el objetivo de visualizar los datos
```python
with open("output.txt", "w") as text_file:
    for tweet in tweepy.Cursor(api.search,
                               q= query,
                               count=count_tweets,
                               lang= language).items():
        print ("\n\t@"+ tweet.user.screen_name," Tweetió:"+ "\n\t" + tweet.text, file = text_file)
```

