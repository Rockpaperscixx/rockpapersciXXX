from tkinter import *
import random
root=Tk()
var=StringVar()
def donothing1(event):
    donothing_1(event)
def donothing2(event):
    donothing_2(event)
def donothing3(event):
    donothing_3(event)
frame1=Frame(root,width="300",height="300", bg="green")
frame1.pack()
frame1.pack_propagate(0)
frame2=Frame(frame1, bg="Black")
frame2.pack(side="bottom",fill=X)
label2=Label(frame2, height="3", textvariable= var, fg="white", bg="Black")
label2.pack()
var.set("asdhgahusdghjags")
label1=Label(frame1, text="Choose your weapon against computer, choose well!!:- ", fg="yellow",bg="green")
label1.pack(side="top")
Rock=Button(frame1,text="ROCK",fg="RED", width="5", height="2")
Paper=Button(frame1,text="Paper",fg="RED", width="5", height="2")
Scissor=Button(frame1,text="Scissor",fg="RED", width="5", height="2")
Rock.pack(side="left")
Paper.pack(side="right")
Scissor.pack(side="top")
Rock.bind('<Button-1>', donothing1)
Paper.bind('<Button-1>', donothing2)
Scissor.bind('<Button-1>', donothing3)
def donothing_1(event):
    var.set("this is a test")
    choice=1
    getresult(choice)
def donothing_2(event):
    var.set("this is a test")
    choice=2
    getresult(choice)
def donothing_3(event):
    var.set("this is a test")
    choice=3
    getresult(choice)
def getresult(choice):
    human_points=0
    comp_points =0
    msg=""
    weapon_of_choice={1:'Rock',2: 'Paper', 3: 'Scissor'}
    if (human_points <5 and comp_points <5):        
        humanchoice=weapon_of_choice.get(int(choice),"never")
        compchoice= weapon_of_choice.get(random.randint(1,3),"never")
        if(humanchoice=='Rock' and compchoice=='Paper'):
            comp_points+=1
            msg="Point by computer"
        elif(humanchoice=='Paper'and compchoice=='Scissor'):
            comp_points+=1
            msg="Point by computer"
        elif(humanchoice=='Scissor' and compchoice=='Rock'):
            comp_points+=1
            msg="Point by computer"
        elif(humanchoice=='Rock'and compchoice=='Scissor'):
            human_points+=1
            msg="Point by Human"
        elif(humanchoice=='Paper'and compchoice=='Rock'):
            human_points+=1
            msg="Point by Human"
        elif(humanchoice=='Scissor' and compchoice=='Paper'):
            human_points+=1
            msg="Point by Human"
        else:
            msg="It is the same"
    if(human_points==1):
        var.set("Human WON !!\n   "+msg+"\n  "+humanchoice+"+"+compchoice+"  "+str(human_points)+" "+ str(comp_points))
    elif(human_points==0 and comp_points==0):
        var.set("Draw !!\n   "+msg+"\n  "+humanchoice+"+"+compchoice+"  "+str(human_points)+" "+ str(comp_points))
    else:
        var.set("Human LOST !!\n   "+msg+"\n  "+humanchoice+"+"+compchoice+"  "+str(human_points)+" "+ str(comp_points))
root.mainloop()

