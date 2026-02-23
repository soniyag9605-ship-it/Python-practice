import random
secret_number=random.randint(1,10)
print("Welcome to number Gussing Game")
print("Guess a number between 1 and 10")
guss=int(input("Enter your guest:"))
if Guess==secret_number:
  print("Congratulations!You guessed correctly")
else:
  print("Wrong guess the correct number was",secret_number)
