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
