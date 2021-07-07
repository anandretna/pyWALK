cmd="heh"
n=0
m=0
while cmd.lower() != "quit":
    cmd=input(">")
    if cmd.lower()=="help":
        print(">start      --- start walking")
        print(">stop       --- stop walking")
        print(">left       --- turn left")
        print(">right      --- turn right")
        print(">climbtree  --- climb a tree")
        print(">climbhill  --- climb a hill")
        print(">throwstone --- throw a stone ")
        print(">climbdown  --- climb down ")
        print(">quit       --- quit walking")
    elif cmd.lower()=="start":
        if n==0:
            print("walking")
            n+=1
        else :
            print("already walking")
    elif cmd.lower() == "stop":
        if m == 0:
            print("stoped walking")
            m+=1
        else :
            print("still standing")
    elif cmd.lower() == "left":
        print("turning left")
    elif cmd.lower() == "right":
        print("turning right")
    elif cmd.lower() == "climbtree":
        print("climbing tree")
    elif cmd.lower() == "climbdown":
        print("climbed down")
    elif cmd.lower() == "climbhill":
        print("climbing hill")
    elif cmd.lower() == "throwstone":
        print("throwing a stone")
    elif cmd.lower() == "quit":
        print("thankyou for walking with me")
        break
    else :
        print("oops wrong command try>help ")