import random

random_number = random.randint(20, 50)

def fizz_buzz():
  for number in range(1, random_number):
    if number % 5 == 0 and number % 3 == 0:
      print("FizzBuzz")
    elif number % 5 == 0:
      print("Buzz")
    elif number % 3 == 0:
      print("Fizz")
    else:
      print(number)
      
fizz_buzz()