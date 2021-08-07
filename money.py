from sys import call_tracing
from colorama import Fore, init
import os
import time

init()

y = Fore.LIGHTYELLOW_EX
g = Fore.LIGHTGREEN_EX
r = Fore.RESET
red = Fore.LIGHTRED_EX

def zero(number):
    if number < 10:
        out = "00" + str(number) 
    elif number < 100:
        out = "0" + str(number)
    else:
        out = str(number)

    return out


def add():
    what = input("[+] What: ")
    price = input("[+] Price:  ")

    file = open("data.txt", "a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S") + " | " + "{:7.2f}".format(float(price)) + " | " + what + "\n")
    file.close()

    print("")
    main()

def list_all():

    print("")

    number = 0

    firstline = open("data.txt", "r")
    total_line = firstline.readline().strip("\n")
    firstline.close()

    total = 0

    with open("data.txt") as f:
        next(f)
        for line in f:
            print(zero(number) + " | " + line.strip("\n"))
            number += 1
            splittedline = line.split(" | ")
            total += float(splittedline[1])

    print("")
    result = float(total_line) - float(total)

    if float(result) < 0:
        result_out = red + str("{:7.2f}".format(float(result))) + r
    else:
        result_out = g + str("{:7.2f}".format(float(result))) + r

    calc = str("{:7.2f}".format(float(total_line))) + " | " + str("{:7.2f}".format(float(total))) + " | " + result_out

    print("="*27)
    print(calc)
    print("")
    main()


def delete():
    number = input("[+] id number: ")

    file = open("data.txt", "r")
    lines = file.readlines()
    del lines[int(number) + 1]
    file.close()

    new_file = open("data.txt", "w+")

    for line in lines:
        new_file.write(line)

    new_file.close()

    main()



def main():
    if not os.path.exists(os.getcwd() + "/data.txt"):
        print("[*] Creating 'data.txt' file...")
        file = open("data.txt", "a")
        inp = input("[+] Enter your current Money: ")
        file.write(inp + "\n")
        file.close()


    x = input(y + "[+] " + r)

    if x == "add":
        add()
    
    elif x == "list":
        list_all()

    elif x == "delete":
        delete()
    
    elif x == "clear":
        os.system("clear")
        main()

    elif x == "exit":
        quit()

    else:
        main()
    

main()