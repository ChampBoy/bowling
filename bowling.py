# Written by paraw001
## Import Statements
import random, turtle, time


def main():
    turtle.speed(0)
    turtle.penup()
    existence=[1,1,1,1,1,1,1,1,1,1] #  0 = Pin not present at location, 1 = Pin exists at location
    pinlist=[]
    frame=0 
    printer(existence) #Printing initial frame


    while frame<10: #While will run 10 times for 10 frames
        topple_pins(frame,pinlist)
        frame+=1
        
    turtle.color('red')
    turtle.goto(-50,-50)
    total_score=finalScore(pinlist) #Sending final score list to score calculator function
    turtle.write("Final Score: " + str(total_score),font=("Arial", 14, "normal"))

def topple_pins(frame,pinlist): #Takes input from user 2 times for each frame and prints statement depending on 
    score_roll1=0               # remaining number of pins
    score_roll2=0
    roll_no=0
    r=0
    existence=[1,1,1,1,1,1,1,1,1,1]
    
    while roll_no<2:
        user_input=turtle.textinput('Frame '+ str(frame+1),'Enter # of Pins (null for random) ')
        existence=number_to_knock(user_input,existence) 
        turtle.clear()
        printer(existence)
        
        if check_remaining(existence)!=0 and roll_no==0:
            turtle.goto(-50,-50)
            turtle.color('red')
            turtle.write("Open Frame: " + str(10-check_remaining(existence)),font=("Arial", 14, "normal"))
        
        if check_remaining(existence)==0 and roll_no==0:
            turtle.goto(-15,-50)
            turtle.color('red')
            turtle.write("Strike " ,font=("Arial", 14, "normal"))
            score_roll1=10
            roll_no +=3
            strike_counter=1
        
        elif check_remaining(existence)==0 and roll_no==1:
            turtle.goto(-15,-50)
            turtle.color('red')
            turtle.write("Spare " ,font=("Arial", 14, "normal"))
            spare_counter=1
        
        if roll_no==0:
            score_roll1=10-check_remaining(existence)
            rold=check_remaining(existence)
        
        if roll_no==1:
            score_roll2=rold-check_remaining(existence)
        
        roll_no+=1
    
    #Now we add scores to a list
    
    if roll_no==3:
        pinlist.append(score_roll1)
    
    elif score_roll1==10:
        pinlist.append(score_roll1)
    
    else:
        pinlist.append(score_roll1)
        pinlist.append(score_roll2)
    
    time.sleep(2)
    turtle.clear()
    existence=[1,1,1,1,1,1,1,1,1,1] #Resetting the pin board

    if frame==9: # If condition is needed as last frame has a different case (2 or 3 shots)
        if pinlist[len(pinlist)-1]==10: # To check if the first shot is a strike
            i=0
            turtle.clear()
            printer(existence)
            while i<2: #Will take 2 more shots if first was strike
                user_input=turtle.textinput('Frame '+ str(frame+1),'Enter # of Pins (null for random) ')
                existence=number_to_knock(user_input,existence)

                if i==0:
                    pinlist.append(10-check_remaining(existence))
                    rold=check_remaining(existence)
                    turtle.clear()
                    printer(existence)

                if i==1 and rold!=0:
                    pinlist.append(rold-check_remaining(existence))
                    turtle.clear()
                    printer(existence)

                elif i==1:
                    pinlist.append(10-check_remaining(existence))
                    turtle.clear()
                    printer(existence)

                if check_remaining(existence)==0 and i==0: # If there is another strike we would need to reset game
                    existence=[1,1,1,1,1,1,1,1,1,1]
                    turtle.goto(-15,-50)
                    turtle.color('red')
                    turtle.write("Strike " ,font=("Arial", 14, "normal"))
                    time.sleep(2)
                    turtle.clear()
                    printer(existence)             
                i += 1             

        elif pinlist[len(pinlist)-1]+pinlist[len(pinlist)-2]==10: #Checking for Spare
            printer(existence)
            user_input=turtle.textinput('Frame '+ str(frame+1),'Enter # of Pins (null for random) ')
            existence=number_to_knock(user_input,existence)
            turtle.clear()
            printer(existence)
            pinlist.append(10-check_remaining(existence))

    printer(existence)

def number_to_knock(user_input,existence): #Function to decide how many pins would be knocked
    if user_input=='':
        existence=knockpins(existence,random.randint(0,check_remaining(existence)))
    
    elif int(user_input)<=check_remaining(existence):
        existence=knockpins(existence,int(user_input))
    
    else:
        existence=[0,0,0,0,0,0,0,0,0,0]
    
    return existence

def finalScore(pinlist):#Function to calculate final score
    total_score=0
    i=0
    strike_counter=0
    last_frame=0
    
    while i<len(pinlist):
        if i==len(pinlist)-1 or i==len(pinlist)-2 or i==len(pinlist)-3:
            last_frame=1 #Last frame has arrived
    
        if pinlist[i]==10 and last_frame==0:
            total_score+=10+pinlist[i+1]+pinlist[i+2]
            i=i+1
            strike_counter+=1
    
        elif last_frame==0 and (i+strike_counter)%2==0 and pinlist[i]+pinlist[i+1]==10:
            total_score+=10+pinlist[i+2]
            i=i+2
    
        else:
            total_score+=pinlist[i]
            i=i+1
    
    return total_score


def knockpins(existence,n):#Function to knock pins according to user inputs
    
    for x in range(n):
        a=random.randint(0,check_remaining(existence)-1)
        counter=-1
    
        for y in range(len(existence)):
            if existence[y]==1:
                counter+=1
            if counter==a:
                existence[y]=0
    
    return existence

def check_remaining(existence): #Function to check if a pin is still remaining at a location
    counter=0
    
    for y in range(len(existence)):
        if existence[y]==1:
            counter+=1
    
    return counter

def printer(existence): #Function to print pins using turtle if they exist
    location_pin=[(75,50),(100,100),(50,100),(125,150),(75,150),(25,150),(150,200),(100,200),(50,200),(0,200)]

    for x in range(len(location_pin)):
        if existence[x]==1:
            turtle.color('blue')
            turtle.shape('circle')
            turtle.goto(location_pin[x][0]-75,location_pin[x][1]-50)
            turtle.stamp()
        else:
            turtle.goto(location_pin[x][0]-75,location_pin[x][1]-50)
            turtle.color('black')
            turtle.write('X',font=("Arial",8,"bold"))
        turtle.hideturtle()  

    
if __name__=='__main__':
    main()
