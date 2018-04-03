def restaurant_ratings(file_name):
    #Defining a function that accepts a file containing restaurants
    #and their respective scores
    log_text = open(file_name)
    #Passing the data file with the above stated comments.
    rating_for_restaurant = {}
    #Creating empty dictionary to hold restaurant and score
    for line in log_text:
    #Iterates over each line in file
        line = line.rstrip()
        #Removes white space at the right side of each line
        name_score = line.split(":")
        #name_score splits restaurant name and score
        rating_for_restaurant[name_score[0]] = name_score[1]
        #The key for the new dictionary is at name_score index 0 and the value is at name_score index 1
    

    to_be_sorted = []

    for restaurants in rating_for_restaurant:
        things_to_sort = str(restaurants + " is rated at " + rating_for_restaurant[restaurants])
        to_be_sorted.append(things_to_sort)

    final_list = sorted(to_be_sorted)
    for items in final_list:
        print items

    #Take the key, value pair and print out
    





    log_text.close()

restaurant_ratings("scores.txt")