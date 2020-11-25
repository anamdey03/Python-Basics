lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Abhishek", "Rohit", "Sagar", "Prasun", "Avijit", "Sagarika", "Abhishek"]
friends.insert(1, "Anamitra")  # Add the element in the index mentioned
friends.remove("Avijit")  # Remove the element from the list
friends.append("Amik")  # Appends an element at the end of the list
friends.extend(lucky_numbers)  # Add two lists together
friends.pop()  # Removes the last element of the list
print(friends)
print(friends.index("Prasun"))  # Find the index of the element in the list
print(friends.count("Abhishek"))  # Counts the number of times the element is present in the list
lucky_numbers.sort()  # Sort the list in the ascending order
lucky_numbers.reverse()  # Reverse the list
print(lucky_numbers)

friends2 = friends.copy()  # Copy the content of a list into another
print(friends2)
friends.clear()  # Clear the content of the whole lists
