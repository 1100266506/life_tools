def add_restaurant(filename, restaurant_name, cuisine, price):
    inputfile = open(filename, "a")
    restaurant = [restaurant_name, cuisine, price]
    print(restaurant, file = inputfile)
    inputfile.close()
def check_list(filename):
    inputfile = open(filename, "r")
    total_restaurant_list = inputfile.readlines()
    for line in total_restaurant_list:
        new_line = line.strip()
        print(new_line)
        
#start of program
print("Welcome to the Restaurant Decider!")
option = input("Do you want to find a restaurant (press 1) or update the restaurant list (press 2)")
#if the person wants a restaurant based on input criteria...
if option == "1":
    inputfile = open("restaurant_list.txt","r")
    total_data = inputfile.readlines()
    total_list = []
    #the loop takes the restaurant file database and generates a list that contains [restaurant name, cuisine, price]
    for item in total_data:
        mini_list = []
        if item == "\n":
            continue
        else:
            clean_item = item.strip()
            clean = clean_item.strip("[")
            super_clean = clean.strip("]")
            other = super_clean.strip("""'""")
            other_list = other.split("', '")
            total_list.append(other_list)
#generates list of cuisines avaialble in database
    cuisine_list = []
    for restaurant in total_list:
        if restaurant[1] in cuisine_list:
            continue
        else:
            cuisine_list.append(restaurant[1])
    #takes user input about restaurant that they want
    print("You can eat at these restaurants:", cuisine_list)
    cuisine_choice = input("What cuisine do you want to eat: ")
    price_choice = input("Do you want to eat somewhere 'cheap' or 'expensive': ")
    my_restaurant_list = []
    print("You want to eat at a place that is: ", cuisine_choice, "and", price_choice)
    #sifts through database to find the restaurant with appropriate criteria
    for restaurant in total_list:
        if restaurant[1] == cuisine_choice:
            if restaurant[2] == price_choice:
                my_restaurant_list.append(restaurant[0])
    if len(my_restaurant_list)==0:
        print("Sorry, there are no restaurants in the database that fit your criteria")
    else:
        print("How about you eat at these restaurants: ")
        print(my_restaurant_list)
        
if option == "2":
    name= input("What restaurant do you want to add: ")
    cuisine_type = input("What is the cuisine of this restaurant: ")
    price_type = input("Is this expensive or cheap: ")
    add_restaurant("restaurant_list.txt", name, cuisine_type, price_type)
    check_list("restaurant_list.txt")

