import pandas as pd
import os
import requests

# url_stationen = "https://www.dwd.de/DE/leistungen/klimadatendeutschland/statliste/statlex_html.html?view=nasPublication&nn=16102"
# -> URL ist zu lang, daher wird stattdessen eine lokale Datei verwendet

# Stations-ID ermitteln

path_csv = os.path.join("data", "weather", "stationOverview.csv")
stationOverviews = pd.read_csv(path_csv, sep=';', usecols=[
                               "Stations_id", "Stationsname"], dtype=str)
city = "Mannheim"
myStationID = stationOverviews[stationOverviews["Stationsname"]
                               == city]["Stations_id"].item()

# Request bauen
url = "https://api.brightsky.dev/weather"
headers = {'Content-Type': 'application/json'}
# params = {'dwd_station_id': myStationID, 'date': '2019-03-08'}
params = {'dwd_station_id': myStationID,
          'date': '2022-12-15', 'last_date': '2022-12-20'}

response = requests.get(url=url, headers=headers, params=params)


if response.status_code == 200:
    json_s = response.json()
    json_s = f"{json_s}"

    path_txt = os.path.join("data", "weather", "response.txt")
    file1 = open(path_txt, "w")
    file1.write(json_s)
    file1.close()
else:
    print("Status-Code <> 200")
