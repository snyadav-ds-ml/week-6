import requests
import pandas as pd

class Genius:

    def __init__(self, access_token):
        """ Initialize the Genius class with an access token. """
        self.access_token = access_token

    def get_access_token(self):
        """ Return the access token. """
        return self.access_token

    def get_artist(self, search_term):
        """ Search for an artist by name and return their details. """
        genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        response = requests.get(genius_search_url)
        json_data = response.json()
        return json_data['response']['hits']
    
    def get_artists(self, search_terms):
        """ Search for multiple artists and return their details in a DataFrame. """
        search_results = []
        for term in search_terms:
            details = self.get_artist(term)
            if details:
                id = details[0]['result']['primary_artist']['id']
                search_results.append({
                    'search_term': term,
                    'artist_id': id,
                    'artist_name': details[0]['result']['artist_names'],
                    'followers_count': details[0]['result']['pyongs_count']
                })
            else:
                search_results.append({
                    'search_term': term,
                    'artist_id': None,
                    'artist_name': None,
                    'followers_count': None
                })
        return pd.DataFrame(search_results)
