import sys 
from datetime import datetime
import time 
import keyboard
class Person:
    def __init__(self, name: str, age: int, sex: str, height: int):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.health_records = []
        
    def __str__(self):
        return(f"{self.name} is {self.height}' tall, {self.age} years old, and a {self.sex}")
    
    def add_health_record(self, weight: int, date: str):
        new_record = HealthRecord(weight, self.height, date)
        self.health_records.append(new_record)
        
    def view_all_records(self):
        if len(self.health_records) < 1:
            print('No Health Records on File!')
        else:
            print('WEIGHT--BMI--DATE--TIME')
            for i in self.health_records:
                print(i)
                
    def view_recent_record(self):
        if len(self.health_records) >= 1:
            print('WEIGHT--BMI--DATE--TIME')
            print(self.health_records[-1])
        else:
            print('No Health Records on File!')

class HealthRecord:
    def __init__(self, weight: int, height: int, date: str):
        self.weight = weight
        self.date = date
        self.height = height
        self.BMI = round((self.weight * 703) / (self.height ** 2), 2)
    def __str__(self):
        return f'({self.weight}, {self.BMI}, {self.date})'
        
current_person = None
def view_recent_record():
    while True:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            break
        else:
            current_person.view_recent_record()
            input('PRESS ANY KEY TO RETURN TO MAIN MENU')
            break
        
def view_all_health_records():
    global current_person
    while True:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            break
        else:
            current_person.view_all_records()
            input('PRESS ANY KEY TO RETURN TO MAIN MENU')
            break
        
def add_health_record():
    global current_person
    while True:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            break
        else:
            weight = int(input('enter current weight: '))
            date = str(datetime.now())
            current_person.add_health_record(weight, date)
            print('HEALTH RECORD ADDED')
            print('PRESS 1 TO RETURN TO MAIN MENU')
            print('PRESS 2 TO ADD ANOTHER HEALTH RECORD')
            choice = int(input('Enter: '))
            if choice == 1:
                break
            elif choice == 2:
                continue
            else:
                print('INVALID INPUT')
                break
            
def create_user():
    while True:
        name = input('enter name: ')
        age = int(input('enter age: '))
        sex = input('enter sex: ')
        height = int(input('enter height (in): '))
        print('USER CREATED')
        input('PRESS ANY KEY TO RETURN TO MAIN MENU')
        break
    return Person(name, age, sex, height)

def main_menu():
    global current_person
    while True:
        print('MAIN MENU')
        print('Enter 1 to create a user')
        print('Enter 2 to add a health record')
        print('Enter 4 to view all health records')
        print('Enter 5 to view most recent record')
        print('Enter 3 to EXIT')
        try:
            selection = int(input('Enter your selection here: '))
            
            if selection == 1:
                current_person = create_user()
            elif selection == 2:
                add_health_record()
            elif selection == 3:
                sys.exit('YOU HAVE NOW EXITED THE APP')
            elif selection == 4:
                view_all_health_records()
            elif selection == 5:
                view_recent_record()
            else:
                print('INVALID SELECTION')
        except ValueError:
            print('INVALID SELECTION -- PLEASE TRY AGAIN')

            
            
main_menu()