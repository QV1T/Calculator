# first = input("What is the first number")
# second = input("What is the second number")
# functionType = input("What function would you like to perform?")
# def step1(first,second):
#     answer = int(first) + int(second)
#     print(answer)
    
def step2(first,second,functionType):
    if functionType == "add" or functionType == "addition":
        answer = int(first) + int(second)
        print(str(answer))
    elif functionType == "minus" or functionType == "subtraction":
        answer = int(first) - int(second)
        print(str(answer))
    elif functionType == "times" or functionType == "multiply":
        answer = int(first) * int(second)
        print(str(answer))
    elif functionType == "divide":
        answer = int(first) / int(second)
        print(str(answer))

step2(5,6,"times")

def horoscopeCalc(BirthMonth):
    BirthMonth = int(BirthMonth)
    if BirthMonth   == 0:
        print("Your zodiac animal is the unicorn. You are full of optimism, smiles, and rainbows! You are social and make friends wherever you go! You don’t often feel sad.")
    if BirthMonth   == 1:
        print("Your zodiac animal is the phoenix. You are very determined in accomplishing things. Your fiery spirit is unbeatable, and once you set your mind to things you are unstoppable.")
        #rooster
    if BirthMonth   == 2:
        print("Your zodiac animal is the ant. You are tiny and easily squished. You toil away in obscurity. No one cares about you, as there are many of you in your colony.")
        #dog
    if BirthMonth   == 3:
        print("Your zodiac animal is the beetle. You are disgusting. Everyone hates you. You are easily squished.")
        #pig
    if BirthMonth   == 11:
        print("Your zodiac animal is the turtle. Mostly introverted, you prefer to work alone. You cower to those that intimidate you, and prefer not to participate in most activities.")
        #rat
    if BirthMonth   == 5:
        print("Your zodiac animal is the orca. You are ferocious when angered, and have a cold appearance, but are warm on the inside.")
        #ox
    if BirthMonth   == 9:
        print("Your zodiac animal is the chipmunk. You are vermin. You are easily missed. Everyday is a struggle for you but no one cares.")
        #tiger
    if BirthMonth   == 7:
        print("Your zodiac animal is the human. You are evil. You do not care about your inferiors or your superiors.")
        #rabbit
    if BirthMonth   == 8:
        print("Your zodiac animal is the pterodactyl. You are full of energy. You easily can dodge any pessimism and prefer to be in places in the sky.")
        #dragon
    if BirthMonth   == 6:
        print("Your zodiac animal is komodo dragon. You are easily outraged by people and prefer to be alone, or with people that are also Komodo dragons.")
        #snake
    if BirthMonth   == 10:
        print("Your zodiac animal is the dodo bird. You are useless and about to go extinct.")
        #horse
    if BirthMonth   == 4:
        print("Your zodiac animal is the aphid. You are so weak, even ants can beat you up.")
        #goat
horoscopeCalc(int(input("What month were you born(in numbers)")))


def FutureByYear(year):
    if year % 2 == 0:
        print("In " + str(year) + ", you will be dead")
    elif year % 5 == 0:
        print("In " + str(year) + ", you will suffer from an serious illness")
    elif year % 3 == 0:
        print("In " + str(year) + ", you will regret the choices that you made today.")
    elif year % 7 == 0:
        print("In " + str(year) + ", you will be married to a rock.")
    elif year % 2 == 1:
        print("In " + str(year) + ", you will be a carpet that people step on.")

FutureByYear(int(input("For what year do you want to know your fortune")))

        
