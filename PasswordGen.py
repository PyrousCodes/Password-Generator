#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# I'm currently a beginner at python, so don't expect much
# I got some code using google search-
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random
import time
import os

Length = int(input("What would you like to be the length of your password?: "))
Question = input("Would you like to save your password in a text file?: ")

time.sleep(1)

print("Generating your password...")

time.sleep(2)

Strings = (
    "a",
    "A",
    "b",
    "B",
    "c",
    "C",
    "d",
    "D",
    "e",
    "E",
    "f",
    "F",
    "g",
    "G",
    "h",
    "H",
    "i",
    "I",
    "j",
    "J",
    "k",
    "K",
    "l",
    "L",
    "m",
    "M",
    "n",
    "N",
    "o",
    "O",
    "p",
    "P",
    "q",
    "Q",
    "r",
    "R",
    "s",
    "S",
    "t",
    "T",
    "u",
    "U",
    "v",
    "V",
    "w",
    "W",
    "x",
    "X",
    "y",
    "Y",
    "z",
    "Z"
)

Numbers = (
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
)

Symbols = (
    "`",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "{",
    "}",
    "]",
    "|",
    ";",
    ":",
    "'",
    ",",
    "<",
    ".",
    ">",
    "/",
    "?"
)

file = open("Enter your own directory", 'w')

for x in range(Length):
    Generated_Password = random.choice(Strings + Numbers + Symbols)
    if Question == "Yes" or "yes":
        file.write(Generated_Password)
    else:
        exit

    print(f"{Generated_Password}", end="")

file.close()
