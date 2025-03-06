import random

def roll_dice():
    return random.randint(1, 6)

def get_user_choice():
    while True:
        user_input = input("Do you want to roll again? (yes/no): ").strip().lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("❌ Invalid input! Please type 'yes' or 'no'.")

def main():
    while True:
        input("Press Enter to roll the dice...")  
        dice_value = roll_dice()  
        print(f"🎲 You rolled a {dice_value}!") 

        user_input = get_user_choice()
        if user_input == "no":
            print("Goodbye! Thanks for playing. 😊")
            break  
if __name__ == "__main__":
    main()

