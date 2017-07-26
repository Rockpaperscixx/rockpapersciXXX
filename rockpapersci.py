import random
class game:
    human_points=0
    comp_points =0
    weapon_of_choice={1:'Rock',2: 'Paper', 3: 'Scissor'}
    while (human_points <5 and comp_points <5): 
        choice=input("enter the choice of your weapon\n Rock - (1)\n Paper - (2)\n scissor - (3)")
        humanchoice=weapon_of_choice.get(int(choice),"never")
        compchoice= weapon_of_choice.get(random.randint(1,3),"never")
        if(humanchoice=='Rock' and compchoice=='Paper'):
            comp_points+=1
            print("Point by computer")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        elif(humanchoice=='Paper'and compchoice=='Scissor'):
            comp_points+=1
            print("Point by computer")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        elif(humanchoice=='Scissor' and compchoice=='Rock'):
            comp_points+=1
            print("Point by computer")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        elif(humanchoice=='Rock'and compchoice=='Scissor'):
            human_points+=1
            print("Point by Human")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        elif(humanchoice=='Paper'and compchoice=='Rock'):
            human_points+=1
            print("Point by Human")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        elif(humanchoice=='Scissor' and compchoice=='Paper'):
            human_points+=1
            print("Point by Human")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
        else:
            print("It is the same")
            print("Human:- "+ humanchoice +"+ computer:-"+ compchoice)
            print(human_points,comp_points)
    if(human_points==5):
        print("Human WON !!")
    else:
        print("Human LOST !!")
