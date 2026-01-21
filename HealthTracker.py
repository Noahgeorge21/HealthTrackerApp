import sys 
from datetime import datetime
import time 
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
            print('No Health Records.')
        else:
            for i in self.health_records:
                print(i)
                
    def view_recent_record(self):
        if len(self.health_records) >= 1:
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
        
user_db = {}
current_person = None 

while True:
    print('MAIN MENU')
    print()
    print('Enter 1 to create a user')
    print('Enter 2 to add a health record')
    print('Enter 4 to view all health records')
    print('Enter 5 to view most recent record')
    print('Enter 3 to EXIT')
    print()
    selection = int(input('Enter your selection here: '))
    if selection == 1:
        name = input('enter name: ')
        age = int(input('enter age: '))
        sex = input('enter sex: ')
        height = int(input('enter height (in): '))
        current_person = Person(name, age, sex, height)
        print('USER CREATED')
        print('RETURNING TO MAIN MENU')
        continue
    elif selection == 2:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            continue
        else:
            weight = int(input('enter current weight: '))
            date = str(datetime.now())
            current_person.add_health_record(weight, date)
            print('HEALTH RECORD ADDED')
            print('RETURNING TO MENU')
            continue
    elif selection == 4:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            continue
        else:
            print('weight, BMI, date')
            current_person.view_all_records()
    elif selection == 5:
        if current_person == None:
            print('ERROR -- USER NOT FOUND -- please create a user')
            continue
        else:
            print('weight, BMI, date')
            current_person.view_recent_record()
        
    elif selection == 3:
        sys.exit('YOU HAVE NOW EXITED THE APP')
    
    

