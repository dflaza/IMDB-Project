from IMDB_Data import master_dictionary
from IMDB_Data import year_dictionary
from IMDB_Data import actor_dictionary
from IMDB_Data import rating_dictionary
from IMDB_Data import title_list
from IMDB_Data import year_list
from IMDB_Data import actor_list
from IMDB_Data import rating_list
import random

'''Lists'''
film_list = list(master_dictionary.items())
movie_rating_list = []

'''Menu Variables'''
main_menu_flag = "" #flag to return user to main menu when prompted

def menu_flag():
    global main_menu_flag

    if (main_menu_flag == "n"):
        print("\nThanks for using the app. Have a great day!")
        quit()
    
    if (main_menu_flag == "y"):
        main_menu()
        
    else:
        print("\nThis is not a valid input!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()        

def main_menu():
    '''Main menu for user to make their selection'''
    print("\nWelcome to the Oscar Best Picture Film Selector!\n\nPlease choose one of the options below to get started.\n")
    print("__MAIN MENU__\n\n1 - Randomly select a film\n\n2 - Search films by Year\n\n3 - Search films by actor/actress\n\n4 - Search by IMDB rating\n\n5 - Advanced search (filter results by multiple criteria)\n\n6 - Exit")

    menu_choice = int(input("\nPlease confirm your choice: ")) #prompt user to choose selection from the menu
    
    if (menu_choice == 1):
        random_film_1()
        
    if (menu_choice == 2):
        year_film_search_2()
        
    if (menu_choice == 3):
        actor_film_search_3()
        
    if (menu_choice == 4):
        rating_film_search_4()
        
    if (menu_choice == 5):
        advanced_film_search_5()
        
    if (menu_choice == 6):
        print("\nThanks for using the app! Have a great day")
        quit()
        
    if (menu_choice < 1 or menu_choice > 6):
        print("This is not a valid option!")
        main_menu()        
        
def random_film_1():
    '''Selects a random film from the master_dictionary for the user'''
    global menu_choice
    global main_menu_flag
    
    print("\nYour randomly selected film is:\n\n " + str(random.choice(film_list)))  
        
    main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
    menu_flag()
 
def year_film_search_2():
    '''Returns a film/list of films by year/year range chosen by user'''
    global menu_choice
    global main_menu_flag    
    
    year_choice_min = int(input("\nPlease enter the earliest year for films you want to watch: "))
    year_choice_max = int(input("Please enter the latest year for films you want to watch: "))
    
    film_year_dict = {title:year for (title,year) in year_dictionary.items() if year_choice_min <= year <= year_choice_max}
    
    if len(film_year_dict) == 0:
        print("\nSorry, no films matched your search!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()

    else:
        print("\nThese are the following films that were released between " + str(year_choice_min) + " and " + str(year_choice_max) + ":")
        
        for title, year in film_year_dict.items():
            print()
            print("(Film: "+ title + "),  " + "(Year: " + str(master_dictionary[title]["Year"]) + "),  (IMDB Rating: " + str(master_dictionary[title]["Rating"]) + "),   (Actors: " + str(master_dictionary[title]["Actors"]) + ")")
        
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
    
def actor_film_search_3():
    '''Returns a film/list of films by actor chosen by user'''
    global menu_choice
    global main_menu_flag
    global actor_dictionary
    global title_list
        
    actor_choice = input("\nSearch for a film by actor or actress: ")
    
    film_actor_dict = {title:actor for (title,actor) in actor_dictionary.items() if actor_choice in actor}
    
    if len(film_actor_dict) == 0:
        print("\nSorry, no films matched your search!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()

    else:
        print("\nThese are the following films that have " + str(actor_choice) + ":") 
        for title, actor in film_actor_dict.items():
            print()
            print("(Film: "+ title + "),  " + "(Year: " + str(master_dictionary[title]["Year"]) + "),  (IMDB Rating: " + str(master_dictionary[title]["Rating"]) + "),   (Actors: " + str(actor) + ")")
            
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
      
def rating_film_search_4():
    '''Returns a film/range of films based on the rating criteria from a user'''
    global menu_choice
    global main_menu_flag
    
    rating_choice_min = float(input("\nPlease enter the LOWEST IMDB rating for films you want to watch: "))
    rating_choice_max = float(input("Please enter the HIGHEST IMDB rating for films you want to watch: "))
    
    film_rating_dict = {title:rating for (title,rating) in rating_dictionary.items() if rating_choice_min <= rating <= rating_choice_max}
    
    if len(film_rating_dict) == 0:
        print("\nSorry, no films matched your search!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
        
    else:
        print("\nThese are the following films that have an IMDB rating between " + str(rating_choice_min) + " and " + str(rating_choice_max) + ":")
        
        for title, rating in film_rating_dict.items():
            print()
            print("(Film: "+ title + "),  " + "(Year: " + str(master_dictionary[title]["Year"]) + "),  (IMDB Rating: " + str(rating) + "),   (Actors: " + str(master_dictionary[title]["Actors"]) + ")")
            
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
    
def advanced_film_search_5():
    '''Allows user to search for a film using multiple criteria'''
    global menu_choice
    global main_menu_flag
    
    print("\nType in information into the following parameters to narrow your film search: ")
    
    '''Year Parameters'''
    print("\n___Year___")
    
    year_choice_min = int(input("\nPlease enter the earliest year for films you want to watch: "))
    year_choice_max = int(input("Please enter the latest year for films you want to watch: "))
    
    parameter_dict_1 = {title:year for (title,year) in year_dictionary.items() if year_choice_min <= year <= year_choice_max}    
    
    '''Actor Parameters'''
    print("\n___Actor/Actress___")
    
    actor_choice = input("\nPlease Enter an actor/actress: ")
    
    parameter_dict_2 = {title:actor for (title,actor) in actor_dictionary.items() if title in list(parameter_dict_1.keys()) if actor_choice in actor} # filters movie from parameter_dict_1 where "actor_choice" exists
    
    '''Rating Parameters'''
    print("\n___IMDB Rating___")
    
    rating_choice_min = float(input("\nPlease enter the LOWEST IMDB rating for films you want to watch: "))
    rating_choice_max = float(input("Please enter the HIGHEST IMDB rating for films you want to watch: "))
    
    parameter_dict_3 = {title:rating for (title,rating) in rating_dictionary.items() if title in list(parameter_dict_2.keys()) if rating_choice_min <= rating <= rating_choice_max}
    
    if len(parameter_dict_3) == 0:
        print("\nSorry! No films matched your search!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
        
    else:
        '''Summary of filtered films'''
        print("\nThese are the films that match your search: ")

        for title, rating in parameter_dict_3.items():
            print()
            print("(Film: "+ title + "),  " + "(Year: " + str(master_dictionary[title]["Year"]) + "),  (IMDB Rating: " + str(rating) + "),   (Actors: " + str(master_dictionary[title]["Actors"]) + ")")
            
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()
       
'''Running main menu function and exception handling'''
while True:
    try:
        main_menu()
        
    except ValueError:
        print("\nINVALID INPUT!")
        main_menu_flag = str(input("\nWould you like to return to the main menu?(y/n): "))
        menu_flag()        