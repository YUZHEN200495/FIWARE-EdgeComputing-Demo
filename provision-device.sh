#!/bin/bash

set -e

## 0 Check no old services available


curl "http://localhost:4041/iot/services" \
     -H 'Fiware-service: swbf' \
     -H 'Fiware-servicepath: /'

STOP DATA TRANSFER!!!


## 1 Create Device-Group
curl -iX POST 'http://localhost:4041/iot/services' \
-H 'fiware-service: swbf' \
-H 'fiware-servicepath: /' \
-H 'Content-Type: application/json' \
--data-raw '{
    "services": [
        {
            "entity_type": "BatteryControllers",
     "service": "swbf",
            "subservice": "/",
            "apikey": "BatteryControllers2024secret",
            "resource": "/iot/json"
        }
    ]
}'



curl -L -X POST 'http://localhost:4041/iot/devices' \
    -H 'fiware-service: swbf' \
    -H 'fiware-servicepath: /' \
    -H 'Content-Type: application/json' \
--data-raw '{
  "devices": [
    {
      "device_id": "Controller0001",
      "entity_name": "urn:ngsi-ld:BatteryControllers:Controller0001",
      "entity_type": "BatteryControllers",
      "timezone": "Europe/Berlin",
      "transport": "MQTT",
      "protocol": "MQTT_JSON",
      "commands": [
        {
          "name": "PushCommand",
          "type": "command"
        }
      ],
      "attributes": [
        {
          "object_id": "chargeBehaviour",
          "name": "chargeBehaviour",
          "type": "Property"
        },
        {
          "object_id": "dischargeBehaviour",
          "name": "dischargeBehaviour",
          "type": "Property"
        },
        {
          "object_id": "newTempC",
          "name": "newTempC",
          "type": "Property",
          "metadata": {
            "unitCode": {
              "type": "Text",
              "value": "CEL"
            }
          }
        },       
       {
          "object_id": "CO2",
          "name": "CO2",
          "type": "Property",
          "metadata": {
            "unitCode": {
              "type": "Text",
              "value": "PPM"
            }
          }
        }
      ],
      "lazy": []
    }
  ]
}'


## 7 Start data transmission from M5Stack microcontroller to HIVEMQ Broker


## 8 Check CB, after some seconds, entity available
curl -v GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:BatteryControllers:Controller0001' \
     -H 'fiware-service: swbf' \
     -H 'fiware-servicepath: /' \
     -H 'Link: <http://context/user-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
     -H 'Accept: application/ld+json' 
