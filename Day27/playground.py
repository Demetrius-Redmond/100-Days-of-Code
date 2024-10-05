def add(*args):
    numbers = list(args)
    results = 0 
    for num in numbers:
        
        results += num
       
    print(results) 

add(5,5,5,5)

def calculate(**kwargs):



class Car:
    def __init__(self, **kwargs):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan" model="GTR")