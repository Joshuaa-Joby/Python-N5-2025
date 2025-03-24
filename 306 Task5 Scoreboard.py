print("x ends the session ")
print("h adds a score to home team")
print("a adds a score to away team")
home = 0
away = 0
period = 1
while period < 4:
    key = input("enter one of the following keys: h,a,x:")
    if  key == "x":
            print("home team: ",home)
            print("away team: ",away)
            print("period ",period)
            period = period + 1

    elif key == "h":
        home = home + 1
        print("home team: ",home)
        print("away team: ",away)
        print("period ",period)
   
    elif key == "a":
        away = away + 1
        print("home team: ",home)
        print("away team: ",away)
        print("period ",period)
 
print("final score")
print("home team: ",home)
print("away team: ",away)
print("period ",period)
print("game over")
            