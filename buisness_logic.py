import random 
lives= 0
def round_one():
    
    guess=input("Enter a number from 1 to 10 ")
    random_number=random.randint(1,10)
    while True:
        if guess == str(random_number):
            print("Correct")
            break
        else:
            print("Incorrect")
            guess=input("Enter a number from 1 to 10 ")
def round_two():
    guess=input("Enter a number from 1 to 50 ")
    random_number=random.randint(1,10)
    while True:
        if guess == str(random_number):
            print("Correct")
            break
        else:
            print("Incorrect")
            guess=input("Enter a number from 1 to 50 ")


