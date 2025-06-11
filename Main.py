import json, unittest, datetime

with open("./data-1.json", "r", encoding="utf8") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r", encoding="utf8") as f:
    jsonData2 = json.load(f)

with open("./data-result.json", "r", encoding="utf8") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    locationParts = jsonObject['location'].split('/')

    result = {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location': {
            'country': locationParts[0],
            'city': locationParts[1],
            'area': locationParts[2],
            'factory': locationParts[3],
            'section': locationParts[4]
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }
