#1
class ListHelper:
    def greatest_frequency(my_list):
        return max(set(my_list), key=my_list.count)
    
    def doubles(my_list):
        unique_items = set(my_list)
        return sum(1 for item in unique_items if my_list.count(item) >= 2)

# Example usage:
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))

#2
class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
    
    def name(self):
        return self._name
    
    def weight(self):
        return self._weight
    
    def __str__(self):
        return f"{self._name} ({self._weight}g)"

book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
print("Name of the book:", book.name())
print("Weight of the book:", book.weight())
print("Book:", book)
print("Phone:", phone)

#3
class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        super().__init__(model, speed)
        self._weight = weight
    
    def __str__(self):
        return f"{self._model}, {self._speed} MHz, {self._weight} kg"

laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)

#4
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
    
    def list_games(self):
        return [game for game in self._games.values() if game.year < 1990]

museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))

for game in museum.list_games():
    print(game.name)

#5
class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self._password = password
    
    def add_ingredient(self, ingredient, amount, password):
        if password != self._password:
            raise ValueError("Wrong password!")
        super().add_ingredient(ingredient, amount)
    
    def print_recipe(self, password):
        if password != self._password:
            raise ValueError("Wrong password!")
        super().print_recipe()

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")
diminuendo.print_recipe("pocushocus")

#6
import random

class Dice:
    def __init__(self, sides=6):
        self._sides = sides
    
    def roll(self):
        return random.randint(1, self._sides)

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dices = [dice1, dice2, dice3]

rolls = [dice.roll() for dice in dices]
print("Rolls:", rolls)
print("Sum:", sum(rolls))

#7
class Player:
    def __init__(self, name, player_id):
        self._name = name
        self._player_id = player_id
        self._dice = Dice()
        self._pet = None
    
    def roll_dice(self):
        return self._dice.roll()
    
    def set_pet(self, mammal):
        self._pet = mammal
    
    def __str__(self):
        return f"Player {self._player_id}: {self._name}, Pet: {self._pet}"

player1 = Player("Alice", 1)
player2 = Player("Bob", 2)

players = {1: player1, 2: player2}

for player_id, player in players.items():
    roll_result = player.roll_dice()
    print(f"{player}: Rolled {roll_result}")

#8
class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
    
    def __str__(self):
        return f"Mammal: {self.name}, Species: {self.species}, Size: {self.size}, Weight: {self.weight}"

mammal1 = Mammal(1, "Dog", "Fido", "Medium", "15 kg")
mammal2 = Mammal(2, "Cat", "Whiskers", "Small", "5 kg")

#9
class PhoneBook:
    def __init__(self):
        self._persons = {}
    
    def add_number(self, name, number):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_number(number)
    
    def add_address(self, name, address):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_address(address)
    
    def get_entry(self, name):
        return self._persons.get(name, "Name not found")
    
    def __str__(self):
        return "\n".join(f"{name}: {person}" for name, person in self._persons.items())

# Example usage:
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
phonebook.add_address("Emily", "Viherlaaksontie 7, Espoo")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))