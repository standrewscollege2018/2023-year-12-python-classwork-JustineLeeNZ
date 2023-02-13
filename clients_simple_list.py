""" manage client info using a simple list - Justine Lee 13/2/2023 """

# list of clients
client_list = ["John Smith","Bob Roberts"]

# print each name, 1 per line - suitable for simple output
for name in client_list:
    print(name)

# add divider to output to separate examples
print(20 * "=")

# print each name as numbered list - using for i in range() suitable when need to track position in list
for i in range(0,len(client_list)):
    print(f"{i+1}. {client_list[i]}")

# add divider to output to separate examples
print(20 * "=")

# add new item (client name) to end of the list
client_list.append("John Doe")

# display the updated list
for name in client_list:
    print(name)

# add divider to output to separate examples
print(20 * "=")

# quick way to display full list WHEN DEBUGGING ONLY
print(client_list)

# add divider to output to separate examples
print(20 * "=")

# delete 2nd name
del(client_list[1])
# check results of deletion
print(client_list)

# add divider to output to separate examples
print(20 * "=")

# change 2nd value in a list
client_list[1] = "Justine Lee"
# check results of modifying an item in the list
print(client_list)

# add divider to output to separate examples
print(20 * "=")

# add to list based on user input
name = input("Enter a client: ")
client_list.append(name)
print(client_list)

