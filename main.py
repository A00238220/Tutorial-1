import random

#tutorial 1

#######
#Q1
#########
#creating a list
lagos = ['cars', 'keke', 'bike']

#printing items in the list using index positions
print(f"Lagos is usually busy in the morning due to the amount of {lagos[0]}")
print(f"Lagos is usually busy in the afternoon due to the amount of {lagos[1]}")
print(f"Lagos is usually busy in the evening due to the amount of {lagos[2]}")

print()

#######
#Q2
########
#step 1
people = ['ben', 'chioma', 'eve', 'charity', 'abayomi']

print(f"{people[0].title()}, you have been selected to go on the mission")
print(f"{people[1].title()}, you have been selected to go on the mission")
print(f"{people[2].title()}, you have been selected to go on the mission")
print(f"{people[3].title()}, you have been selected to go on the mission")
print(f"{people[4].title()}, you have been selected to go on the mission")
print(f"The number of people selected to go on the mission is {len(people)}")

print()
#step 2
# #removing an item from the list using pop method
# people.remove('ben')
# print(people)

# #removing an item from the list using pop method
# people.pop(1)
# print(people)

# #removing an item from the list using del method
# del people[2]
# print(people)

# #empty the list
# people.clear()
# print(people)

#deleting chioma from the list 
print(f"{people[1].title()}, you have been dropped from the list due to your illness")
del people[1]
print(people)

#replacing chioma with david
people.append('david')
print(people)

print()
#printing a message to new members of the list
print(f"{people[0].title()}, you have been selected to go on the mission")
print(f"{people[1].title()}, you have been selected to go on the mission")
print(f"{people[2].title()}, you have been selected to go on the mission")
print(f"{people[3].title()}, you have been selected to go on the mission")
print(f"{people[4].title()}, you have been selected to go on the mission")
print(f"The number of people selected to go on the mission is {len(people)}")

print()
#step 3
#adding 3 celebrities to the list using the insert function
celebrities = 'john', 'philip', 'beyonce'

#adding john to the begining of the list
people.insert(0, 'john')
print(people)

#adding philip to the middle of the list
people.insert(3, 'philip')
print(people)

#adding beonce to the end of the list
people.append('beyonce')
print(people)

print()
#printing a message to new members of the list
print(f"{people[0].title()}, you have been selected to go on the mission")
print(f"{people[1].title()}, you have been selected to go on the mission")
print(f"{people[2].title()}, you have been selected to go on the mission")
print(f"{people[3].title()}, you have been selected to go on the mission")
print(f"{people[4].title()}, you have been selected to go on the mission")
print(f"{people[5].title()}, you have been selected to go on the mission")
print(f"{people[6].title()}, you have been selected to go on the mission")
print(f"{people[7].title()}, you have been selected to go on the mission")
print(f"The number of people selected to go on the mission is {len(people)}")

print()
#step 4
for peoples in people:  
  print(f"Dear {peoples.title()}, only two people will be able to go on this mission")

print()
#removing all items (leaving 2 people) on the list using the pop method
print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print(f"{people[0].title()}, you have been dropped from the list")
people.pop(0)
print(people)

print()
#printing a message to remaining people
print(f"{people[0].title()}, you are part of the finalist of people selected to go on the mission")
print(f"{people[1].title()}, you are part of the finalist of people selected to go on the mission")
print(f"The number of people selected to go on the mission is {len(people)}")

print()
#step 5
#deleting everyone on the list using del function
del people[0:2]
print(people)

print(f"The number of people selected to go on the mission is {len(people)}")


##########
#Q3
###########
#creating a list of possible locations for the world cup
choices = ['canada', 'belgium', 'egypt', 'portugal']

#sorting the list
choices_sorted = sorted(choices)

#printing original list and sorted list to compare
print(f"original list: {choices}")
print(f"sorted list: {choices_sorted}")


print()
#using reverse
#sorting the list in reverse
choices_rsorted = sorted(choices, reverse=True)

#printing original list and sorted list in reverse to compare
print(f"original list: {choices}")
print(f"reverse sorted list: {choices_rsorted}")

print()
#printing list using reverse function
choices.reverse()
print(choices)


#printing list using reverse function again
choices.reverse()
print(choices)

print()
#using sort method
choices.sort()
print(choices)

#using sort method (reverse alphabetical order)
choices.sort(reverse=True)
print(choices)

########
#Q4
###########
#creating list of countries, cities, color, cars

countries = ['france', 'canada', 'nigeria', 'ghana']
cities = ['chicago', 'sudbury', 'lagos', 'accra']
color = ['brown', 'yellow', 'green', 'red']
cars = ['honda', 'toyota', 'kia', 'hyundai']
pets = ['dog', 'cat', 'rabbit', 'parrot']

#creating a story using random.choices
story = f"{random.choice(cities).title()} is a city located in {random.choice(countries).title()}, it has a popular favorite color of {random.choice(color)} and a common {random.choice(pets)} pet with most people driving {random.choice(cars)}"

#random.randint(1,5)??????
# print(random.randint(1,5))
print(story)

########
#Q5
###########
print()
#making list of student number
student = ["A",0,0,5,4,3,2,1,2]
  
print(f"{student[0]}{student[1]}{student[2]}{student[3]}{student[4]}{student[5]}{student[6]}{student[7]}{student[8]}")

########
#Q5
###########
print()

#creating list and sublist of menu
meal = ['beakfast', 'lunch', 'dinner']
breakfast = ['coffee', 'egg', 'bread']
lunch = ['rice', 'pizza', 'snack']
dinner = ['bagel', 'sausage', 'pancake']

#creating sentence
sentence = f"our {meal[0]} menu is: {breakfast[0]} and {breakfast[-1]}\nour {meal[1]} menu is: {lunch[0]} and {lunch[-1]}\nour {meal[2]} menu is: {dinner[0]} and {dinner[-1]}"

#printing sentence
print(sentence)