planets_df = pd.DataFrame()
planets_next_page = 'https://swapi.dev/api/planets/'

while planets_next_page is not None:
planets_response = requests.get(planets_next_page)
planets_data = planets_response.json()
planets_df = pd.concat([planets_df, pd.DataFrame(planets_data['results'])], ignore_index=True)
planets_next_page = planets_data['next']
planets_df.shape
