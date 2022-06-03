from unittest import result
from dice import Die
from hand import Hand

#I will create a "game" for each line in yatzy and test them as I go.
#The upper section will be the same for all, except the number, therefore I create one game for all.

def rolldice(gameDice):
    values=[]
    for dice in gameDice:
        dice.roll()
        values.append(dice.returnNo())
    return values

def xofakind(gameDice,number): #find X number of a kind, where X can be 2, 3, 4, aso. 
    #Use count()?
    #rollHand=Hand()
    #keepHand=Hand()
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values,reverse=True)
        
        for j in range(len(sortedvalues)-2):
            if sortedvalues[j]==sortedvalues[j+1] and sortedvalues[j]==sortedvalues[j+2]:
                results.extend(sortedvalues[j:j+3])
                print(results)
                points = sum(results)
                return points
                break
            else:
                points=0
    return points

def upperSection(gameDice,number):
    results=[]
    for i in range(3):
        for dice in gameDice:
            dice.roll()
            if dice.returnNo()==number:
                results.append(dice.returnNo())
                gameDice.remove(dice)
    points=sum(results)
    return points 

# 1 pair
#Should I keep the highest die in results even when it's not a pair? 
def onepair(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values,reverse=True)
        for i in range(len(sortedvalues)-1):
            if sortedvalues[i]==sortedvalues[i+1]:
                results.extend(sortedvalues[i:i+2])
                gameDice=gameDice[:-2] #everything except the two last elements. 
                break
    if len(results)>0:
        sortedresults=sorted(results,reverse=True)
        sortedresults=sortedresults[0:2]
        points=sum(sortedresults)
    else:
        points=0
    return points

# 2 pairs
def twopairs(gameDice):
    results=[]

    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values,reverse=True)
        for i in range(len(sortedvalues)-1):
            if sortedvalues[i]==sortedvalues[i+1]:
                results.extend(sortedvalues[i:i+2])
                gameDice=gameDice[:-2] #everything except the two last elements. 
                break

    if len(results)==4:
        points=sum(results)
    else:
        points=0
    return points

# 3 of a kind
def threeofakind(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values,reverse=True)
        for j in range(len(sortedvalues)-2):
            if sortedvalues[j]==sortedvalues[j+1] and sortedvalues[j]==sortedvalues[j+2]:
                results.extend(sortedvalues[j:j+3])
                points = sum(results)
                return points
                break
            else:
                points=0
    return points

# 4 of a kind
def fourofakind(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values,reverse=True)
        for j in range(len(sortedvalues)-3):
            if sortedvalues[j]==sortedvalues[j+1] and sortedvalues[j]==sortedvalues[j+2] and sortedvalues[j]==sortedvalues[j+3]:
                results.extend(sortedvalues[j:j+4])
                points = sum(results)
                return points
                break
            else:
                points=0
    return points

# Low straight
def lowstraight(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values)
        for value in sortedvalues:
            if value not in results and value!=6:
                results.append(value)
                gameDice=gameDice[:-1]
    points=sum(results)
    if points<15:
        points=0
    return points

# High Straight
def highstraight(gameDice):
    results=[]
    # Sort the values of the dice. Compare two dice together from the top. If they are the same, remove them from gameDice and put them into results list. 
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values)
        for value in sortedvalues:
            if value not in results and value!=1:
                results.append(value)
                gameDice=gameDice[:-1]
    points=sum(results)
    if points<20:
        points=0
    return points

# Full House
def fullhouse(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        


# Chance
def chance(gameDice):
    results=[]
    for i in range(3):
        values=rolldice(gameDice)
        sortedvalues=sorted(values)
        print(sortedvalues)
        save=[6,5]
        for j in sortedvalues:
            if j in save:
                results.append(j)
                gameDice=gameDice[:-1]
        print(results)
        save.append(4-i)
        save.append(3-i)
    points=sum(results)
    return points

# Yatzy/Yahtsee
def yatzy(gameDice):
    results=[]


def yatzygame():
    #create a list of five dice, all are set to value 1. 
    gameDice = [Die(),Die(),Die(),Die(),Die()]

    #First game:
    #ones=upperSection(gameDice,1)
    #print(ones)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #One pair:
    #onePair=onepair(gameDice)
    #print(onePair)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Two pairs:
    #twoPairs=twopairs(gameDice)
    #print(twoPairs)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Three of a kind:
    #threeOfAKind=threeofakind(gameDice)
    #print(threeOfAKind)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Four of a kind:
    #fourOfAKind=fourofakind(gameDice)
    #print(fourOfAKind)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Low Straight:
    #lowStraight=lowstraight(gameDice)
    #print(lowStraight)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #High Straight:
    #highStraight=highstraight(gameDice)
    #print(highStraight)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Chance:
    #Chance=chance(gameDice)
    #print(Chance)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    upperSectionv2(1)

if __name__ == "__main__": #This will not be run if yatzygames gets imported to another file. 
    yatzygame()
