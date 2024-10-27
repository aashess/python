# Taking input of Country, No. Visits, Cities

country = input("Enter the Country: ")
visits = int(input("No. of Visits: "))
cities = eval(input("Name of Cities: "))

# Making Dictionaries 
travel_log=[]

# Making Function 
def add_new_dic(country1,visits1,cities1):
    new_dic = {}
    new_dic["country"]= country1
    new_dic["visits"]= visits1
    new_dic["cities"]= cities1
    travel_log.append(new_dic)

# Main Program + Calling Function
add_new_dic(country,visits,cities)

# print of output
print(f"You have been to {travel_log[0]['country']}. {travel_log[0]['visits']} times.")

print(f"My Favourite city was {travel_log[0] ['cities']}")