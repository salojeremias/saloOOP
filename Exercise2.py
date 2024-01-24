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
