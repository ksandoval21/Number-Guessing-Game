import buisness_logic as bl
import colorama
from colorama import Fore, Style, Back 
colorama.init()
print(Fore.LIGHTGREEN_EX +'Welcome! Try to guess the correct number to win the game! \n '+ Style.RESET_ALL)
while True:
    response=input("Choose a level ")
    if response == "1":
        bl.Guess.round_one()
    elif response =="2":
        exit()