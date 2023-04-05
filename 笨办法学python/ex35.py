from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much <50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
        


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.") 
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:   #循环语句里面嵌套if语句；该while语句会一直循环下去，除非利用其他函数进行打断
        choice = input(">")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face.")  #利用dead()函数论里面的exit()函数来跳出while循环
        elif choice == "taunt bear" and not bear_moved:  #taunt:嘲讽
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True     #通过熊房间的步骤应该是先taunt嘲讽熊，然后再打开门
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            
            
def cthulhu_room():  #cthulhu:神棍
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
   
    choice = input(">")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):  #定义dead函数
    print(why,"Good job!")
    exit(0)   #作用应该是跳出while循环
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input(">")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()



     