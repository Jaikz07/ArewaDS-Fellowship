# Day 2: 30 Days of python programming

# variables
first_name = "Jayson"
last_name = "Solomon"
full_name = "Jayson Solomon"
country = "Nigeria"
city = "Kano"
age = 29
year = 2025
is_married = "No"
is_true = "No"
is_light_on = "yes"
person, animal, place, thing = "John", "Lion", "Nerbreska", "plate"

# print functions
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(is_married,"\n",is_true,"\n",is_light_on)
print(person, animal, place, thing)

print(type(first_name))
print(type(year))
print(type(is_light_on))

print(len(first_name))

#Comparism function definition
def compare_lengths(var1, var2):
    if len(var1) > len(var2):
        return "var1 is longer than var2"
    elif len(var1) < len(var2):
        return "var2 is longer than var1"
    else:
        return "var1 and var2 are of the same length"

string1 = first_name
string2 = last_name

print(compare_lengths(string1, string2))



# Basic arithmetics
num_one = 5
num_two = 4

Total = num_one + num_two
Difference = num_one - num_two
Product = num_one * num_two
Division = num_one / num_two
Remainder = num_one % num_two
Exponent = num_one ** num_two
Floor_division = num_one // num_two

#Mathematical operations
import math

# Given radius
radius = 30

# Calculating area
area_of_circle = math.pi * radius ** 2

# Calculating circumference
circum_of_circle = 2 * math.pi * radius

# Printing the results
print(f"Area of the circle:{round(area_of_circle, 2)}square meters")
print(f"Circumference of the circle:{round(circum_of_circle,2)} meters")

# Taking radius as input from the user
user_radius = float(input("Enter the radius of the circle in meters: "))

# Calculating area with user-provided radius
user_area_of_circle = math.pi * user_radius ** 2

# Printing the result rounded to two decimal places
print(f"Area of the circle with radius {user_radius}: {round(user_area_of_circle, 2)} square meters")


# Prompt the user for their first name and store it in the variable first_name
first_name = input("first name: ")

# Prompt the user for their last name and store it in the variable last_name
last_name = input("last name: ")

# Prompt the user for their country and store it in the variable country
country = input("country: ")

# Prompt the user for their age and store it in the variable age
# Convert the input to an integer since age is a numerical value
age = int(input("Enter your age: "))

# Print the collected information to verify
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

help('keywords')