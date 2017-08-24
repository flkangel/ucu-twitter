# ucu-twitter
Creé este repositorio para agregar la documentación del proyecto.

El archivo **restcalls.py** tiene un script que utiliza la API REST de ***Twitter***

* Se importan los módulos necesarios
```python
import sys
import requests
import json
from requests_oauthlib import OAuth1
```

* Se agregan las credenciales para la autorización.
```python
API_KEY = 'xMtlmTsU6CK6Z1nEHva4tMPkS6u6npS6u6npjZ'
API_SECRET = 'jbKHeL2cNGevilZVS6u6np2v5'
ACCESS_TOKEN = '8-W2bIaCbzS6u6npSQCcT5UKcZAEdNHBTgB6iA8S6u6npB'
ACCESS_TOKEN_SECRET = 'RrYXl0344712NcO1gX6LwOFd64cjJP'
```
* Se definen los valores del **Header** de la llamada:
    * **url** : url base de la **API REST** de ***Twitter***
    * **endpoint**: Operación a realizar, en este caso **leer timeline**
    * **screen_name**: Nombre de la cuenta de ***Twiterr*** a leer timeline
    * **count** : Cantidad de **Tweets** que quiero leer
```python
url = 'https://api.twitter.com/1.1/'
endpoint = 'statuses/user_timeline.json'
screen_name ='MasterChef_UY'
count = '3'
```
* La librería **OAuth1** del módulo **requests** armá el encabezado requerido por la **API** de ***Twitter*** para la authorización
```python
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
```
* Se hace la llamada a la **API** utilizando el método **GET** y pasando los parámetros correspondientes, está devuelve un objeto en formato **json** y el resultado es almacenado en la variable **response**.
 ```python
response = requests.get(url+endpoint+'?screen_name='+screen_name+'&count='+count, auth=auth)
```

* Finalmente para verificar que está funcionando correctamente se imprimen los ***Tweets*** y el código de respuesta de la llamada HTTP en caso correcto será **OK: 200**
```python
if response.status_code == 200:
   print ("Authorization Successful")
for tweet in response.json():
 print (json.dumps(tweet['text']))
```

