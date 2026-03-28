import random

def generate_puzzle(low=1, high=100):
    print(f"I'm thinking of a number between {low} and {high}")
    return random.randint(low, high)


# EAFP策略
def make_guess(target):
    guess = None

    while guess == None:
        try:
            guess = int(input("Guess:"))
        except ValueError:
            print("Enter an integer!")

    if guess == target:
        return True
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")

    return False

# # LBYL策略
# def make_guess(target):
#     guess = None

#     while guess == None:
#         guess = input("Guess:")

#         if guess.isdigit():
#             guess = int(guess)
#         else:
#             print("Enter an integer!")
#             guess = None

#     if guess == target:
#         return True

#     if guess < target:
#         print("Too low")
#     elif guess > target:
#         print("Too high")
    
#     return False

def play(tries=8):
    target=generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return 
        tries -= 1

    print(f"Game is over, the answer is {target}")

if __name__ == "__main__":
    play()

