import requests

def generate_post_request(auth_token):
    url = "https://digital.iservices.rte-france.com/token/oauth/"
    headers = {
        'Authorization': f'Basic {auth_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response if needed
        data = response.json()
        return data
    else:
        response.raise_for_status()  # Raise an HTTPError for bad responses

