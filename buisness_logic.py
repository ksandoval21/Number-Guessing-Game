import random 
class Guess:
    def __init__(self,random_number, guess):
        self.random_number= random_number
        self.guess= guess
        lives=0

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
    

