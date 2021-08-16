from ai import AI
from human import Human
import random


Cchoice=["rock","paper","scissors","lizard","spock"]
while True:
    
    youwin,computerwin=0,0
    for i in range(1,6):
            print('this is a basic game of rock paper scissors,with a twist!')
            print('this version includes two extra choices lizard and Spock')
            print("Round",1, "Start:")
            print("Please select any one option:")
            print("1.Rock","2.Paper","3.Scissors", "4.lizard","5.Spock",sep="\n")
            Yourchoice=int(input())
            if Yourchoice==1:
                print("You select Rock")
                Yourchoice="Rock"
            elif Yourchoice==2:
                print("You select paper")
            elif Yourchoice==3:
                print("You select scissors")
            elif Yourchoice==4:
                print("You select Lizard")
            elif Yourchoice==5:
                print("You Seelect Spock")
            else:
                 print("Invalid Choice")
                 break
            Computerchoice=random.choice(Cchoice)
            print("computer select:", Computerchoice)
        

            if Yourchoice==Computerchoice:
                    youwin+=1
                    computerwin+=1
                    print("this Round Is a Tie:")
            elif (Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissors") or(Yourchoice=="Scissors" and Computerchoice=="Paper"):
                (Yourchoice=="lizard" and Computerchoice=="paper") or (Yourchoice=="Rock" and Computerchoice=="lizard") or (Yourchoice=="Scissors"and Computerchoice=="lizard")  
                (Yourchoice=="Spock"and Computerchoice=="lizard") or (Yourchoice=="rock" and Computerchoice=="Spock") or (Yourchoice=="Paper"and Computerchoice=="Spock")
                youwin+1
                print("You win this Round")
            else:
                    computerwin+1
                    print("Computer win this Round")



            if youwin>computerwin:
                print("You win the game") 
                print("Score is:", "Your score:",youwin,"Computer score:", computerwin,sep=" ")
            elif computerwin>youwin:
                print("You Lose the game. Computer win the game:")
                print("Score is:","Your score:", youwin, "Computer score:",computerwin,sep=" ")
            else:
               

                print("Score is:", "Your score:",youwin,",Computer score:",computerwin,sep=" ")
            user_choice=input("want to Play again?(Yes/Exit)")
            if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
                continue

            else:

                break

                



                

     
            
    




        
    
      

        
    #     print(f'Hello, {human_player_2}. ')
    #creating the actual 1 v 1, where we pit one player against the other
    # we will establish which esture beats waht and how that will make the winner gain points
    #


    
    

    
        
        
    # print(f'Hello, {computer_player_1}. ')

        
        
    
        
    

    

    
    

    
    
    
        
        
    
    
    
        





                
        
    
















