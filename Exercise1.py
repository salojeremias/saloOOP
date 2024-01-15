#1
x = "Hello World"
print(x)


#2
import random

# User inserts integers
def get_user_numbers():
    numbers = []
    for _ in range(10):
        number = int(input("Enter a number: "))
        numbers.append(number)
    return numbers

# User inserts strings
def get_user_strings():
    strings = []
    for _ in range(10):
        string = input("Enter a string: ")
        strings.append(string)
    return strings

user_numbers = get_user_numbers()
user_strings = get_user_strings()

print("User Input - Numbers:", user_numbers)
print("User Input - Strings:", user_strings)

random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Randomly Generated Numbers:", random_numbers)


#3
# "sorted" sorts from smallest to largest
print("Randomly Generated Numbers:", sorted(random_numbers))


#4
# User inserts numbers and when "0" is entered it quits
def get_user_input():
    numbers = []
    while True:
        try:
            user_input = int(input("Enter an integer (enter 0 to stop): "))
            numbers.append(user_input)
            if user_input == 0:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return numbers

# Here it counts all negative integers and prints them out if entered
def count_negative_integers(numbers):
    negative_count = sum(1 for num in numbers if num < 0)
    return negative_count

user_numbers = get_user_input()

negative_count = count_negative_integers(user_numbers)
print("Number of negative integers:", negative_count)


#5
# This prints out all even numbers when entered
def count_even_integers(numbers):
    even_count = sum(1 for num in numbers if num != 0 and num % 2 == 0)
    return even_count

even_count = count_even_integers(user_numbers)
print("Number of even integers:", even_count)


#6
def get_user_input():
    numbers = []
    while True:
        try:
            user_input = int(input("Enter an integer (enter 0 to stop): "))
            numbers.append(user_input)
            if user_input == 0:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return numbers

def count_negative_integers(numbers):
    negative_count = sum(1 for num in numbers if num < 0)
    return negative_count

def count_even_integers(numbers):
    even_count = sum(1 for num in numbers if num != 0 and num % 2 == 0)
    return even_count

def sum_positive_divisible_by_three(numbers):
    divisible_by_three_sum = sum(num for num in numbers if num > 0 and num % 3 == 0)
    return divisible_by_three_sum

user_numbers = get_user_input()

negative_count = count_negative_integers(user_numbers)
even_count = count_even_integers(user_numbers)
divisible_by_three_sum = sum_positive_divisible_by_three(user_numbers)

print("Number of negative integers:", negative_count)
print("Number of even integers:", even_count)
print("Sum of positive integers divisible by three:", divisible_by_three_sum)


#7
def calculate_ap(max_value):
    common_difference = 3
    terms = [i for i in range(3, max_value + 1, common_difference)]
    return terms

def count_terms(terms):
    return len(terms)

def calculate_sum(terms):
    return sum(terms)

def calculate_sum_of_squares(terms):
    return sum(num**2 for num in terms)

max_value = int(input("Enter the maximum value of the arithmetic progression: "))

ap_terms = calculate_ap(max_value)

num_of_terms = count_terms(ap_terms)
sum_of_terms = calculate_sum(ap_terms)
sum_of_squares = calculate_sum_of_squares(ap_terms)

print("Number of terms in the arithmetic progression:", num_of_terms)
print("Sum of the terms in the arithmetic progression:", sum_of_terms)
print("Sum of the squares of the terms in the arithmetic progression:", sum_of_squares)


#8
import random

# Here we define the actions
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Here we define the winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    # This makes the game playable again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


#9
import random

def generate_random_number():
    return random.randint(1, 6)

# Here it prints out the random nuber
random_result = generate_random_number()
print("Random number:", random_result)


#10
phone_book = {}

# Here we define how to search a name from the book
def search_contact():
    name = input("name: ")
    if name in phone_book:
        print("number:", phone_book[name])
    else:
        print("no number")

# Here we define how to add names to the book
def add_contact():
    name = input("name: ")
    number = input("number: ")
    phone_book[name] = number
    print("ok!")

# Here we define the actions
def phone_book_app():
    while True:
        print("command (1 search, 2 add, 3 quit):", end=" ")
        command = int(input())
        
        if command == 1:
            search_contact()
        elif command == 2:
            add_contact()
        elif command == 3:
            print("quitting...")
            break
        else:
            print("Invalid command. Please enter 1, 2, or 3.")

phone_book_app()