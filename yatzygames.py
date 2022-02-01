from dice import Die

#I will create a "game" for each line in yatzy and test them as I go.
#The upper section will be the same for all, except the number, therefore I create one game for all.
def upperSection(gameDice,number):
    results=[] #This will be a list with all the results in integers, not the dice objects. 
    for i in range(3):
        for dice in gameDice:
            dice.roll()
            if dice.returnNo()==number:
                results.append(dice.returnNo())
                gameDice.remove(dice)
    for element in results:
        gameDice.append(Die()) #I removed the Die element, must return them to the list. In case I forget to reset the dice in the main program. 
    points=sum(results)
    return points 

#1 pair
def onepair(gameDice):
    results=[]
    #Sort the values of the dice. Compare two dice together from the top. If they are the same, remove them from gameDice and put them into results list. 
    for i in range(3):
        values=[]
        for dice in gameDice:
            dice.roll()
            values.append(dice.returnNo())
        sortedvalues=sorted(values,reverse=True)
        for i in range(len(sortedvalues)-1):
            if sortedvalues[i]==sortedvalues[i+1]:
                results.extend(sortedvalues[i:i+2])
                gameDice=gameDice[:-2] #everything except the two last elements. 
                break
    #Should I keep the highest die in results even when it's not a pair? 
    #Want to keep the highest pair we have. Sort the results and keep the first two, if we have two. 

    #if the length of "results" is longer than 0, sort the results and put the two highest in "points". Else set points to 0. 
    if len(results)>0:
        sortedresults=sorted(results,reverse=True)
        sortedresults=sortedresults[0:2]
        points=sum(sortedresults)
    else:
        points=0
    return points

#2 pairs
def twopairs(gameDice):
    results=[]
    #Sort the values of the dice. Compare two dice together from the top. If they are the same, remove them from gameDice and put them into results list. 
    for i in range(3):
        values=[]
        for dice in gameDice:
            dice.roll()
            values.append(dice.returnNo())
        sortedvalues=sorted(values,reverse=True)
        for i in range(len(sortedvalues)-1):
            if sortedvalues[i]==sortedvalues[i+1]:
                results.extend(sortedvalues[i:i+2])
                gameDice=gameDice[:-2] #everything except the two last elements. 
                break
    
    print(sortedvalues)
    print(results)

# 3 of a kind, 4 of a kind, Low straight, High Straight, Full House, Chance, Yatzy/Yahtsee

def yatzy():
    #create a list of five dice, all are set to value 1. 
    gameDice = [Die(),Die(),Die(),Die(),Die()]

    #First game:
    ones=upperSection(gameDice,1)
    print(ones)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #One pair:
    onePair=onepair(gameDice)
    print(onePair)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #Two pairs:
    #twopairs(gameDice)
    #gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 


yatzy()