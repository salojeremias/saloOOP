#2
import random

class Coin:
    def init(self):
        self.sideup = 'Heads'
    # modified the code here so that it gives the wanted results
    def toss_the_coin(self):
        result = random.randint(0, 3)
        if result == 0:
            self.sideup = 'Heads'
        elif result == 1:
            self.sideup = 'Tails'
        elif result == 2:
            self.sideup = 'Table Upright'
        else:
            self.sideup = random.choice(['Rabbit Hole', 'Wormhole in Space'])

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin... ")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

main()


#3
import time

class AlarmClock:
    def __init__(self, alarm_time, snooze_time=5, alarm_sound='Beep'):
        self.current_time = time.strftime('%H:%M:%S')
        self.alarm_time = alarm_time
        self.alarm_status = False
        self.snooze_time = snooze_time
        self.alarm_sound = alarm_sound

# Set the alarm time
    def set_alarm(self, time):
        
        self.alarm_time = time

# Toggle the alarm status
    def toggle_alarm(self):
        
        self.alarm_status = not self.alarm_status

# Activate snooze for a specified duration
    def snooze_alarm(self):
        
        pass

# Stop the alarm if it is currently ringing
    def stop_alarm(self):

        pass

# Private method to update the current time
    def _update_time(self):
        
        self.current_time = time.strftime('%H:%M:%S')


#4
def factorials(n: int) -> dict:
    # Initialize an empty dictionary to store the results
    factorial_dict = {}

    # Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        # Calculate the factorial of the current number
        factorial_result = 1
        for j in range(1, i + 1):
            factorial_result *= j

        # Store the result in the dictionary
        factorial_dict[i] = factorial_result

    return factorial_dict

# Example usage:
n = 4
result = factorials(n)
print(result)


#5
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    # Calculate average for each contestant
    avg_person1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg_person2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg_person3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    # Find the contestant with the smallest average
    min_average = min(avg_person1, avg_person2, avg_person3)

    if min_average == avg_person1:
        return person1
    elif min_average == avg_person2:
        return person2
    else:
        return person3

# Example usage:
person1 = {"name": "Alice", "result1": 8, "result2": 9, "result3": 7}
person2 = {"name": "Bob", "result1": 6, "result2": 8, "result3": 9}
person3 = {"name": "Charlie", "result1": 7, "result2": 6, "result3": 8}

winner = smallest_average(person1, person2, person3)
print("Winner:", winner["name"])



#6
from datetime import date

def list_years(dates: list) -> list:
    # Extract the years from the date objects and sort them
    years = sorted([d.year for d in dates])
    return years


#7
class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

class Manga:
    def __init__(self, name, writer, genre, year):
        self.name = name
        self.writer = writer
        self.genre = genre
        self.year = year

class Anime:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

class Song:
    def __init__(self, name, artist, genre, year):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year

# Example usage:
dates = [
    date(2000, 1, 1),
    date(1995, 5, 15),
    date(2010, 7, 20),
    date(2005, 3, 10)
]

sorted_years = list_years(dates)
print("Sorted Years:", sorted_years)


#8
class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


#9
class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)

# Example usage:
my_pet = new_pet("Buddy", "Dog", 2015)
print("My Pet:", my_pet.name, my_pet.species, my_pet.year_of_birth)


#10
class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

def movies_of_genre(movies: list, genre: str) -> list:
    return [movie for movie in movies if movie.genre == genre]

# Example usage:
john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)
movies = [john_woo, kungfu, jet_li, Movie("Hero", "Yimou Zhang", "action", 2002)]

print("Movies in the action genre:")
for movie in movies_of_genre(movies, "action"):
    print(f"{movie.director}: {movie.name}")

