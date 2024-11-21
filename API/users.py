# Imports
# Built In
import os
import requests

# Project
from Params import BASE_API_URL

# Define the URL of your API Gateway endpoint
base_user_url: str = f"{BASE_API_URL}/PROD/users"

# Import API Key from OS Environs
api_key: str = os.environ['API_KEY']

# Set up the headers with the API key
headers: dict[str, str] = {
    "x-api-key": api_key,
}

def get_user(user_id: str):
    """
    Invokes a GET Request to get information about the specified user

    :param user_id: The ID of the user, will most likely be an email that exists within the domain of the PR Department of Education
    :type user_id: str


    :return:
    """

    # Prepare URL String
    url: str = f"{base_user_url}/get_user"

    # Prepare QueryStringParameters
    params = {'user_id': user_id}

    # Send the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
        print("Response:", response.json())  # or response.text depending on the content type
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Error:", response.text)


# Testing
if __name__ == "__main__":
    _user_id = 'jgwilson1997@gmail.com'
    result = get_user(_user_id)

    print(result)
