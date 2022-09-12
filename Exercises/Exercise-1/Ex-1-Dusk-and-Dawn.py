# Dawn and Dusk - An Illutration of the Cycle of Day and Night conveyed through a single RGB LED
# Armaan Agrawal
# 2022-09-11

import board
import time
import neopixel


# got this function from stackoverflow
# link: https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length
def zip_longest(*lists):
    def g(l):
        for item in l:
            yield item
        while True:
            yield "foo"
    gens = [g(l) for l in lists]
    for _ in range(max(map(len, lists))):
        yield tuple(next(g) for g in gens)

# using this code to create the LED Object for the onboard NEOPIXEL LED
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1.0

# initiliazing the main r,g,b tuple
colorTuple = (0,0,0)


# built a fade function to allow for a smooth change of colors through different gradients
# the principle behind this function is that it accepts two tuples and subtracts each of their i,j,k values and incrementally scales all components of the first tuple to the second tuple simultaneously
def fade(tup1,tup2):
    a1 = tup1[0] - tup2[0]
    a2 = tup1[1] - tup2[1]
    a3 = tup1[2] - tup2[2]

    # it is essential to replace the "foo" with the highest value for the particular component: ie. the absolute value of the difference between the first and second tuple for that component

    for i,j,k in zip_longest(range(0,abs(a1)+1),range(0,abs(a2)+1),range(0,abs(a3)+1)):
        if i == "foo":
            i = abs(a1)
        if j == "foo":
            j = abs(a2)
        if k == "foo":
            k = abs(a3)

        if a1 > 0:
            a = tup1[0]-i
        else:
            a = tup1[0]+i
        if a2 > 0:
            b = tup1[1]-j
        else:
            b = tup1[1]+j
        if a3 > 0:
            c = tup1[2]-k
        else:
            c = tup1[2]+k

        led[0] = (a,b,c)
        time.sleep(0.05)


# loopAgain gives the player the choice to interact with the installation once more
# TimeToLED maps out each hour to its specific rgb color
loopAgain = True
TimeToLED = {
            0: (39,37,86),
            1: (73,68,132),
            2: (102,72,126),
            3: (142,85,130),
            4: (190,94,132),
            5: (227,93,118),
            6: (255,77,0),
            7: (255,103,0),
            8: (255,129,0),
            9: (255,167,0),
            10: (253,230,124),
            11: (255,197,13),
            12: (251,190,0),
            13: (255,180,2),
            14: (253,168,5),
            15: (253,150,22),
            16: (255,141,0),
            17: (255,129,0),
            18: (255,103,0),
            19: (255,77,0),
            20: (75,61,96),
            21: (21,40,82),
            22: (8,24,58),
            23: (0,0,0)
        }

while loopAgain:
    print("Welcome to the Dawn to Dusk show!")
    showType = input("""
            What mode would you like to see today:
                1) Automatic
                2) Manual
            """
        )
    # in the automatic loop, the sequence from night to day is shown with colors fading into one another
    if int(showType) == 1:
        AutomaticLoop = True
        while AutomaticLoop:
            for i in range(0,23):
                tuple_1 = TimeToLED.get(i)
                tuple_2 = TimeToLED.get(i+1)
                fade(tuple_1,tuple_2)
            AutomaticLoop = int(input("Do you want to see the automatic mode again? Enter 0 for no and 1 for yes.\n"))

    # in the manual loop, viewers can choose the time of the day to see what color the sky is in that particular hour
    elif int(showType) == 2:
        ManualLoop = True


        while ManualLoop:
            timeOfDay = int(input("What is the time of the day? (Enter a number between and including 0 and 23)\n"))
            if timeOfDay not in range(0,24):
                print("Please enter a valid number between 0 and 23.\n")
                timeOfDay = input("What is the time of the day? (Enter a number between and including 0 and 23)\n")

            colorTuple = TimeToLED.get(timeOfDay)
            led[0] = colorTuple
            time.sleep(1.25)
            ManualLoop = int(input("Do you want to enter a different number? Enter 0 for no and 1 for yes.\n"))

    # error checking (assuming only numbers are entered)


    else:
        print("Please enter either 1 or 2.\n")
        continue

    loopAgain = int(input("Do you want to see the show again? Enter 0 for no and 1 for yes.\n"))


