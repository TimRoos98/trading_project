generationForecastLogin = "ZGE5Y2NmZGQtY2I4Mi00YzhiLTg2ZmEtOTQ5MGJiZTYyOGViOjE0ZTJlMTgzLTNkZDgtNDNkOS1hODc3LWRjMGYyMGM5OWI3MA=="
generatedLogin = "N2IyN2VmYmEtMTc5Zi00OTEwLTk4NDgtMzFhMDM0ZjE5MDhjOjRkOGVmNGY4LTc5YmUtNGU4Zi04NjZiLTg5ZjFjNjRlNjE1MA=="

production_type = "SOLAR"
forecast_type = "D-1"
start_date = "2024-06-01T00:00:00%2B02:00"
end_date = "2024-06-03T00:00:00%2B02:00"

forecastFileName = "forecast_data_.csv"
generatedFileName = "generated_data_.csv"


# try:
#     forecast_auth = generate_post_request(generationForecastLogin)
#     print(forecast_auth)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")
#
# forecast_token = forecast_auth.get('access_token')
# print(forecast_token)
# try:
#     forecast_data = extract_values(send_get_request(production_type, forecast_type, start_date, end_date, forecast_token))
#
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")
#
# json_to_csv(forecast_data, generate_filename(forecastFileName, start_date.replace("%2B", "+"), end_date.replace("%2B", "+")))
