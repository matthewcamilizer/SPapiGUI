import requests

# Your Spotify API credentials
client_id=client_id
client_secret=client_secret

# Obtain an access token from Spotify
token_url = 'https://accounts.spotify.com/api/token'
data = {'grant_type': 'client_credentials'}
response = requests.post(token_url, data=data, auth=(client_id, client_secret))

if response.status_code == 200:
    access_token = response.json()['access_token']
else:
    print("Error obtaining access token.")
    exit()

squery=input("search what? ")
# Use the access token to make a search request
search_endpoint = 'https://api.spotify.com/v1/search'
headers = {'Authorization': f'Bearer {access_token}'}
params = {'q': squery, 'type': 'track'}
response = requests.get(search_endpoint, params=params, headers=headers)

if response.status_code == 200:
    search_results = response.json()
    # Process and print the search results as needed
    print(search_results)
else:
    print("Error performing the search.")
