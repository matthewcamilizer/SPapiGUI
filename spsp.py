import requests,json

# Your Spotify API credentials
client_id=client_id
client_secret=client_secret

# Obtain an access token from Spotify
token_url = 'https://accounts.spotify.com/api/token'
data = {'grant_type': 'client_credentials'}

class InvalidCalling(Exception):
    @classmethod
    def id(cls):
        return "Invalid client id."
    @classmethod
    def secret(cls):
        return "Invalid client secret."

response = requests.post(token_url, data=data, auth=(client_id, client_secret))
r=response.json()

if response.status_code!=200:
    if r['error_description']=='Invalid client secret':
        raise InvalidCalling(InvalidCalling.secret())
    if r['error_description']=='Invalid client':
        raise InvalidCalling(InvalidCalling.id())
    else:
        raise InvalidCalling(r['error_description'])

access_token = r['access_token']


zz=input("search what? ")
# Use the access token to make a search request
search_endpoint = 'https://api.spotify.com/v1/search'
headers = {'Authorization': f'Bearer {access_token}'}
params = {'q': zz, 'type': 'track'}
response = requests.get(search_endpoint, params=params, headers=headers)

if response.status_code == 200:
    search_results = response.json()
    # Process and print the search results as needed
    print(search_results)
else:
    print("Error performing the search.")
