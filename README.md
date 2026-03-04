# AQI Agent

An agent that calculated the Air Quality Index (AQI) for Indian cities using pollutant data from a dataset (talked about later).

---

## Working

For each row in the dataset, the agent:

1. Calculates a sub-index for each pollutant (PM2.5, PM10, SO2, NOx, NH3, CO, O3) using India's official AQI breakpoint formula
2. Takes the highest sub-index as the final AQI value
3. Assigns a category based on the AQI bucket

| AQI Range | Category |
|---|---|
| 0 – 50 | Good |
| 51 – 100 | Satisfactory |
| 101 – 200 | Moderate |
| 201 – 300 | Poor |
| 301 – 400 | Very Poor |
| 400+ | Severe |

The user may also enter a city as input to retrieve the AQI information of thta specific city.

---

## Dataset

The script expects a CSV file at `../data/city_day.csv` with the following columns:

| Column | Description |
|---|---|
| City | Name of the city |
| Date | Date of the reading |
| PM2.5 | Particulate matter (≤ 2.5 µm) |
| PM10 | Particulate matter (≤ 10 µm) |
| SO2 | Sulphur dioxide |
| NOx | Nitrogen oxides |
| NH3 | Ammonia |
| CO | Carbon monoxide |
| O3 | Ozone |

The dataset used is the [India Air Quality Data](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india) from Kaggle.

---

## How to run

```bash
pip install pandas numpy
python aqi_agent.py
```

---

## Sample output

```
City                 Date        AQI_Calculated  AQI_Category
Ahmedabad            2015-01-01           149.0      Moderate
Aizawl               2020-03-11            54.0  Satisfactory
Amaravati            2017-11-24           138.0      Moderate
Amritsar             2017-02-27            40.0          Good
Bengaluru            2015-01-01            16.0          Good
Delhi                2015-01-01           622.0        Severe
Hyderabad            2015-01-04            30.0          Good
Mumbai               2015-01-01            34.0          Good
```
