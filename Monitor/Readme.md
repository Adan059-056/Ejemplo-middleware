# PRÁCTICA: Sistema Distribuido para Monitoreo Ambiental
Autor: Adán Pérez Alvarado  
**Fecha:** 27/06/2025  
**UEA:** Sistemas Distribuidos  
**Profesor:** Dr. Guillermo Monroy Rodríguez

## Objetivo
Comprender las matices que es capaz de ofrecer un sistema distribuido capaz de monitorear variables ambientales (humedad, temperatura, calidad del aire) en distintas zonas utilizando las herramientas que conforman la arquitectura de microservicios.   

## Arquitectura de Microservicios

El sistema está compuesto por los siguientes servicios:

- `sensor_service`: simula sensores y envía datos.
- `collector_service`: recibe y reenvía los datos a los servicios correspondientes.
- `storage_service`: guarda los datos de cada zona.
- `alert_service`: genera alertas por valores extremos.
- `frontend_service` (opcional): interfaz para consultar datos y alertas.
---

## Tecnologías Usadas

- Lenguaje: Python 3.10+
- Framework: Flask
- Comunicación: HTTP REST (`requests`)
- Contenedores: Docker y Docker Compose
- Formato de datos: JSON

---

## Generación de Alertas

Las alertas se generan cuando:

- Temperatura > 35 °C  
- Humedad < 20% 
- Humedad > 80%  
- Calidad del aire > 60

---

## API de Consulta (`storage_service`)

| Método | Ruta                        | Resultado                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/colonia/<nombre>`          | Últimas mediciones de la colonia          |
| GET    | `/promedio/<nombre>`        | Promedios de temperatura, humedad, aire|
| GET    | `/todos` *(opcional)*       | Todas las mediciones almacenadas       |

---