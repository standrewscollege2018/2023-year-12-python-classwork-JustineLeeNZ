""" manage client info using a list of lists - Justine Lee 13/2/2023 """

# list of clients
client_list = [["Justine Lee", 21, "Poodle"],["John Smith", 45, "Hamster"]]

# skill 1
# display an individual client's details in nicely formatted way
# print client name - 1st client
print(client_list[0][0])

# print client age - 1st client
print(client_list[0][1])

# print client pet - 2nd client
print(client_list[1][2])


# skill 2
# display each client in a numbered list
for i in range(0,len(client_list)):
    print(f"{i+1}. Name: {client_list[i][0]} Age: {client_list[i][1]}")


# skill 3
# delete the first client from the list
print(client_list) # for debugging only
del(client_list[0])
print(client_list) # for debugging only
    

# skill 4
# add a new client to the list - name and age and pet
name = "Mickey Mouse"
age = 100
pet = "Goofy"


client_list.append([name, age, pet])
print(client_list)


# skill 5
# modify the age of the second client in the list



