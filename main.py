
user_input = int(input("Enter your number: "))

def fizz_buzz():
  for number in range(1, user_input):
    if number % 5 == 0 and number % 3 == 0:
      print("FizzBuzz")
    elif number % 5 == 0:
      print("Buzz")
    elif number % 3 == 0:
      print("Fizz")
    else:
      print(number)
      
fizz_buzz()