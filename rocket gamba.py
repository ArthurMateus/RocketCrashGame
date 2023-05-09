from random import randint
from time import sleep
import os
from colorama import Fore

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def multiplier():
    mtp = randint(100, 500)
    value = mtp / 100
    return value

def weight():
    num = randint(1,1000)
    if num <= 10:
        return 1
    elif num <= 20 and num > 10:
        return 2
    elif num <= 20 and num > 10:
        return 3
    elif num <= 60 and num > 20:
        return 4
    elif num <= 180 and num > 60:
        return 5
    elif num <= 340 and num > 180:
        return 6
    elif num <= 470 and num > 340:
        return 7
    elif num <= 560 and num > 470:
        return 8
    elif num <= 690 and num > 560:
        return 9
    elif num <= 750 and num > 690:
        return 10
    elif num <= 800 and num > 750:
        return 11
    elif num <= 860 and num > 800:
        return 12
    elif num <= 900 and num > 860:
        return 13
    elif num <= 930 and num > 900:
        return 14
    elif num <= 950 and num > 930:
        return 15
    elif num <= 970 and num > 950:
        return 16
    elif num <= 980 and num > 970:
        return 17
    elif num <= 985 and num > 980:
        return 18
    elif num <= 992 and num > 985:
        return 19
    elif num <= 1000 and num > 992:
        return 20
    

def main():
    while True:
        cls()
        stop = 'nonsense'
        total = 0
        points= 0
        totals = 0
        bkamt = weight()
        wlcheck = 1

        print('Welcome to the Rocket Crash Game!')
        print(Fore.RED)
        print('Stop the multiplier whenever you want to, if it crashes, you lose!')
        print(Fore.MAGENTA)
        ipoints = int(input('Enter the amount of points you want to input: '))
        for c in range(1,bkamt):
            cls()
            round = multiplier()
            total += round
            
            print(Fore.BLUE + 'Multiplier is at {:.2f}'.format(total))
            if stop != '':
                totals = total
                points = ipoints * totals
                print(Fore.GREEN + 'You are at {:.2f} points!'.format(points))
                stop = str(input(Fore.CYAN + 'Press Enter to Stop or anything else to continue: '))
                wlcheck += 1
            elif stop == '':
                print(Fore.YELLOW+ 'You Stopped!')
                sleep(.5)
        cls()
        if wlcheck < bkamt:
            print(Fore.GREEN + 'You Won!')
            print('You Stopped at {:.2f}x and won {:.2f} points!'.format(totals, points))
            print('The crasher stopped at {:.2f}'.format(total))
        elif wlcheck == bkamt:
            print(Fore.RED + 'You Lost {:.2f}!'.format(ipoints))
            print("The crasher was at {:.2f}x and you didn't stop in time".format(totals))
        print(Fore.RESET)
        yorn = str(input('Do you want to play again? [Y/N]: '))
        if yorn.upper() == 'N':
            break


main()