import pytz
from pathlib import Path
import random
import os
def cookingWithEchols(meals, sides, numberOfDinners, cook):
  mealsForThePeriod = []
  cookOfTheWeek = random.choice(list(cook))
  print("here\'s who's cooking " + cookOfTheWeek)
  while len(mealsForThePeriod) < numberOfDinners:
    mealChoice = random.choice(list(meals))
    sideChoice = random.choice(list(sides))
    food = mealChoice + " & " + sideChoice
    meal= food.title()
    def doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides):
      niceChoice = input("If you want to replace the last thing type yes or y\n").lower()
      if niceChoice == 'yes' or niceChoice == 'y':
        print("got it")
        lastChoice = mealsForThePeriod.pop()
        print(mealsForThePeriod)
        replacement = input("What do you want to replace? \nType A for the first dish or type B for the side dish\n").lower()
        if replacement == 'a':
          print("I chose " + lastChoice)
          print("let's try something else")
          food = random.choice(list(meals)) + " & " + sideChoice
          meal= food.title()
          mealsForThePeriod.append(meal)
          print(*mealsForThePeriod, sep = "\n")
          doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides)
        else: 
          print("I chose " + lastChoice)
          print("let's try something else")
          food = mealChoice + " & " + random.choice(list(sides))
          meal= food.title()
          mealsForThePeriod.append(meal)
          print(*mealsForThePeriod, sep = "\n")
          doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides)
      else:
        print("nice, go me here's what we got")
        print(mealsForThePeriod, sep = "\n")
        print("adding more")
        food = random.choice(list(meals)) + " & " + random.choice(list(sides))
        meal= food.title()
        mealsForThePeriod.append(meal)
        print(*mealsForThePeriod, sep = "\n")
        doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides)
    mealsForThePeriod.append(meal)
    print(*mealsForThePeriod, sep = "\n")
    shoppingList = doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides)
  print("That's your Shopping List")
  print(*mealsForThePeriod, sep = "\n")
  with open('shopping_list.txt', 'w') as doc:
    for item in mealsForThePeriod:
      doc.write(item+ '\n')
cookingWithEchols(['taquitos','chicken nuggets','kievs','soups','potstickers','pork buns' 'chicken','roasted veggies','stir fry','tacos','tofu','hamburgers','hot dogs','sloppy joe','pulled pork','salmon','bacon','shredded beef', 'pot roast', 'corned beef hash', 'katsu','stews','hamburg steak', 'burritos','empanadas','egg','onigiri','buns','loco moco', 'meatballs','meatloaf','ravioli'], ['white rice','salad','italian pasta','soups','asian pasta','egg rolls','veggies', 'quinoa salad','fried rice', 'yellow rice','fries', 'asparagus','brussel sprouts', 'waffles','potatoes', 'mashed potatoes', 'garlic bread'], 8, ["Jamin","Elaine"])

        # goal to rewrite this as classes.

#cal = Calendar()
#cal.add('attendee', 'MAILTO:abc@example.com')
#cal.add('attendee', 'MAILTO:xyz@example.com')

#event = Event()
#event.add('summary', 'Python meeting about calendaring')
#event.add('dtstart', datetime(2021, 4, 4, 8, 0, 0, tzinfo=pytz.utc))
#event.add('dtend', datetime(2021, 4, 4, 10, 0, 0, tzinfo=pytz.utc))
#event.add('dtstamp', datetime(2021, 4, 4, 0, 10, 0, tzinfo=pytz.utc))

# Adding events to calendar
#cal.add_component(event)

#directory = str(Path(__file__).parent.parent) + "/"
#print(directory)
#f = open(os.path.join(directory, 'example.ics'), 'wb')
#f.write(cal.to_ical())
#f.close()
#In this tutorial, you’ll learn about #Object-Oriented Programming (OOP) in Python #and its fundamental concept with the help of #examples.,Object-Oriented Programming makes #the program easy to understand as well as #efficient.,One of the popular approaches to #solve a programming problem is by creating #objects. This is known as Object-Oriented #Programming (OOP).,In the above program, we #define two methods i.e sing() and dance(). #These are called instance methods because #they are called on an instance object i.e blu.
#
#The example for class of parrot can be :
#
#class Parrot:
#   pass
#The example for object of parrot class can be:
#
#obj = Parrot()
#Example 1: Creating Class and Object in Python
#class Parrot:
#
#   # class attribute
#species = "bird"
#
## instance attribute
#def __init__(self, name, age):
#   self.name = name
#self.age = age
#
## instantiate the Parrot class
#blu = Parrot("Blu", 10)
#woo = Parrot("Woo", 15)
#
## access the class attributes
#print("Blu is a {}".format(blu.__class__.#species))
#print("Woo is also a {}".format(woo.__class__.#species))
#
## access the instance attributes
#print("{} is {} years old".format(blu.name, #blu.age))
#print("{} is {} years old".format(woo.name, #woo.age))
#Output
#
#Blu is a bird
#Woo is also a bird
#Blu is 10 years old
#Woo is 15 years old
#Example 2 : Creating Methods in Python
#class Parrot:
#
#   # instance attributes
#def __init__(self, name, age):
#   self.name = name
#self.age = age
#
## instance method
#def sing(self, song):
#   return "{} sings {}".format(self.name, #song)
#
#def dance(self):
#   return "{} is now dancing".format(self.#name)
#
## instantiate the object
#blu = Parrot("Blu", 10)
#
## call our instance methods
#print(blu.sing("'Happy'"))
#print(blu.dance())
#Output
#
#Blu sings 'Happy'
#Blu is now dancing
#Example 3: Use of Inheritance in Python
## parent class
#class Bird:
#
#   def __init__(self):
#   print("Bird is ready")
#
#def whoisThis(self):
#   print("Bird")
#
#def swim(self):
#   print("Swim faster")
#
## child class
#class Penguin(Bird):
#
#   def __init__(self):
#   # call super()
#function
#super().__init__()
#print("Penguin is ready")
#
#def whoisThis(self):
#   print("Penguin")
#
#def run(self):
#   print("Run faster")
#
#peggy = Penguin()
#peggy.whoisThis()
#peggy.swim()
#peggy.run()
#Output
#
#Bird is ready
#Penguin is ready
#Penguin
#Swim faster
#Run faster
#Example 4: Data Encapsulation in Python
#class Computer:
#
#   def __init__(self):
#   self.__maxprice = 900
#
#def sell(self):
#   print("Selling Price: {}".format(self.#__maxprice))
#
#def setMaxPrice(self, price):
#   self.__maxprice = price
#
#c = Computer()
#c.sell()
#
## change the price
#c.__maxprice = 1000
#c.sell()
#
## using setter
#function
#c.setMaxPrice(1000)
#c.sell()
#Output
#
#Selling Price: 900
#Selling Price: 900
#Selling Price: 1000
#Example 5: Using Polymorphism in Python
#class Parrot:
#
#   def fly(self):
#   print("Parrot can fly")
#
#def swim(self):
#   print("Parrot can't swim")
#
#class Penguin:
#
#   def fly(self):
#   print("Penguin can't fly")
#
#def swim(self):
#   print("Penguin can swim")
#
## common interface
#def flying_test(bird):
#   bird.fly()
#
##instantiate objects
#blu = Parrot()
#peggy = Penguin()
#
## passing the object
#flying_test(blu)
#flying_test(peggy)
#Output
#
#Parrot can fly
#Penguin can 't fly