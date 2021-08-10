#The Hunger Games
from math import ceil
import random

numOfDistricts = 12#set the number of districts
#initialize some more stuff
tributes = []
dead = []
deadthisday = []
day = 1

class Tribute:

    def __init__(self, nme, dist, inj):
        self.name = nme[:-2]#Set the name to whatever the player entered MINUS the gender and space at the end
        self.district = dist#set the district to whatever it was assigned to.
        self.inj = False#set inj to false by default
        self.asleep = False
        self.kills = 0
        self.gender = nme[(len(nme)-1):]#get the gender the player entered. the last letter of the input

        if self.gender.lower() == "m":#if the player is male
            #give him male pronouns
            self.hisher = "his"
            self.himher = "him"
            self.heshe = "he"
        elif self.gender.lower() == "f":
            #give her female pronouns
            self.hisher = "her"
            self.himher = "her"
            self.heshe = "she"
        else:
            #give them they/them pronouns
            self.hisher = "their"
            self.himher = "them"
            self.heshe = "they"

def initialize():
    global tributes, numOfDistricts, dead, deadthisday, day
    tributes = []
    dead = []
    deadthisday = []
    day = 1
    
    while True:
        try:
            numOfDistricts = int(input("Enter number of districts\n"))
            break
        except ValueError:
            print("Number of districts must be a number\n")
    temp = ""#dummy variable
    i=1

    print("\nName your tributes with the following format:\n name gender\ne.g. Jane Doe f\n")
    #while i is less than or equal to double the number of districts (two tributes for each district)
    while i<=(numOfDistricts*2):
        #"Name tribute number" whatever number we're on
        temp = ""
        while True:
            temp = input("Name tribute #{}\n".format(i))
            if (len(temp) >= 3):
                break
            else:
                print("Name must be at least 3 characters\n")

        #create a new tribute. temp is the name you entered.
        #What ceil(i/2) does is, since there's half as many districts as there
        #are tributes, divide whatever number tribute we're on by 2 and round up.
        #So if we're on tribute #2 , 2/2 is 1, so it will be district one.
        #Tribute #15 would be 7.5, rounded up is district 8. You get the idea.
        #The last bit sets inj to false.
        tributes.append(Tribute(temp, ceil(i/2), False))
        i += 1

        
    #for each tribute...
    for j in range(len(tributes)):
        #Print their name, district, and gender. This is mainly for debugging purposes.
        print("{}, district {}, {}".format(tributes[j].name, tributes[j].district, tributes[j].gender))

#===============================================================================

def pickRandomAction(tribute1, tribute2):
    #TODO: Make sure each person can only interact with eachother once.
    global tributes, dead, deadthisday
    #make their names easier to access.
    t1 = tribute1.name
    t2 = tribute2.name

    #This bit's pretty self explanitory but I should still say what it does.
    #We get a random number, between 0 and however many scenarios I've created.
    #It then runs whatever scenario it lands on. Some of these have multiple layers.
    #There's also a few easter eggs.
    num = random.randint(0,41)

    if num == 0:
        print("{} picks flowers".format(t1))
    elif num == 1:
        print("{} sees {} in the distance, but ignores {} for now.".format(t1, t2, tribute2.himher))
    elif num == 2:
        print ("{} thinks about home.".format(t1))
    elif num == 3:
        if (tribute1.inj == True and tribute2.inj == False):
            print ("{} tries to shank {}, but {} is too quick for {}.".format(t1, t2, t2, tribute1.himher))
        elif (tribute1.inj == True and tribute2.inj == True):
            print ("{} and {} see eachother, but both are too weak to fight.".format(t1, t2))
        elif (tribute1.inj == False and tribute2.inj == True):
            print ("{} stabs {} with an improvised shank and kills {}.".format(t1, t2, tribute2.himher))
            tribute1.kills += 1
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
        elif (tribute1.inj == False and tribute2.inj == False):
            print ("{} stabs {} with an improvised shank and injures {}.".format(t1, t2, tribute2.himher))
            tribute2.inj = True
    elif num == 4:
        temp = random.randint(0,2)
        if temp == 0:
            print ("{} tries to eat something inedible and regrets it.".format(t1))
            tribute1.inj = True
        else:
            print ("{} tries to eat something inedible.".format(t1))
    elif num == 5:
        print ("{} starts talking to {}self".format(t1, tribute1.himher))
    elif num == 6:
        if tribute2.inj == False:
            print ("{} shoots {} with an arrow.".format(t1, t2))
            tribute2.inj = True
        else:
            print ("{} shoots and kills {} with an arrow".format(t1, t2))
            tribute1.kills += 1
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
            
    elif num == 7:
        print ("{} picks up some medicine.".format(t1))
        tribute1.inj = False
    elif num == 8:
        print ("{} thinks about murder.".format(t1))
    elif num == 9:
        print ("{} tries to shoot {} with an arrow, but misses.".format(t1, t2))
    elif num == 10:
        print ("{} removes {}'s head with a broadsword.".format(t1, t2))
        tribute1.kills += 1
        tributes.remove(tribute2)
        dead.append(tribute2)
        deadthisday.append(tribute2)
    elif num == 11:
        temp = random.randint(0,3)
        if tribute2.inj == True and temp != 3:
            print ("{} throws a rock at {}'s face and kills {}".format(t1, t2, tribute2.himher))
            tribute1.kills += 1
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
        elif tribute2.inj == True and temp == 3:
            print("{} throws a rock at {}'s face.".format(t1, t2))
        elif tribute2.inj == False:
            print ("{} throws a rock at {}'s face very hard.".format(t1, t2))
            tribute2.inj = True
            
    elif num == 12:
        print ("{} steps on a landmine.".format(t1))
        tributes.remove(tribute1)
        dead.append(tribute1)
        deadthisday.append(tribute1)
    elif num == 13:
        print ("{} hides in some bushes".format(t1))
    elif num == 14:
        print ("{} recieves a supply drop from an unknown sponser.".format(t1))
        tribute1.inj = False
    elif num == 15:
        print ("{} steps in something indescribable.".format(t1))
    elif num == 16:
        temp = random.randint(0,10)
        if temp == 10:
            print ("{} dies of dysentary".format(t1))
            tributes.remove(tribute1)
            dead.append(tribute1)
            deadthisday.append(tribute1)
        else:
            print ("{} climbs a tree.".format(t1))
    elif num == 17:
        print ("{} tires {}self out from running.".format(t1, tribute1.himher))
    elif num == 18:
        print ("{} begs for mercy from {}. {} allows it.".format(t2, t1, tribute1.heshe))
    elif num == 19:
        print ("{} begs for mercy from {}, but {} is in no mood and cuts {} down.".format(t1, t2, t2, tribute1.himher))
        tribute2.kills += 1
        tributes.remove(tribute1)
        dead.append(tribute1)
        deadthisday.append(tribute1)
    elif num == 20:
        temp = random.randint(0,10)
        if temp != 6:
            print ("{} gets bit by a savage rabbit.".format(t1))
            tribute1.inj = True
        else:
            print ("{} gets murdered by a savage rabbit.".format(t1))
            tributes.remove(tribute1)
            dead.append(tribute1)
            deadthisday.append(tribute1)
    elif num == 21:
        print ("{} activates a tripwire and gets shot with a bunch of poison darts.".format(t1))
        tributes.remove(tribute1)
        dead.append(tribute1)
        deadthisday.append(tribute1)
    elif num == 22:
        print ("{} strangles {} to death.".format(t1, t2))
        tribute1.kills += 1
        tributes.remove(tribute2)
        dead.append(tribute2)
        deadthisday.append(tribute2)
    elif num == 23:
        print ("{} poisons a potato".format(t1))
    elif num == 24:
        print ("{} carves {} initials into a tree".format(t1, tribute1.hisher))
    elif num == 25:
        if tribute1.inj == True:
            print ("{} gets in a swordfight with {}, and loses.".format(t1, t2))
            tribute2.kills += 1
            tributes.remove(tribute1)
            dead.append(tribute1)
            deadthisday.append(tribute1)
        else:
            print ("{} gets in a swordfight with {}, and wins.".format(t1, t2))
            tribute1.kills += 1
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
    elif num == 26:
        print ("{} caves {} skull in with a club".format(t1, t2))
        tribute1.kills += 1
        tributes.remove(tribute2)
        dead.append(tribute2)
        deadthisday.append(tribute2)
    elif num == 27:
        print ("{} thinks about the human condition.".format(t1))
    elif num == 28:
        if len(dead)>0:
            temp = random.randint(0, len(dead)-1)
            print ("{} finds {}'s corpse.".format(t1, dead[temp].name))
        else:
            print ("{} gets mortally wounded by {} and is left to die.".format(t1, t2))
            tribute2.kills += 1
            tributes.remove(tribute1)
            dead.append(tribute1)
            deadthisday.append(tribute1)
    elif num == 29:
        print ("{} nearly steps on a landmine".format(t1))
    elif num == 30:
        print ("{} creepily watches {}.".format(t1, t2))
    elif num == 31:
        print ("{} stabs {} in the heart.".format(t1, t2))
        tribute1.kills += 1
        tributes.remove(tribute2)
        dead.append(tribute2)
        deadthisday.append(tribute2)
    elif num == 32:
        temp = random.randint(0,8)
        if temp == 8:
            print ("{} points both middle fingers towards the sky".format(t1))
        elif temp == 2:
            print ("{} throws a rock at {}'s face, misses, and gets shot with an arrow".format(t1, t2))
            if tribute1.inj == True:
                tribute2.kills += 1
                tributes.remove(tribute1)
                dead.append(tribute1)
                deadthisday.append(tribute1)
            else:
                tribute1.inj = True
        else:
            print ("{} shoots a squirrel for food.".format(t1))

    elif num == 33:
        print ("{} punches a leaf".format(t1))
    elif num == 34:
        print ("{} pisses in a bush".format(t1))
    elif num == 35:
        print ("{} looks desparately around for something to eat".format(t1))
    elif num == 36:
        temp = random.randint(0, 300)

        if temp == 300:
            print ("{} and {} have hot, steamy, sweaty sex".format(t1, t2))
        else:
            print ("{} practices stabbing on a dead squirrel".format(t1))
    elif num == 37:
        print ("{} trips a tripwire and gets shot in the arm with an arrow".format(t1))
        tribute1.inj = True
    elif num == 38:
        print ("{} does some exploring".format(t1))
    elif num == 39:
        print ("{} and {} sing songs together".format(t1, t2))
    elif num == 40:
        print("{} tries to eat tree bark".format(t1))
    elif num == 41:
        print ("{} smacks {} with a yard stick".format(t1, t2))
               
def pickRandomNightAction(tribute1, tribute2):
    #This is the same as pickRandomAction(), just with a different scenario set.
    global tributes, dead, deadthisday
    t1 = tribute1.name
    t2 = tribute2.name
    num = random.randint(0,26)
    tribute1.asleep = False

    if num == 0:
        print ("{} cries {}self to sleep.".format(t1, tribute1.himher))
        tribute1.asleep = True
    elif num == 1:
        print ("{} walks around in circles, unable to sleep.".format(t1))
        tribute1.inj = True
    elif num == 2:
        print ("{} goes into a tree and sleeps there.".format(t1))
        tribute1.asleep = True
    elif num == 3:
        if tribute2.asleep == True:
            print ("{} kills {} in {} sleep".format(t1, t2, tribute2.hisher))
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
            tribute1.kills += 1
        else:
            print ("{} sneaks up on {} and stabs {} to death.".format(t1, t2, tribute2.himher))
            tributes.remove(tribute2)
            dead.append(tribute2)
            deadthisday.append(tribute2)
            tribute1.kills += 1
    elif num == 4:
        if tribute2.asleep == False:
            print ("{} invites {} into {} shelter.".format(t1, t2, tribute1.hisher))
        else:
            print ("{} sets {} on fire.".format(t1, t2))
            tribute2.inj = True
    elif num == 5:
        temp = random.randint(0,5)
        if tribute1.asleep == False:
            if tribute1.inj == True:
                print ("While looking for shelter, {} trips and falls onto some sharp rocks and bleeds out.".format(t1))
                tributes.remove(tribute1)
                dead.append(tribute1)
                deadthisday.append(tribute1)
            else:
                if temp == 2:
                    print ("{} trips on some sharp rocks and gets knocked unconscious.".format(t1))
                    tribute1.inj = True
                else:
                    print ("{} trips on some rocks, and then decides to sleep there.".format(t1))
                    tribute1.asleep = True
        else:
            print("{} sleeps well.".format(t1))
            tribute1.asleep = True
    elif num == 6:
        temp = random.randint (0,15)
        if temp == 1:
            print ("{} sees a bleak future even with victory, and kills {}self".format(t1, tribute1.himher))
            tributes.remove(tribute1)
            dead.append(tribute1)
            deadthisday.append(tribute1)
        else:
            print ("{} falls asleep in a flower patch.".format(t1))
            tribute1.asleep = True
    elif num == 7:
        print ("{} tries not to think about tomorrow.".format(t1))
        tribute1.asleep = True
    elif num == 8:
        temp = random.randint(0,10)
        if temp == 4:
            print ("{} falls asleep standing up somehow.".format(t1))
            tribute1.asleep = True
        else:
            print ("{} goes catatonic and fails to sleep".format(t1))
    elif num == 9:
        print("{} stumbles around in darkness".format(t1))
    elif num == 10:
        if tribute2.asleep == False:
            print ("{} sees {}, and slowly backs away.".format(t1, t2))
        else:
            print ("{} eats a poison potato.".format(t1))
            tribute1.inj = True
    elif num == 11:
        print ("{} gets bit by a bat and dies.".format(t1))
        tributes.remove(tribute1)
        dead.append(tribute1)
        deadthisday.append(tribute1)
    elif num == 12:
        print ("{} hugs a tree".format(t1))
    elif num == 13:
        if tribute1.inj == True:
            print ("{} collapses from exhaustion".format(t1))
            tribute1.asleep = True
        else:
            print ("{} missteps and cuts {} leg.".format(t1, tribute1.hisher))
            tribute1.inj = True
    elif num == 14:
        print ("{} falls asleep in a ditch.".format(t1))
        tribute1.asleep = True
    elif num == 15:
        print ("{} sleeps with one eye open.".format(t1))
    elif num == 16:
        print ("{} has nightmares about {} killing {}".format(t1, t2, tribute1.himher))
        tribute1.asleep = True
    elif num == 17:
        print ("{} falls asleep to the sound of crickets.".format(t1))
        tribute1.asleep = True
    elif num == 18:
        print ("{} dreams about {}self as victor.".format(t1, tribute1.himher))
        tribute1.asleep = True
    elif num == 19:
        print ("{} stares at the night sky.".format(t1))
    elif num == 20:
        print ("{} imagines a world where anyone can be anything.".format(t1))
    elif num == 21:
        print ("{} falls asleep near a bush".format(t1))
        tribute1.asleep = True
    elif num == 22:
        print ("{} struggles to fall asleep, but manages in the end.".format(t1))
        tribute1.asleep = True
    elif num == 23:
        print ("{} lays down with {} eyes wide open".format(t1, tribute1.hisher))
    elif num == 24:
        print("{} has nightmares ".format(t1))
        tribute1.asleep = True
    elif num == 25:
        print ("{} makes a bed out of some grass".format(t1))
        tribute1.asleep = True
    elif num == 26:
        print ("{} keeps watch in a tree".format(t1))
        
#============================================================================
        
def Day():
    global day, tributes

    print ("**Day {}**\n".format(day))#say what day it is
    i=0
    while i < len(tributes):#for each living tribute...
        othertribs = []
        j=0
        while j < len(tributes):
            if tributes[j] != tributes[i]:
                othertribs.append(tributes[j])
            j += 1
        rTrib = random.randint(0,len(othertribs)-1)#pick a random target tribute

        
        
        pickRandomAction(tributes[i], othertribs[rTrib])
        i += 1

def Night():
    global day, tributes
    print("**Night {}**\n".format(day))
    i=0
    while i < len(tributes):#for each living tribute...
        othertribs = []
        j=0
        while j < len(tributes):
            if tributes[j] != tributes[i]:
                othertribs.append(tributes[j])
            j += 1
        rTrib = random.randint(0,len(othertribs)-1)#pick a random target tribute

        pickRandomNightAction(tributes[i], othertribs[rTrib])
        i += 1
    day += 1

def Cannons():
    global deadthisday
    print("\n**{} cannon shots go off in the distance.**".format(len(deadthisday)))
    input()
    for i in range(len(deadthisday)):
        print ("{}\nDistrict {}\n".format(deadthisday[i].name, deadthisday[i].district))
    del deadthisday[:]

#===========================================================================
#Game Loop
while True:
    initialize()
    while len(tributes) != 1: #As long as there is more than 1 tribute remaining
        Day() #Start a new day
        input() 
        if len(tributes) == 1: #If there is only 1 tribute left
            break #Break the cycle, move on
        Night() #Otherwise go on to night
        Cannons() #List all the tributes who died
        input()
    print ("{} from District {} survived the Hunger Games!".format(tributes[0].name, tributes[0].district))
    input()

    print ("Order of death\n")
    for i in range(len(dead)): #For each dead tribute
        print ("{}: {}".format((numOfDistricts*2)-i, dead[i].name)) #List the name and time of death of the tribute.
        #Explanation of (numOfDistricts*2)-i
        #numOfDistricts is the number of districts in the game.
        #Since this is player defined we need a formula to find last place. It isn't necessarily 12.
        #So The total number of districts is last place. Then it multiplies it by 2 to get the number of tributes.
        # i is the current position of this function in the array. The farther along it is, the higher the position of the tribute, so the position and ranking have an inverse relationship.
    input()
    print ("Kills\n")
    for i in range(len(dead)): #For each dead tribute
        tributes.append(dead[i]) 

    #Sort the tributes by number of kills
    killorder = []
    while len(killorder) < (numOfDistricts * 2):
        highest = 0
        nextHighest = None
        for i in range(len(tributes)):
            if tributes[i].kills > highest:
                highest = tributes[i].kills
                nextHighest = tributes[i]
            if nextHighest == None:
                nextHighest = tributes[0]
        tributes.remove(nextHighest)
        killorder.append(nextHighest)
        
    for i in range(len(killorder)):
        print ("{} - {}".format(killorder[i].kills, killorder[i].name))

    again = input("\nType 'yes' to play again; anything else to exit\n")
    if (not again.lower().startswith('y')):
        break
    else:
        print("\n"*10)