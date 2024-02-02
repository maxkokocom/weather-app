import httpx
import json
import pandas as pd
from datetime import datetime
import time
import sys


def get_weather(latitude=51.5085, longitude=-0.1257, historic=False, start_date='2024-01-01', end_date='2024-02-01'):
    api_url = 'https://api.open-meteo.com/v1/forecast'
    api_params = '&hourly=temperature_2m,rain,showers,visibility'
    url = ''.join([api_url, '?latitude=', str(latitude), '&longitude=', str(longitude), api_params])

    if historic:
        extra_time_param = '&start_date=' + start_date + '&end_date=' + end_date + '&hourly=temperature_2m'
    else:
        extra_time_param = '&past_days=31'

    url = ''.join([url, extra_time_param])

    for attempt_number in range(4):
        try:
            r = httpx.get(url)
            r.raise_for_status()
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
            time.sleep(1)
            if attempt_number == 3:
                print("Cannot connect to open meteo, stopping the program")
                sys.exit(1)
            print("Retrying api request")

    json_dict = json.loads(r.text)
    return json_dict, r.status_code


def aggregate_daily(json_dict):
    df = pd.DataFrame(json_dict['hourly'])
    df['time'] = pd.to_datetime(df['time'])
    daily = df.groupby(df['time'].dt.date).agg({
        'temperature_2m': 'mean',
        'rain': 'sum',
        'showers': 'sum',
        'visibility': 'mean'
    })
    print(daily)

    return daily


def save_parquet(pandas_dataframe, file_path, compression=None):
    pandas_dataframe.to_parquet(path=file_path, compression=compression)


def upload_parquet_somewhere(file_path, endpoint):
    pass


if __name__ == '__main__':
    json_dict = get_weather()[0]
    aggregated_dataframe = aggregate_daily(json_dict)

    now = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    filename = "open-meteo-" + now
    save_parquet(aggregated_dataframe, filename)
    # upload_parquet_somewhere(filename, endpoint)


def lambda_handler(event, context):
    json_dict = get_weather()[0]
    aggregated_dataframe = aggregate_daily(json_dict)

    now = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    filename = "open-meteo-" + now
    save_parquet(aggregated_dataframe, filename)
    # upload_parquet_somewhere(filename, endpoint)
