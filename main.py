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
        print(mealsForThePeriod)
        replacement = input("What do you want to replace? \nType A for the first dish or type B for the side dish\n").lower()
        if replacement == 'a':
          print("I chose " + mealsForThePeriod[-1])
          mealChoice,sideChoice = mealsForThePeriod[-1].split(' & ')
          print("let's try something else")
          food = random.choice(list(meals)) + " & " + sideChoice
          meal= food.title()
          mealsForThePeriod.pop()
          mealsForThePeriod.append(meal)
          print(*mealsForThePeriod, sep = "\n")
          doYouLoveMe(mealsForThePeriod, mealChoice, sideChoice, food, meal, meals, sides)
        else: 
          print("I chose " + mealsForThePeriod[-1])
          mealChoice,sideChoice = mealsForThePeriod[-1].split(' & ')
          print("let's try something else")
          food = mealChoice + " & " + random.choice(list(sides))
          meal= food.title()
          mealsForThePeriod.pop()
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
cookingWithEchols(['taquitos','chicken tenders','kievs','soups','potstickers','pork buns' 'chicken','roasted veggies', 'seafood' ,'stir fry','tacos','tofu','hamburgers','hot dogs','sloppy joe','pulled pork','salmon','bacon','shredded beef', 'pot roast', 'corned beef hash', 'spaghetti', 'katsu','stews','hamburg steak', 'burritos','empanadas','egg','onigiri','buns','loco moco', 'meatballs','meatloaf','ravioli'], ['white rice','salad','italian pasta','soups','asian pasta','egg rolls','veggies', 'quinoa salad','fried rice', 'yellow rice','fries', 'asparagus','brussel sprouts', 'waffles','potatoes', 'mashed potatoes', 'garlic bread'], 8, ["Jamin","Elaine"])
#todo MainDishes json and sideDishs json to shorten this