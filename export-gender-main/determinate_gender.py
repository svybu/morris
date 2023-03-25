import requests
import pandas as pd
from unidecode import unidecode
import json
from progress.bar import IncrementalBar


# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_rows', None)

""" ********** main function for gender determination and export to another file *******************"""

#main function, that choose between csv file and API call


female_cache = []
male_cache = []
male_names, female_names = [], []
male_names_data = './Data/names_male.csv'
female_names_data = './Data/names_female.csv'
female_cache_tofile = './Cache/female_cache.csv'
male_cache_tofile = './Cache/male_cache.csv'


def get_gender(name, path_to_result=None):
    if name[-4:] == '.csv':
        load_data()
        g_export_data = pd.read_csv(name, delimiter=";")
        df = pd.DataFrame(g_export_data)  # create Dataframe from file
        user_names = df['User Name'].tolist()
        #progress bar in console mode
        bar = IncrementalBar('Machine spirit is working', max=len(user_names))
        gender = []
        for name in user_names:
            gender.append(find_gender(name))
            bar.next()
        bar.finish()
        df['gender'] = gender
        df.to_csv(path_to_result, index=False, sep=';')
        # save result in new file with similar structure to original
        write_to_cache()
        print(f"Done! Result file:{path_to_result}")
    else:
        name = str(name).capitalize()
        gender = find_gender(name)
        return json.dumps({'name': name, 'gender': gender})


def find_gender(name):
    global male_cache, female_cache, male_names_data, female_names_data
    URL = 'https://api.genderize.io'  # additional source for determination
    i = 0  # counter for API
    user = unidecode(name)
    parsed_name_1 = user.split(' ')[0].capitalize()  # first word in 'username'
    parsed_name_2 = user.split(' ')[-1].capitalize()
    # last word in 'username' if firstname and lastname swapped places
    if (# cache for faster determination for names are already found
            parsed_name_1 or parsed_name_2) in female_cache:
        gender = 'female'
    elif (  # cache for faster determination for names are already found
            parsed_name_1 or parsed_name_2) in male_cache:
        gender = 'male'
    elif parsed_name_1 in female_names:  # search in offline dataset
        gender = 'female'
        female_cache.append(parsed_name_1)
    elif parsed_name_1 in male_names:  # search in offline dataset
        gender = 'male'
        male_cache.append(parsed_name_1)
    elif parsed_name_2 in female_names:
        gender = 'female'
        female_cache.append(parsed_name_2)
    elif parsed_name_2 in male_names:
        gender = 'male'
        male_cache.append(parsed_name_2)
    elif use_api:
        i += 1
        api_response = requests.get(URL, params={
            'name': parsed_name_1})  # additional search for the names that are missed in offline dataset
        # This API is free for up to 1000 names/day
        if api_response.json()['gender'] == 'male':
            gender = 'male'
            male_cache.append(parsed_name_1)
        elif api_response.json()['gender'] == 'female':
            gender = 'female'
            female_cache.append(parsed_name_1)
        else:
            gender = 'undefined'  # names that cannot be determined , usually look like nicknames or unreal names
            # undefined.append(user)
    else:
        gender = 'undefined'

    return gender


def write_to_cache():
    global female_cache, male_cache, female_cache_tofile, male_cache_tofile
    female_cache_file = pd.DataFrame(columns=['name', 'gender'])
    female_cache_file['name'] = female_cache
    female_cache_file['gender'] = 'F'
    female_cache_file.to_csv(female_cache_tofile, index=False, sep=',')

    male_cache_file = pd.DataFrame(columns=['name', 'gender'])
    male_cache_file['name'] = male_cache
    male_cache_file['gender'] = 'M'
    male_cache_file.to_csv(male_cache_tofile, index=False, sep=',')


""" **********  path to original and result files  *******************"""
name = 'bolivia_comments.csv'

use_api = False  # turn on/off  external API usage

#opening files
def load_data():
    global male_names_data, female_names_data, female_cache_tofile, male_cache_tofile
    global male_names, female_names, female_cache, male_cache
    male_names = pd.read_csv(male_names_data)
    male_names = pd.DataFrame(male_names)
    male_names = male_names['name'].tolist()
    female_names = pd.read_csv(female_names_data)
    female_names = pd.DataFrame(female_names)
    female_names = female_names['name'].tolist()
    try:
        male_cache = pd.read_csv(male_cache_tofile)
        female_cache = pd.read_csv(female_cache_tofile)
        female_cache = pd.DataFrame(female_cache)
        female_cache = female_cache['name'].tolist()
        male_cache = pd.DataFrame(male_cache)
        male_cache = male_cache['name'].tolist()
    except:
        female_cache = []
        male_cache = []


if __name__ == "__main__":
    get_gender(name)
