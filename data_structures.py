# Write a program that accepts user input to create a list of integers.
# Then, compute the sum of all the integers in the list.
sum_int = []
for i in range(1, 7):
    num = input('Feed me numbers... ')
    sum_int.append(int(num))
print(sum(sum_int))

# Create a tuple containing the names of five of your favorite books.
# Then, use a for loop to print each book name on a separate line
fav_books = (
    'To Kill a Mockingbird', 'The Great Gatsby', '1984',
    "The Hitchiker's Guide to the Galaxy",
    'The Girl with the Dragon Tattoo')
for book in fav_books:
    print(book)

# Write a program that uses a dictionary to store information about a person,
# such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary.
# Then, print the dictionary to the console.
user_info = {'name': None, 'age': None, 'fav_color': None, 'fav_language': None}
name = input('What is your name? ')
age = input('What is your age? ')
fav_color = input('What is your favorite color? ')
fav_language = input('What is your favorite language')
user_info['name'] = name
user_info['age'] = age
user_info['fav_color'] = fav_color
user_info['fav_language'] = fav_language

# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
def get_sets():
    user_input = input('Enter your first set: ')
    user_input2 = input('Enter your other set: ')
    user_list = [int(x) for x in user_input.split(' ')]
    for x in user_input2.split(' '):
        user_list.append(int(x))
    return set(user_list)
get_sets()

# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list
# that contains only the words that have an odd number of characters.
words = input('Share with me some few words: ').split(' ')
odd_len = [word for word in words if len(word)%2 != 0]