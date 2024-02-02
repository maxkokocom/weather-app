from src.main import get_weather, aggregate_daily


def test_open_meteo_connection():
    assert get_weather()[1] == 200


def test_aggregate_func_mean_temp():
    result_of_mean_temp_from_2024_01_01_to_2024_02_01 = [8.345833333333333, 11.583333333333334, 9.754166666666666, 7.7124999999999995, 6.320833333333333, 5.5375000000000005, 3.2458333333333336, 1.6624999999999999, 1.9791666666666667, 2.1999999999999997, 2.6958333333333333, 4.729166666666667, 2.1875, 3.3958333333333335, 0.75, 0.09583333333333334, 0.43333333333333335, -0.6833333333333335, 0.4166666666666667, 3.204166666666667, 9.116666666666665, 10.004166666666666, 9.075000000000001, 10.4, 9.75, 8.808333333333334, 4.4875, 6.375, 10.320833333333333, 8.629166666666666, 7.4750000000000005, 7.041666666666667]

    json_dict = get_weather(latitude=51.5085, longitude=-0.1257, historic=True, start_date='2024-01-01', end_date='2024-02-01')[0]
    aggregated_dataframe = aggregate_daily(json_dict)

    assert result_of_mean_temp_from_2024_01_01_to_2024_02_01 == list(aggregated_dataframe["temperature_2m"].values)


# Similar to above, hardcoded historic date
def test_aggregate_func_sum_rain():
    pass
