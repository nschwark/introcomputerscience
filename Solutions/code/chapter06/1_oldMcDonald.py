def hadFarm():
    return "Old MacDonald had a farm, Ee-igh, Eeigh, Oh!\n"

def verseFor(animal):
    animalVerse = hadFarm() + "And on that farm he had a " + animal + ", Ee-igh, Eeigh, Oh!"
    return animalVerse

def animalSound(sound):
    soundVerse = "With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.\n" + "Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + "."
    return soundVerse

def main():
    
    x = 0

    for animal in ["cow", "pig", "horse", "duck", "dog"]:

        sounds = ["moo", "oink", "neh", "quack", "woof"]
        
        print(verseFor(animal))
        print(animalSound(sounds[x]))
        print(hadFarm())

        x = x + 1

main()