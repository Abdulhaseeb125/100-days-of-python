#Note there are not the fastest codes because these are written on self thaughts not on guided these can be improved by thinking more for a while.
#written by abdul haseeb

#website link...
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
  
#coide for hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def wif():
        turn_left()
        move()
        turn_right()
 
while not at_goal():
    if at_goal():
        break
    elif front_is_clear() and wall_on_right():
        while front_is_clear():
            move()
    elif wall_in_front():
        while wall_in_front():
            wif()
        move()
    elif not wall_on_right():
        turn_right()
        while front_is_clear():
            move()
        turn_left()

        
# Maze code:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
       
        
def turn_around():
    for i in range(0,3):
        turn_left()

while not at_goal():
    if front_is_clear():
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
    elif wall_in_front():
        while wall_in_front() and  not wall_on_right():
            turn_right()
        while wall_in_front() and wall_on_right():
            turn_left()
