######################
# EECS1015 - Lab 8
# Name: Alexander Ukhin
# Student ID: 217946807
# Email: alexanderukhin@gmail.com
######################

#Ran out of time, this is as far as I got, tired as all heck, sorry for the mess

import random
#import pytest

maxDays:int
startingBacteria:int
divisionChance:int
maxLifeSpan:int


class Bacteria:
    global startingBacteria
    bacteriaCreated = startingBacteria
    bacteriaDeceased = 0

    #initialize the list bacteriaApt with these parameters
    def __init__(self, divideChance, maxLifespan):
        Bacteria.bacteriaCreated =+ 1
        self.maxLifespan = maxLifespan
        self.divideChance = divideChance
        self.lifespan = random.randrange(1, maxLifespan)
        self.death = False
        self.daysAlive = 0
        # 0 is individual lifespan   1 is maximum lifespan   2 is division chance   3 is if dead   4 is personal days alive

    def live_a_day(self):
        #if it's dead or has lived for more than 10 days it cannot divide, therefore return none
        if self.death or self.daysAlive > 10:
            return None

        random100 = random.randrange(1, 101)
        if random100 < self.divideChance:
            Bacteria.bacteriaCreated += 1
            return Bacteria(self.divideChance, self.maxLifespan)
        #incase bacteria decides not to divide or some other stupid condition
        else:
            return None

    def is_alive(self):
        if self.daysAlive < self.lifespan:
            self.death = True
        #check if it's possible for the bacteria to be alive (Are days lived less than it's lifespan)
        return self.daysAlive < self.lifespan


class Colony:
    global maxLifeSpan, divisionChance, maxDays
    day = 0

    #Creates a colony of bacteria with help of Bacteria class
    def __init__(self, seed):
        self.startBacteriaAmnt = seed
        self.totalBacteria = seed
        self.totalDeadBacteria = 0
        self.day = 0
        #"Bacteria Apartment" list to store created bacteria
        self.bacteriaApt = []

        #loop through amount of bacteria and call live a day (use colony live a day to loop through all bacteria which then uses the bacteria live a day for individual bacteria)
        #loop to create new bacteria based on the amount given in seed
        for i in range(seed):
            self.bacteriaApt.append(Bacteria(divisionChance, maxLifeSpan))

    def live_a_day(self, printDailyReport=True):
        self.day += 1
        #bacteria death counter and list of new bacteria born per day
        bacteriaBornToday = []
        bacteriaDiedToday = 0

        #loop through and see if the bacteria creates a new bacteria or if it's dead
        for i in range(len(self.bacteriaApt)):

            #If bacteria is dead, add to the death list today
            if not self.bacteriaApt.is_alive():
                bacteriaDiedToday += 1

            bacteriaBornToday = Bacteria.live_a_day()


        while Colony.get_colony_size() > 0:
            print("Day %5d Colony Size %6d New Members %6d Expired Members %6d" % (self.day, self.totalBacteria, len(bacteriaBornToday), bacteriaDiedToday))
            if Colony.get_colony_size() < 50000:

                break

    def print_colony_status(self):

        print("Experiment Stopped")
        print("Colony report at DAY " + str(self.day))
        #placeholder for when I have variable
        print("Current colony population " + str(Colony.get_colony_size()))
        print("Total number of bacteria " + str(Bacteria.bacteriaCreated))
        return ""

    #gets the size of the colony during a specific moment
    def get_colony_size(self):
        #This doesn't work, need to find replacement
        return len(self.bacteriaApt)


def main():
    run:str = "Y"
    while run == "Y":
        global maxDays, startingBacteria, divisionChance, maxLifeSpan

        maxDays = int(input("Max number of days to let the colony grow: "))

        startingBacteria = int(input("Number of starting bacteria [1 or greater]: "))
        while startingBacteria < 0.99999999999999999:
            startingBacteria = int(input("Input Number of starting bacteria [1 or greater]: "))

        divisionChance = int(input("% chance of daily division [1-100]: "))
        while divisionChance > 100 or 0.99999999999999 > divisionChance:
            divisionChance = int(input("% chance of daily division [1-100]: "))

        maxLifeSpan = int(input("Maximum lifespan for a bacteria (1 or greater): "))
        while maxLifeSpan < 0.999999999999999999:
            maxLifeSpan = int(input("Input a Maximum lifespan for a bacteria ( >1< or greater): "))

        Colony(startingBacteria)



        run:str = input("Try another Experiment? (Y/N) ")


if __name__ == "__main__":
    main()