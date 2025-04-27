"""
BINGO GAME
Author: Lyle Jose
"""
print("Welcome to the Bingo Game!\n")
print("Continuously enter a different number between 1 and 80\n")
print("If you get all 10 numbers correct, you will get BINGO!\n")

def check_input_num(num):
    if num not in range(1, 81):
        return 404
    else:
        return num
    
# list of bingo numbers, and a list to store correctly guessed numbers
bingoNums = [7, 26, 40, 58, 73, 17, 22, 12, 13, 33]
bingoNums_Collected = []

while len(bingoNums) != 0:
    num = int(input("Enter a number between 1 and 80:"))
    num = check_input_num(num)

    if num == 404:
        print("Error in input. Enter a number within range.")
    else:
        if num in bingoNums:
            bingoNums_Collected.append(num)
            print("This number has been scracthed off your bingo card.")
        if num not in bingoNums:
            print("This number is not on your bingo card.")
        if len(bingoNums_Collected) == 10:
            print("You have BINGO!")
            break