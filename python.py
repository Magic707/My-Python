#1______________basic data types(remember annotation)_________________________________
number: int = 20
decimal: float = 2.3
text: str = 'Hello sobhan'
active: bool = True

names: list =['sobi','ebi','meti' ]
coordinates: tuple =(1.3 , 2.5)
unique: set ={1,2,3,4}
data: dict ={'name': "sobi", 'age': 22}

#2___________def instruction for functions________________________________________
from datetime import datetime

def show_date() -> None: 
    print('this is the current date and time:')
    print(datetime.now())

    
show_date()
show_date()

def greet(name: str) -> None:
    print(f'Hello, {name}')

greet('sobi')
greet('lui')    

def add(a: float, b: float) -> float:
    return a+b

print(add(1,5))

#3_______Class uses when we want to use duplicated a lot ___________________________________________
class Horse:
    def __init__(self, color: str, horsepower: int) -> None:
        self.color=color
        self.horsepower=horsepower

horse: Horse = Horse("red", 250)
print(horse.color)        
print(horse.horsepower)  

#4____________________methods:( << is a functionthat is inside a Class >> )________________________
class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand=brand
        self.horsepower=horsepower
    
    def derive(self) -> None:
        print(f'{self.brand} is driving')

    def get_info(self) -> None:
        print(f'{self.brand} with {self.horsepower} horsepower')    




volvo: Car = Car("red", 250)
volvo.derive()
volvo.get_info()

