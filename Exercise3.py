#2
class  NumberStats:
    def __init__(self):
        #instead of self.numbers = 0, it should = []
        self.numbers = []
        #here we give attributes to the even and odd calculations for the 4th part
        self.sum_even = 0
        self.sum_odd = 0

    def add_number(self, number: int):
        self.numbers.append(number)
        #4th part continues here:
        if number % 2 == 0:
            self.sum_even += number
        else:
            self.sum_odd += number

#these 3 def's are for the 2nd part, which define the number counting, getting the sum and counting the average.
    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        return sum(self.numbers) / len(self.numbers)
    
#These 2 def's are for the 4th part, which defines the sum of even and odd numbers added.
    def get_sum_even(self):
        return self.sum_even

    def get_sum_odd(self):
        return self.sum_odd

if __name__ == "__main__":
    #Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    #Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    #Part 3 test prints:
    stats = NumberStats()
    stats.add_number(4)
    stats.add_number(2)
    stats.add_number(5)
    stats.add_number(2)
    stats.add_number(-1)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    #Part 4 test prints:
    stats = NumberStats()
    stats.add_number(4)
    stats.add_number(2)
    stats.add_number(5)
    stats.add_number(2)
    stats.add_number(-1)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats.get_sum_even())
    print("Sum of odd numbers:", stats.get_sum_odd())

#3
class LunchCard:
    #Part 1:
    def __init__(self, balance: float):
        self.balance = balance
        
    def __str__(self):
        return f"Balance: {self.balance}"
    
    #Part 2:
    def eat_ordinary(self, amount: float):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True
            

    def eat_luxury(self, amount: float):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True
        

    #Part 3:
    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit cannot be negative:", str(amount))
        self.balance += amount
        
card = LunchCard(50)
print(card)

card.eat_ordinary(2.95)
print(card)

card.eat_luxury(5.90)
print(card)

card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(200)
print(card)

#4
class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points
        
def passed(submissions: list, lowest_passing: int) -> list:
    passed_submissions = [submission for submission in submissions if submission.points >= lowest_passing]
    return passed_submissions

submissions = [
    ExamSubmission("Alice", 85),
    ExamSubmission("Bob", 70),
    ExamSubmission("Charlie", 60),
    ExamSubmission("David", 45)
]
lowest_passing_grade = 60
passed_submissions = passed(submissions, lowest_passing_grade)

for submission in passed_submissions:
    print(submission.examinee, submission.points)


#5
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True
    

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        price = 2.95
        if payment >= price:
            self.funds += price
            self.ordinaries += 1
            return payment - price
        else:
            return payment

    def eat_luxury(self, payment: float):
        price = 5.90
        if payment >= price:
            self.funds += price
            self.luxuries += 1
            return payment - price
        else:
            return payment

    def eat_ordinary_lunchcard(self, card: LunchCard):
        price = 2.95
        if card.balance >= price:
            card.subtract_from_balance(price)
            self.ordinaries += 1
            return True
        else:
            return False


    def eat_luxury_lunchcard(self, card: LunchCard):
        price = 5.90
        if card.balance >= price:
            card.subtract_from_balance(price)
            self.luxuries += 1
            return True
        else:
            return False
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit(amount)
        self.balance -= amount


if __name__ == "__main__":
    #Part1
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    #Part2
    exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)

    #Part 3
    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    #Part4
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)


#6
#Part 1:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}{self.weight}g'
    
#Part 2:
class box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        total = sum(present.weight for present in self.presents)
        return total
    
#code test
book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
box = box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 50)
box.add_present(cd)
print(box.total_weight())


#7
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

#Part 1:
class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        total_height = sum(person.height for person in self.persons)
        print(f'There are {len(self.persons)} persons iin the room, and their total height is {total_height} cm.')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')

#Part 2:
    def shortest(self):
        if not self.persons:
            return None
        shortest_person = min(self.persons, key = lambda x: x.height)
        return shortest_person 

# Part: 3
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
            return shortest_person
        else:
            return None

#code test     
room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.print_contents()


#8
class Recording:
    def __init__(self, length: int):
        self.length = length

    def get_length(self):
        return self.length

    def set_length(self, length: int):
        self.length = length

#code test
the_wall = Recording(43)
print(the_wall.get_length())
the_wall.set_length(44)
print(the_wall.get_length())


#9
class WeatherStation:
    def __init__(self, name: str):
        self.name = name
        self.observations = []

    def add_observations(self, observation: str):
        self.observations.append(observation)

    def latest_observation(self):
        if self.observations:
            return self.observations[-1]
        else:
            return ""
        
    def number_of_observations(self):
        return len(self.observations)
    
    def __str__(self):
        return f'{self.name}, {self.number_of_observations()} observations'

#code test
station = WeatherStation("Houston")
station.add_observations("Rain 10mm")
station.add_observations("Sunny")
print(station.latest_observation())
station.add_observations("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)


#10
class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        self.service_charge()

    def withdraw(self, amount: float):
        self.balance -= amount
        self.service_charge()

    def get_balance(self):
        return self.balance

    def service_charge(self):
        self.balance -= self.balance * 0.01

#code test
account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())