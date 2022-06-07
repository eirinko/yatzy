from hand import Hand

def manyOfOne(number):
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
    for i in range(3):
        rollinghand.rolls()
        for dice in rollinghand:
            if dice==number:
                resulthand.append(dice)
                rollinghand.remove(dice)
    return resulthand

def xofakind(number): #Five of a kind would be yahtsee
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
    for i in range(3):
        rollinghand.rolls()
        
        print(rollinghand)
        #print(set(rollinghand))
        if len(set(rollinghand))==1:
            print("Yahtsee!")

    return resulthand    

def onepair(gameDice):
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])

def twopairs(gameDice):
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])

def threeofakind(gameDice):
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def fourofakind():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def lowstraight():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def highstraight():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def fullhouse():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def chance():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def yahtsee():
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
def yatzy():
    ones=manyOfOne(1)
    twos=manyOfOne(2)
    threes=manyOfOne(3)
    fours=manyOfOne(4)
    fives=manyOfOne(5)
    sixes=manyOfOne(6)
    points=sum(ones)+sum(twos)+sum(threes)+sum(fours)+sum(fives)+sum(sixes)
    if points>=50:
        points+=50
    print(points)
    xofakind(2)

if __name__ == "__main__": #This will not be run if yatzygames gets imported to another file. 
    yatzy()
    
