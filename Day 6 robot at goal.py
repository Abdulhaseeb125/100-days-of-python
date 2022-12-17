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
