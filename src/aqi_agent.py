import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

def get_AQI_bucket(x):
    if x <= 50:
        return "Good"
    elif x <= 100:
        return "Satisfactory"
    elif x <= 200:
        return "Moderate"
    elif x <= 300:
        return "Poor"
    elif x <= 400:
        return "Very Poor"
    else:
        return "Severe"

def run_agent():
    df = pd.read_csv("../data/city_day.csv")

    pm25 = df["PM2.5"]
    pm10 = df["PM10"]
    so2 = df["SO2"]
    nox = df["NOx"]
    nh3 = df["NH3"]
    co = df["CO"]
    o3 = df["O3"]

    pm25_si = np.select(
        [pm25 <= 30, pm25 <= 60, pm25 <= 90, pm25 <= 120, pm25 <= 250, pm25 > 250],
        [
            pm25 * 50 / 30,
            50 + (pm25 - 30) * 50 / 30,
            100 + (pm25 - 60) * 100 / 30,
            200 + (pm25 - 90) * 100 / 30,
            300 + (pm25 - 120) * 100 / 130,
            400 + (pm25 - 250) * 100 / 130
        ],
        default=np.nan
    )

    pm10_si = np.select(
        [pm10 <= 50, pm10 <= 100, pm10 <= 250, pm10 <= 350, pm10 <= 430, pm10 > 430],
        [
            pm10,
            pm10,
            100 + (pm10 - 100) * 100 / 150,
            200 + (pm10 - 250),
            300 + (pm10 - 350) * 100 / 80,
            400 + (pm10 - 430) * 100 / 80
        ],
        default=np.nan
    )

    so2_si = np.select(
        [so2 <= 40, so2 <= 80, so2 <= 380, so2 <= 800, so2 <= 1600, so2 > 1600],
        [
            so2 * 50 / 40,
            50 + (so2 - 40) * 50 / 40,
            100 + (so2 - 80) * 100 / 300,
            200 + (so2 - 380) * 100 / 420,
            300 + (so2 - 800) * 100 / 800,
            400 + (so2 - 1600) * 100 / 800
        ],
        default=np.nan
    )

    nox_si = np.select(
        [nox <= 40, nox <= 80, nox <= 180, nox <= 280, nox <= 400, nox > 400],
        [
            nox * 50 / 40,
            50 + (nox - 40) * 50 / 40,
            100 + (nox - 80) * 100 / 100,
            200 + (nox - 180) * 100 / 100,
            300 + (nox - 280) * 100 / 120,
            400 + (nox - 400) * 100 / 120
        ],
        default=np.nan
    )

    nh3_si = np.select(
        [nh3 <= 200, nh3 <= 400, nh3 <= 800, nh3 <= 1200, nh3 <= 1800, nh3 > 1800],
        [
            nh3 * 50 / 200,
            50 + (nh3 - 200) * 50 / 200,
            100 + (nh3 - 400) * 100 / 400,
            200 + (nh3 - 800) * 100 / 400,
            300 + (nh3 - 1200) * 100 / 600,
            400 + (nh3 - 1800) * 100 / 600
        ],
        default=np.nan
    )

    co_si = np.select(
        [co <= 1, co <= 2, co <= 10, co <= 17, co <= 34, co > 34],
        [
            co * 50,
            50 + (co - 1) * 50,
            100 + (co - 2) * 100 / 8,
            200 + (co - 10) * 100 / 7,
            300 + (co - 17) * 100 / 17,
            400 + (co - 34) * 100 / 17
        ],
        default=np.nan
    )

    o3_si = np.select(
        [o3 <= 50, o3 <= 100, o3 <= 168, o3 <= 208, o3 <= 748, o3 > 748],
        [
            o3,
            50 + (o3 - 50),
            100 + (o3 - 100) * 100 / 68,
            200 + (o3 - 168) * 100 / 40,
            300 + (o3 - 208) * 100 / 539,
            400 + (o3 - 748) * 100 / 539
        ],
        default=np.nan
    )

    subindices = np.vstack([pm25_si, pm10_si, so2_si, nox_si, nh3_si, co_si, o3_si])
    aqi = np.nanmax(subindices, axis=0)

    df["AQI_Calculated"] = np.round(aqi)
    df["AQI_Category"] = df["AQI_Calculated"].apply(get_AQI_bucket)

    result = df[["City", "Date", "AQI_Calculated", "AQI_Category"]]
    table = result.groupby("City").first().reset_index()

    print(table)

    city_name = input("\nEnter city name: ")

    city_data = table[table["City"].str.lower() == city_name.lower()]

    if city_data.empty:
        print("City not found")
    else:
        print(city_data)

run_agent()
