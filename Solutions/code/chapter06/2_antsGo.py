def antsGo(number):
    return "The ants go marching " + number + " by " + number + ", hurrah! hurrah!\n"

def numByNum(number):
    return "The ants go marching " + number + " by " + number + ","

def littleOne(action):
    return "The little one stops to " + action + ","

def endVerse():
    return "And they all go marching down...\n" + "In the ground...\n" + \
        "To get out...\n" + "Of the rain.\n" + "Boom! Boom! Boom!"

def main():

    x = 0

    for number in ["one", "two"]:
        
        action = ["suck his thumb", "tie his shoe"]

        print(antsGo(number) * 2, end="")
        print(numByNum(number))
        print(littleOne(action[x]))
        print(endVerse())

        x = x + 1

main()