import random

def generate_random_list():
     num=random.randint(1,20)
     while True:
          guess=int(input("Guess a number between 1 and 20: "))
          if guess<num:
             print("Too low!")
          elif guess>num:
             print("Too high!")
          else:
             print("You guessed it! The number was", num)
             print("Computer also guessed it in", num, "tries")
             break

print("-----------------------------------Welcome to the Guessing Game-----------------------------------")
generate_random_list()


while True:
     user_input = input("Do you want to play again? (yes/no): ").strip().lower()

     if user_input == "yes":
          generate_random_list()  
     else:
          print("Goodbye!")
          break
     
print("------------------------------------------Thanks for playing----------------------------------------")     


