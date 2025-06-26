# 🐍 Python Internship – Day 3

# 🎯 Task: Working with Lists, Split/Join, and Tuples

# Step 1: Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into a list of words
words_list = sentence.split()

# Step 3: Print the list
print("List of words:", words_list)

# Step 4: Join the list back into a sentence using ' - ' as a separator
joined_sentence = ' - '.join(words_list)
print("Joined sentence:", joined_sentence)

# Step 5: Store your first and last name in a tuple
name_tuple = ("Dani", "Ahmed")  # Replace with your actual first and last name

# Step 6: Print each part using indexing
print("First Name:", name_tuple[0])
print("Last Name:", name_tuple[1])
