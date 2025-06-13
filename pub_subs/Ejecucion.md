# Guia de uso

## 1. Ejecutar el *broker*
Abrir una terminal (*cmd*)
~~~bash
python broker.py
~~~

Se mostrará como resultado:
~~~bash
~~~
[BROKER] Escuchando en 0.0.0.0:14000...
~~~

## 2.Ejecutando uno o más suscriptores
Abrir una terminal y ejecuta un suscriptor o más

~~~bash
python subscriber.py
~~~
Cuando se te pida, escribe el tema
(*topic*), por ejemplo:
~~~bash
Tema a suscribirse: deportes
~~~
El sistema mantendrá la conexión abierta esperando el mensaje del *broker*

## 3 Ejecutar una o más publicaciones
En otra terminal:
~~~bash
python publisher.py
~~~
Envia un mensaje en este formato:
~~~bash
deportes:¡El América ganó 15-0!
~~~
Todos los suscriptores suscritos a <deportes> recibiran:
~~~bash
[deportes] ¡El Pumas ganó 5-0!
~~~

