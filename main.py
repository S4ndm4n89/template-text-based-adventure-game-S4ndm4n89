
def main():
    print("Welcome to the Game")

    PlayerName=input("what is your name? ")
    print("Hello " + PlayerName)

    lives = 3
    print(f"You have {lives} Remaining lives")

    Backpack =[] # inititialise empty list for backpack

    while True:
        TravelDirection = input("which direction would you like to go ? please choose direction ( north, south, east or west) " )

        if TravelDirection == "north":
                print("you went north")
            # I,m trying to fail puzzules lose a life
                puzzle_guess_north =input("what if is 2+2 ?")
                if puzzle_guess_north == "4":
                        print("correct")
        # We need to collect somthing from the puzzule
                        Backpack.append("key1")

                else:
                        print("incorrect")
                        lives -= 1
                        print (f"You have {lives} remaining")

        elif TravelDirection == "south":
                print("you went south")
             # I,m trying to fail puzzules lose a life
                puzzle_guess_south =input("what if is 2*8 ?")
                if puzzle_guess_south == "16":
                        print("correct")
        # We need to collect somthing from the puzzule
                else:
                        print("incorrect")
                        lives -= 1
                        print (f"You have {lives} remaining")

        elif TravelDirection == "east":
                print("you when east")
             # I,m trying to fail puzzules lose a life
                puzzle_guess_east =input("what if is the value of this binary 10100 ?")
                if puzzle_guess_east == "20":
                        print("correct")
        # We need to collect somthing from the puzzule
                else:
                        print("incorrect")
                        lives -= 1
                        print (f"You have {lives} remaining")
        
        elif TravelDirection == "west":
                print("you went west")
    
        else:
                print("Sorry, not reconised.")

        #if back pack is full, open door and win game
        if("Key 1" in Backpack) and ()


        if lives == 0:
        print(" Your dead!\n please restart")
        exit()




main()
