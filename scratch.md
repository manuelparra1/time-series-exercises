tarships_df = pd.DataFrame()
starships_next_page = 'https://swapi.dev/api/planets/'

while starships_next_page is not None:
starships_response = requests.get(planets_next_page)
starships_data = planets_response.json()
starships_df = pd.concat([planets_df, pd.DataFrame(planets_data['results'])], ignore_index=True)
starships_next_page = planets_data['next']
starships_df.shape
