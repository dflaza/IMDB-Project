from bs4 import BeautifulSoup
import requests
import re

'''Lists used for storage of attributes for each film'''
title_list = []
actor_list = []
year_list = [] 
rating_list = [] #imdb rating

'''Dictionaries used for looking up films against specific attributes '''
master_dictionary = {} #master dictionary that contains Film Title, Year, Actors and Rating
year_dictionary = {} 
actor_dictionary = {} 
rating_dictionary = {}

'''Extracts and parses html code from IMDBs Best Picture list'''
url = "https://m.imdb.com/chart/bestpicture/"

imdb = requests.get(url, verify = False) #ignore SSL certificate verification to get around corporate firewall

imdb_html = imdb.text

soup = BeautifulSoup(imdb_html, 'html.parser')

def extract_film_titles():
    '''Extracts and formats film titles and appends to title_list'''
    global title_list
    
    for title in soup.find_all("h4", class_="best-picture-item-title"): #append movie titles to title_list
        #print()
        #print(title.text)
        title_list.append(title.text)  

    title_list = [re.sub(r"\n\(\d\d\d\d\)\n",'', i) for i in title_list] #strip parantheses, year and escape characters from each element in title_list
    title_list = [title.strip(' ') for title in title_list] #strip whitespaces

    return title_list

def extract_film_actors():
    '''Extracts and formats list of actors/actresses and appends to actor_list'''
    global actor_list
    
    for actor in soup.find_all("p", class_="h5 unbold"): 
        #print()
        #print(actor.text)
        #actor_list.append([(actor.text).split(",")])
        actor_list.append((actor.text).split(","))

    actor_list = [[actors.strip() for actors in actor_groups] for actor_groups in actor_list]
    
    return actor_list

def extract_film_years():
    '''Extracts the year for each film and appends to year_list'''
    global year_list
    
    for year in soup.find_all("span", class_="unbold"):
        #print()
        #print(year.text)
        year_list.append(year.text)  
    
    year_list = [re.sub("\(", '', i) for i in year_list] #strip left parantheses from years
    year_list = [re.sub("\)", '', i) for i in year_list] # strip right parantheses from years
    
    year_list = [int(i) for i in year_list]

    return year_list    

def extract_film_ratings():
    '''Extracts and formats film ratings and appends to rating_list, converts ratings from string to float'''
    global rating_list
    
    for rating in soup.find_all("span", class_="imdb-rating spacing-right-small"): #append movie titles to title_list
        #print()
        #print(rating.text)
        rating_list.append(rating.text)
    
    rating_list = [float(i) for i in rating_list]

    return rating_list

def create_master_dictionary():
    '''Creates a dictionary of dictionaries that contains attributes of each film'''
    global title_list
    global master_dictionary
    num_list = list(range(len(title_list)))

    master_dictionary = {title_list[n]:{"Year": year_list[n], "Actors": actor_list[n],"Rating": rating_list[n]} for n in num_list}
    
    return master_dictionary    

def create_attribute_dictionaries():
    '''Creates the dictionaries for Year:Title, Actor:Title, Rating:Title'''
    global year_dictionary
    global actor_dictionary
    global rating_dictionary
    global actor_list
     
    num_list = list(range(len(title_list)))
    
    year_dictionary = {title_list[n]:year_list[n] for n in num_list}
       
    actor_dictionary = {title_list[n]:actor_list[n] for n in num_list}
    
    rating_dictionary = {title_list[n]:rating_list[n] for n in num_list}
    
    return (year_dictionary, actor_dictionary, rating_dictionary)

'''Running the data extract functions'''
extract_film_ratings()

extract_film_titles()

extract_film_actors()

extract_film_years()

'''Running the functions to create the master film dictionary and attribute dictionaries'''
create_master_dictionary()

create_attribute_dictionaries()