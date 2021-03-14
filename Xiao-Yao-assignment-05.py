# Part A
# Creat a list with 5-7 strings and store them in a variable called myList
# This is a list of my favorite soft-drinks
import random as r

myList = ["Ginger Ale", "Soda Water", "Pink Lemonade", "Sierra Mist", "Diet Coke", "Sprite"]

# Creat a string to store the name of my collection in singular form
myListNameSingular = "my favorite soft-drink"
# In plural form
myListNamePlural = "my favorite soft-drinks"

# Print the output for part A
print("Part A")
print("------")
print(f"My collection contains {myListNamePlural}")

# Part B
# Print a blank line to separate from part A
print("")

# Store the item count of the list in a variable
numItems = len(myList)

# Print the output for part B
print("Part B")
print("------")
print(f"My collection contains {numItems} {myListNameSingular} items.")

# Part C
# Print a blank line to separate from part B
print("")

print("Part C")
print("------")
for drink in myList:
    print(drink)

# Part D
# Print a blank line to separate from part C
print("")

print("Part D")
print("------")
# Use a while loop to iterate over the list
i = 0
while i < numItems:
    print(f"\t{i + 1}. {myList[i]}")
    i += 1

# Part E
# Print a blank line to separate from part D
print("")

# Store two items to be removed from the list into two variables
firstItemToBeRemoved = "Diet Coke"
secondItemToBeRemoved = "Pink Lemonade"

# Use the list remove method to remove two items above
myList.remove(firstItemToBeRemoved)
myList.remove(secondItemToBeRemoved)

print("Part E")
print("------")
print(f"The first {myListNameSingular} removed was '{firstItemToBeRemoved}'.")
print(f"The second {myListNameSingular} removed was '{secondItemToBeRemoved}'.")

# Store a new item for the collection
itemToBeInserted = "Fanta"

# Use the insert method to insert the new item into the second position
myList.insert(1, itemToBeInserted)
print(f"The {myListNameSingular} inserted was '{itemToBeInserted}'.")

# Use len to count total item numbers and overwrite the numItems
numItems = len(myList)

# Use pop to remove the last item and store it in itemPopped
itemPopped = myList.pop()
print(f"The {myListNameSingular} popped off was '{itemPopped}'.")
print("")

# Copy the same loop code from Part C
for drink in myList:
    print(drink)

# Part F
# Print a blank line to separate from part E
print("")
# Creat an empty list called lottoNumbers
lottoNumbers = []

# Create a for loop with a range of 5 times
for time in range(5):
    # Each time randomly generates an interger from 1 to 70 using randint
    # Store this value in lottoNumber
    # Using the append method to add lottoNumber to lottoNumbers
    lottoNumber = r.randint(1, 70)
    lottoNumbers.append(lottoNumber)

# Generate a random integer from 1 to 25 using randrange and store in megaBallNumber
megaBallNumber = r.randrange(1, 25)

# Create an empty string called lottoOutput
lottoOutput = ""

# A counter for the loop
f_counter = 0

# An infinite while loop to iterate over the lottoNumbers
while (True):
    # Access the current lotto number in lottoNumbers using the counter variable and store it in lottoNumber
    # Add the current lottoNumber to lottoOutput and add a space
    # increment the counter variable
    # Use a condition to check the number of iterations and break when exceed the number of items in lottoNumbers
    lottoNumber = lottoNumbers[f_counter]
    lottoOutput = lottoOutput + str(lottoNumber) + " "
    f_counter += 1
    if f_counter == len(lottoNumbers):
        break

# Add the Mega ball to lottoOutput
lottoOutput = lottoOutput + "Mega Ball: " + str(megaBallNumber)

# Print the output
print("Part F")
print("------")
print("My Python Lottery Ticket:")
print(lottoOutput)

# Part G
# Print a blank line to separate from part F
print("")

# Generate a random integer from 1 to 10 using randint and store in numTickets
numTickets = r.randint(1, 10)

# Print the output
print("Part G")
print("------")
print(f"My {numTickets} Python Lottery Tickets:")
print("")
# Same algorithm with 5,6


# Use a for loop to iterate the same number of times in numTickets
for i in range(numTickets):
    lottoNumbers = []
    # Create a for loop with a range of 5 times
    for time in range(5):
        # Each time randomly generates an integer from 1 to 70 using randint
        # Store this value in lottoNumber
        # Using the append method to add lottoNumber to lottoNumbers
        lottoNumber = r.randint(1, 70)
        lottoNumbers.append(lottoNumber)

    # Generate a random integer from 1 to 25 using randrange and store in megaBallNumber
    megaBallNumber = r.randrange(1, 25)

    lottoOutput = ""
    # A counter for the loop
    f_counter = 0

    # An infinite while loop to iterate over the lottoNumbers
    while (True):
        # Access the current lotto number in lottoNumbers using the counter variable and store it in lottoNumber
        # Add the current lottoNumber to lottoOutput and add a space
        # increment the counter variable
        # Use a condition to check the number of iterations and break when exceed the number of items in lottoNumbers
        # Use if statement to judge whether to add a 0
        lottoNumber = lottoNumbers[f_counter]
        if lottoNumber < 10:
            lottoOutput = lottoOutput + "0" + str(lottoNumber) + " "
        else:
            lottoOutput = lottoOutput + str(lottoNumber) + " "

        f_counter += 1
        if f_counter == len(lottoNumbers):
            break

    # Add the Mega ball to lottoOutput and use if statement to judge whether to add a 0
    if megaBallNumber < 10:
        lottoOutput = lottoOutput + "Mega Ball: " + "0" + str(megaBallNumber)
    else:
        lottoOutput = lottoOutput + "Mega Ball: " + str(megaBallNumber)
    print(lottoOutput)
