stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

# 1
# stops.append("Edinburgh Waverley")
# print(stops)

# 2
# stops.insert(0, "Glasgow Queen St")
# print(stops)

# 3
# stops.insert(3, "Polmont")
# print(stops)

# 4
# print(stops.index("Linlithgow"))

# 5
# stops.remove("Livingston")
# print(stops)

# 6
# stops.pop(1)
# print(stops)

# 7
# print(len(stops))

# 8
# print(sorted(stops))

# 9
# reversed_list = []
# i = len(stops)-1

# while i >= 0:
#     reversed_list.append(stops[i])
#     i -= 1
# print(reversed_list)

# 10
# for stop in stops:
#     print(stop)



