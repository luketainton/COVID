#!/usr/bin/env python3

import requests
import json


def get_api(endpoint):
    url = "https://coronavirus-tracker-api.herokuapp.com"
    data = json.loads(requests.get(f"{url}{endpoint}").content.decode("utf-8"))
    return data


def get_by_status(data, status):
    return data[f"{status}"]["latest"]

def main():
    data = get_api("/all")
    confirmed = get_by_status(data, "confirmed")
    deaths = get_by_status(data, "deaths")
    recovered = get_by_status(data, "recovered")
    print("\nCURRENT COVID-19 STATS:")
    print(f'Confirmed:  {confirmed}')
    print(f'Ongoing:    {confirmed - (recovered + deaths)}')
    print(f'Deaths:     {deaths}')
    print(f'Recovered:  {recovered}\n')


main()
