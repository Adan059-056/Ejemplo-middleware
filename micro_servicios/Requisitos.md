# Instrucciones 

## Requisitos
~~~bash
pip install flask request
~~~

## Ejecución
1. Abrir 3 terminales para ejecutar cada servicio en puertos distintos

~~~bash
python user_service.py
python product_service.py
python order_service.py
~~~

2. Usar ```curl``` o ```Postman```para crear un usuario:
~~~bash
curl -X POST -H "Content-Type: application/json" \
-d '{"name":"Ana"}' http://localhost:5001/users
~~~
3. Crear un pedido:
~~~ bash
curl -X POST -H "Content-Type: application/json" \
-d '{"user_id": "1", "product_id":"2"}' http://localhost:5003/orders
~~~

