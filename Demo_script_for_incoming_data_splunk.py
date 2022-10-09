from queue import Queue

import requests as req
import json

def demo_api_call(requestURL):
    response = req.get(url=requestURL)
    if response.status_code != 200:
        print(response.json())
        exit()

    data = response.json()
    return json.dumps(data)


def incoming_data():
    requestURL = 'https://api.covidtracking.com/v1/states/current.json'
    return demo_api_call(requestURL)

def main():
    work_queue = incoming_data()
    data = json.loads(work_queue)
    print(json.dumps(data))

main()