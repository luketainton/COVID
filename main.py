#!/usr/bin/env python3

import requests
import json


def get_api(endpoint):
    url = "https://coronavirus-tracker-api.herokuapp.com"
    res = requests.get(f"{url}{endpoint}")
    if res.status_code == 200:
        dataraw = res.content.decode("utf-8")
        data = json.loads(dataraw)
        return data
    else:
        return 1


def get_by_status(data, status):
    return data["latest"][f"{status}"]

def main():
    data = get_api("/all")
    if data != 1:
        confirmed = get_by_status(data, "confirmed")
        deaths = get_by_status(data, "deaths")
        recovered = get_by_status(data, "recovered")
        print("\nCURRENT COVID-19 STATS:")
        print(f'Confirmed:  {confirmed}')
        print(f'Ongoing:    {confirmed - (recovered + deaths)}')
        print(f'Deaths:     {deaths}')
        print(f'Recovered:  {recovered}\n')
    else:
        print("There was an error getting the latest statistics. Please try again later.")


main()
