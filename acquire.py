import pandas as pd
import os

def get_star_wars_api_url(info):
    # Star Wars API Root Directory Setup
    # root url (table of contents)
    root_url = 'https://swapi.dev/api/'

    # saving response to save as .json
    root_response = requests.get(root_url)

    # converting to .json
    root_response_data = root_response.json()
    
    return root_response_data[info]

def get_people(save=True):
    people_df = pd.DataFrame()
    people_next_page = get_star_wars_api_url("people")

    while people_next_page is not None:
        people_response = requests.get(people_next_page)
        people_data = people_response.json()
        people_df = pd.concat([people_df, pd.DataFrame(people_data['results'])], ignore_index=True)
        people_next_page = people_data['next']
    
    if save:
        # save to csv if option selected
        filename = 'people.csv'

        if not os.path.exists(filename):
            people_df.to_csv(filename, index=False)
            print(f"Saving {filename}...")
        else:
            print(f"File {filename} already exists.")
            
    return people_df

def get_planets(save=True):
    planets_df = pd.DataFrame()
    planets_next_page = get_star_wars_api_url("planets")

    while planets_next_page is not None:
        planets_response = requests.get(planets_next_page)
        planets_data = planets_response.json()
        planets_df = pd.concat([planets_df, pd.DataFrame(planets_data['results'])], ignore_index=True)
        planets_next_page = planets_data['next']
       
    if save:
        # save to csv if option selected
        filename = 'planets.csv'

        if not os.path.exists(filename):
            planets_df.to_csv(filename, index=False)
            print(f"Saving {filename}...")
        else:
            print(f"File {filename} already exists.")
    return planets_df

def get_starships(save=True):
    starships_df = pd.DataFrame()
    starships_next_page = get_star_wars_api_url("starships")

    while starships_next_page is not None:
        starships_response = requests.get(starships_next_page)
        starships_data = starships_response.json()
        starships_df = pd.concat([starships_df, pd.DataFrame(starships_data['results'])], ignore_index=True)
        starships_next_page = starships_data['next']
    
    if save:
        # save to csv if option selected
        filename = 'starships.csv'

        if not os.path.exists(filename):
            starships_df.to_csv(filename, index=False)
            print(f"Saving {filename}...")
        else:
            print(f"File {filename} already exists.")

    return starships_df

def get_all_starwars(save=True):
    # 3 temporary dataframes to hold each type of data
    people_df = get_people(save)
    planets_df = get_planets(save)
    starships_df = get_starships(save)
    
    # columns for sorting ability
    people_df["Type"] = "People"
    planets_df["Type"] = "Planet"
    starships_df["Type"] = "Starship"
    
    #concatenate all 3 into one giant DataFrame
    
    return pd.concat([people_df, planets_df, starships_df])

def get_energy():
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    energy_df = pd.read_csv(url)
    
    filename = 'opsd_germany_daily.csv'

    if not os.path.exists(filename):
        energy_df.to_csv(filename, index=False)
        print(f"Saving {filename}...")
    else:
        print(f"File {filename} already exists.")
    return energy_df

def get_store_data():
    filename = 'tsa_item_demand.csv'

    if not os.path.exists(filename):
        sql_db = "tsa_item_demand"
        url = get_db_url(sql_db)
        query = '''
                select * 
                from sales
                left join items using(item_id)
                left join stores using(store_id)
                '''
        df = pd.read_sql(query,url)
        df.to_csv(filename, index=False)
        print(f"Saving {filename}...")
        
        return df
    else:
        print(f"File {filename} already exists. Loading {filename}...")
        
        return pd.read_csv(filename,index_col=False)
