####
# EECS1015 - Midterm
# Name: Alexander Ukhin
# Student ID: 217946807
# Email: alexanderukhin@gmail.com
#
##
import random

def task0():
  print("Midterm Exam - EECS1015\nName: Alexander Ukhin\nStudent ID: 217946807\nemail: alexanderukhin@gmail.com")
  return

def task1():
  firstname = input("Please input your first name: ")
  lastname = (input("Please input your last name: "))
  workhours = int(input("Please input how many hours per week you work: "))
  hourlywage = float(input("Please input your hourly wage: "))
  print("Employee: " + lastname.upper().strip() + ", " + firstname.strip().capitalize())
  print("$" + str("{:.2f}".format(4*workhours*hourlywage)) + " Monthly salary (gross)")
  print("-$" + str("{:.2f}".format(4*workhours * hourlywage*0.25)) + " Tax Deduction")
  print("$" + str("{:.2f}".format(4*workhours * hourlywage-(4*workhours * hourlywage*0.25))) + " Monthly salary (net)")
  return

def task2():
  bal = 10.00
  #make the menu in a list to represent falafel, pizza, salad, coffee
  menu = ["exit", "falafel", "pizza", "salad", "coffee"]
  prices = [0.00, 3.00, 6.00, 1.50, 1.00]
  print("You have " + str(bal) + " - what item do you want?\n1: Falafel $3.00\n2: Pizza $6.00\n3: Salad $1.50\n4: Coffee $1.00\n Enter 0 to exit.")
  order = int(input("Your order: "))
  #Checks for proper input
  while order != 0 and order != 1 and order != 2 and order !=3 and order != 4:
    order = int(input("Please provide a proper order number: "))

  while order >= 0 and order <= 4:
    if order == 0:
        print("Thank you!")
        break
    while (bal - prices[order]) > 0 and order != 0:
        bal = bal - prices[order]
        print("Order for *" + menu[order] + "* confirmed.\nThank you!\nYou have $" + str("{:.2f}".format(bal)) +" remaining.")
        order = int(input("Your order?: "))
        while order != 0 and order != 1 and order != 2 and order != 3 and order != 4:
            order = int(input("Please provide a proper order number: "))
        while bal - prices[order] < 0:
            order = int(input("Sorry, you don't have enough money for that item.\nPlease provide a new order number: "))
  return

def task3():
     dice = random.randrange(1, 7)
     sixcounter = 0
     credit = "Y"
     geigercounter = ""*40
     while credit == "Y" or credit == "y":
        print("Rolling dice 10 times . . .")
        for i in range(0, 9):
            if dice != 6:
                print("[" + str(dice) + "]")
                dice = random.randrange(1, 7)
            if dice == 6:
                print("*[" + str(dice) + "]*")
                sixcounter = sixcounter + 1
                dice = random.randrange(1, 7)
        if sixcounter >= 2:
            print("YOU WIN!")
            credit = input("Do you want to play again? (Y/N): ")
        else:
            print("YOU LOSE!")
            credit = input("Do you want to play again? (Y/N): ")
     return


DNALetters = ["T", "G", "C", "A"]
DNASequence = ""
mutatedDNA = ""
generate = random.randrange(0, 4)
IAEA = random.randrange(0, 2)

def task4():
    global DNALetters
    global DNASequence
    global mutatedDNA
    global generate
    global IAEA
    def generateDNASequence():
        for i in range(0, 40):
            global DNASequence
            generate = random.randrange(0, 4)
            DNASequence = DNASequence + DNALetters[generate]
            if i == 39:
                print(DNASequence + " (DNA)")

    def applyGammaRadiation(DNASequence):
        global generate
        global mutatedDNA
        if IAEA == 0:
            for i in range(0, 40):
                mutatedDNA = mutatedDNA + DNASequence[i]
            print(DNASequence + " (DNA after radiation)")
        else:
            randomLength = random.randrange(0, 40)
            while DNALetters[generate] == DNASequence[randomLength]:
                generate = random.randrange(0, 4)
            for i in range(0, 40):
                if i == randomLength:
                    mutatedDNA = mutatedDNA + DNALetters[generate]
                else:
                    mutatedDNA = mutatedDNA + DNASequence[i]
            print(mutatedDNA + " (DNA after radiation)")

    def detectMutation(DNASequence, mutatedDNA):
        geigercounter = ""
        if DNASequence == mutatedDNA:
            geigercounter = " "*40
            print(geigercounter + "\nNO MUTATION DETECTED")
        else:
            beep = 1
            for i in range(0, 40):
                if DNASequence[i] != mutatedDNA[i]:
                    geigercounter = geigercounter + "^"
                elif DNASequence[i] == mutatedDNA[i]:
                    geigercounter = geigercounter + " "
            print(geigercounter + "\nMUTATION DETECTED")
    generateDNASequence()
    applyGammaRadiation(DNASequence)
    detectMutation(DNASequence, mutatedDNA)
    return

# main function for EECS1015 midterm
def main():
    task0()
    print("\n-- TASK 1 --\n")
    task1()
    print("\n-- Task 2 --\n")
    task2()
    print("\n-- Task 3 --\n")
    task3()
    print("\n-- Task 4 --\n")
    task4()

if __name__=="__main__":
    main()
