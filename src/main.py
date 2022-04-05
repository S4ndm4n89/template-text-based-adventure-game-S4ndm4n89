from threading import Timer
from time import sleep
def main():
        
    print("Welcome to the Game")

    PlayerName=input("what is your name? ")
    print(f"Hello " + PlayerName)

    lives = 3
    sleep(2)
    print(f"You have {lives } Remaining lives")

    backpack = [] # initialise empty list for backpack
    sleep(2)    
    print("you awake in a room to your front is a Blue door, to your right is a Red door, to left is a Green door and behind you there is a Black Door.") 
    sleep(4)
    print("On the floor in front of you, there is a note ! it reads:")
    sleep(4) 
    print("\n welcome to My game, you need to complete four puzzles and collect there Key to escape. Be aware of hidden threats! ") 
    sleep (4)    
    print("Upon looking around this central room again you find a backpack and put it on")
    sleep(2)
    print("\n you also notice door like shape in the corner of the room, it has four key like wholes init. ")  
    sleep(2)    
    while True:
        Colour = input("\n Which room do you want to try? please choice from Red, Blue, Green or Black. ").lower().strip()    

        if Colour == "red":
                room_colour = "Red"
                puzzle = " what is 2 + 2?"
                puzzle_solution = "4"
                key_number = "1"
                lives = in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number)
               
        elif Colour == "blue":
                room_colour = "Blue"
                puzzle = " what is the value of this binary 10100 ?"
                puzzle_solution = "20"
                key_number = "2"
                lives = in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number)

        elif Colour == "green":
                room_colour = "Green"
                puzzle = " what is 2*8  ?"
                puzzle_solution = "16"
                key_number = "3"
                lives = in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number)

        
        elif Colour == "black": 
                room_colour = "Black"
                puzzle = " what is the value of this binary 1100100 ?"
                puzzle_solution = "100"
                key_number = "4"
                lives = in_room(backpack,lives, room_colour, puzzle, puzzle_solution, key_number)

        else:
                print("Room colour not Recognised!")   

        #if back pack is full, open door and win game.
        if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("key 4" in backpack):
                print(" you input the four keys into the strange door in the corner, it open and you see the outside, you run for freedom\n you escape! game over!!  ") 
                exit()

        if lives == 0:
                print(" Your dead!\n please restart")
                exit()

def in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number):
        print(f"you have entered the {room_colour} room. A timer Starts you have 20 sec to solve the puzzle")
        puzzle_guess = input(puzzle)
     # Implement input timer
        time_limit = 20

        timeout_container = [False]
        lives_container = [lives]
        t = Timer(time_limit, check_time_out, args=(lives_container,timeout_container,))
        t.start()
        print(f"You have {time_limit} seconds to choose the correct answer...\n")
        puzzle_guess = input(puzzle)
        t.cancel()
        lives = lives_container[0]
        timeout = timeout_container[0]

        if not timeout:
                if puzzle_guess == puzzle_solution:
                        if f"Key {key_number}" not in backpack:
                                print(f"Correct. Key {key_number} collected.")
                                backpack.append(f"Key {key_number}")
                        else:
                                print("You have already collected this key!")
                else:
                        lives -= 1
                        print(f"Incorrect. You have {lives} lives remaining.")

        return lives

def check_time_out(lives_container,timeout_container):
        lives_container[0] -= 1
        print(f"Time out! You have {lives_container[0]} lives remaining. Press Enter to continue.")
        timeout_container[0] = True
        return lives_container, timeout_container
 

#def addition(a,b):
        return a+b+5
#test need test_......
#def test_addition():
        assert addition(3,5) == 8
        assert addition(-1,0) ==-1
        assert addition(-1,1) == 0

#def test_in_room():#test what happen when answer is wrong.

        backpack =[]
        lives = 3
        room_colour = "Black"
        puzzle = "what is 6 + 8?"
        puzzle_solution = "13"
        key_number = "4"

        #assert in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number) == 2 #lives-1

        #check corret
        assert in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number) == 3 #lives =
        assert f"key {key_number}" in backpack #check that this key is in backpack

        in_room(backpack,lives,room_colour,puzzle,puzzle_solution,key_number)
        assert backpack !=["key 4, key 4"]
      

if __name__ == "__main__":
        main()
        #value = addition(3,2)
        #print(value)
        #test_addition()
        #test_in_room()
        #









        
