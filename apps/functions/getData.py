import json

import requests as rs
import json as js

fileName = 'userName.json'


def searchMedicine(MedicineName):
    with open(fileName, 'r') as f:
        data = js.load(f)
        print(data.get('refresh'))


searchMedicine('asdf')
