# FIWARE-EdgeComputing Demo [<img src="https://img.shields.io/badge/NGSI-LD-d6604d.svg" width="90"  align="left" />](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf)[<img src="https://fiware.github.io/tutorials.IoT-Agent/img/fiware.png" align="left" width="162">](https://www.fiware.org/)<br/>

[![FIWARE IoT Agents](https://nexus.lab.fiware.org/repository/raw/public/badges/chapters/iot-agents.svg)](https://github.com/FIWARE/catalogue/blob/master/iot-agents/README.md)
[![License: MIT](https://img.shields.io/github/license/fiware/tutorials.Iot-Agent.svg)](https://opensource.org/licenses/MIT)
[![Support badge](https://img.shields.io/badge/tag-fiware-orange.svg?logo=stackoverflow)](https://stackoverflow.com/questions/tagged/fiware)
[![JSON LD](https://img.shields.io/badge/JSON--LD-1.1-f06f38.svg)](https://w3c.github.io/json-ld-syntax/)

---
##  FIWARE-EdgeComputing Demois based on Digital Twin of SmartWorld by FIWARE 

FIWARE's Smartworld is a Model of a Smart City using bricks, sensors, electronics and the FIWARE system. 

The Model was created to show the endless possibilities of the FIWARE technology in multiple fields, like digital governance, energy management, city management, mobility and construction.

This demo extanded former Digital Twin of SmartWorld by FIWARE project with Podman-Compose, Kuberntes and other more advanced deplyments.

---


## Start up the context broker

To run the context broker you need to have docker compose version 2 installed.

The commands to control the system are (under the podman-compose folder):

- ```podman-compose up``` : starts the whole system 
- ```podman-compose down``` : stops the whole system

## Adding new data entities to running context broker:

To run this python script to generate some random data for testing:

```shell
python3 battery-simulate.py
```

## Creating/Updating/ data entities from/to running context broker:
```
curl -v -L -X POST 'http://localhost:1026/ngsi-ld/v1/subscriptions/' \
-H 'Content-Type: application/ld+json' \
-H 'NGSILD-Tenant: swbf' \
--data-raw '{
  "description": "Notify me of all battery control changes",
  "type": "Subscription",
  "entities": [{"type": "BatteryControllers"}],
  "watchedAttributes": ["chargingBehaviour","dischargingBehaviour","newTempC","CO2"],
  "notification": {
    "attributes": ["chargingBehaviour","dischargingBehaviour","newTempC","CO2"],
    "format": "normalized",
    "endpoint": {
      "uri": "http://quantumleap:8668/v2/notify",
      "accept": "application/json",
      "receiverInfo": [
        {
          "key": "fiware-service",
          "value": "swbf"
        }
      ]
    }
  },
   "@context": "https://schema.lab.fiware.org/ld/context"
}'
```

```
curl -X GET 'http://localhost:1026/ngsi-ld/v1/subscriptions/' \
  -H 'Link: <http://context/user-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
  -H 'NGSILD-Tenant: swbf'
```

```
curl -v POST 'http://localhost:1026/ngsi-ld/v1/entities' \
-H 'NGSILD-Tenant: swbf' \
-H 'Content-Type: application/json' \
-H 'Link: <https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
-H 'Accept: application/ld+json' \
--data-raw '
  {
    "id": "urn:ngsi-ld:BatteryControllers:Controller0001",
    "type": "BatteryControllers",
    "chargingBehaviour": {"type": "Property","value": 10},
    "dischargingBehaviour": {"type": "Property","value": 10},
    "newTempC": {"type": "Property","value": 10},
    "CO2": {"type": "Property","value": 10}
  }'
  ```

  ```
curl -v GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:BatteryControllers:Controller0001' \
-H 'NGSILD-Tenant: swbf' \
-H 'Content-Type: application/json' \
-H 'Link: <https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
-H 'Accept: application/ld+json'

  ```
5 UPDATE VALUES FROM CB and read back
  ```
curl -v PATCH 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:BatteryControllers:Controller0001/attrs' \
-H 'Content-Type: application/json' \
-H 'NGSILD-Tenant: swbf' \
-H 'Link: <https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
-H 'Accept: application/ld+json' \
--data-raw '
  {
    "chargingBehaviour": {"type": "Property","value": 7},
    "dischargingBehaviour": {"type": "Property","value": 7},
    "newTempC": {"type": "Property","value": 7},
    "CO2": {"type": "Property","value": 7}
  }'

  ```
  ```
curl -v GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:BatteryControllers:Controller0001' \
-H 'NGSILD-Tenant: swbf' \
-H 'Content-Type: application/json' \
-H 'Link: <https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
-H 'Accept: application/ld+json'

  ```
READ FROM QUANTUM LEAP 
  ```
curl -X GET 'http://localhost:8668/v2/entities/urn:ngsi-ld:BatteryControllers:Controller0001/attrs/chargingBehaviour?limit=3' \
  -H 'Accept: application/json' \
  -H 'Fiware-Service: swbf'
  ```
```
curl -X GET 'http://localhost:8668/v2/entities/urn:ngsi-ld:BatteryControllers:Controller0001/attrs/chargingBehaviour?aggrMethod=count&aggrPeriod=minute&lastN=3' \
  -H 'Accept: application/json' \
  -H 'Fiware-Service: swbf'
```
Read from Quantumleap
```
curl -iX POST 'http://localhost:4200/_sql' \
  -H 'Content-Type: application/json' \
  -d '{"stmt":"SHOW SCHEMAS"}'

curl -X POST 'http://localhost:4200/_sql' \
  -H 'Content-Type: application/json' \
  -d '{"stmt":"SHOW TABLES"}'

curl -iX POST 'http://localhost:4200/_sql' \
  -H 'Content-Type: application/json' \
  -d '{"stmt":"SELECT * FROM mtswbf.etbatterycontrollers WHERE entity_id = '\''urn:ngsi-ld:BatteryControllers:Controller0009'\''  ORDER BY time_index DESC LIMIT 3"}'
```
---

## License

[MIT](LICENSE) © 2020 FIWARE Foundation e.V.
