import requests

from export_csv import flatten_json


def generate_forecast_url(production_type, forecast_type, start_date, end_date):
    base_string = (
        "https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/forecasts?"
        "production_type={}&type={}&start_date={}&end_date={}"
    )
    url = base_string.format(production_type, forecast_type, start_date, end_date)
    return url

def send_forecast_get_request(production_type, forecast_type, start_date, end_date, token):
    url = generate_forecast_url(production_type, forecast_type, start_date, end_date)
    headers = {
        'Authorization': f'Bearer {token}',
        'Host': 'digital.iservices.rte-france.com'
    }
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response if needed
        data = response.json()
        return data
    else:
        response.raise_for_status()  # Raise an HTTPError for bad responses


def extract_values(json_data):
    values_list = []
    for forecast in json_data.get('forecasts', []):
        for value_entry in forecast.get('values', []):
            values_list.append(flatten_json(value_entry))
    return values_list
