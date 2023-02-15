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

#skill 2
# display a simple list of all clients
# NOTE that you only need one index and that specifies which item in the sublist to display
for client in client_list:
    print(f"Name: {client[0]} Age: {client[1]}")


# skill 3
# display each client in a numbered list
# NOTE index+1 so that displayed numbers start at 1 not 0
for index in range(0,len(client_list)):
    print(f"{index+1}. Name: {client_list[index][0]} Age: {client_list[index][1]}")


# skill 4
# delete the first client from the list
print(client_list) # for debugging only
del(client_list[0])
print(client_list) # for debugging only
    

# skill 5
# add a new client to the list - name and age and pet
name = "Mickey Mouse"
age = 100
pet = "Goofy"


client_list.append([name, age, pet])
print(client_list) # for debugging only


# skill 6
# modify the age of the second client in the list to 99
client_list[1][1] = 99
print(client_list) # for debugging only


