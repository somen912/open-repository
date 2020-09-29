import random
import time
global system_score
global user_score

system_score=0
user_score=0


print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    Welcome to   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   Rock, Paper, Sissor   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   Game  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")


def randumgen():
    ''' This is a function to generate random choice from the system '''

    lst=['rock','paper','sissor']
    choice= random.choice(lst)
    return choice

def user_choice(choice):
    ''' This function prints user choice '''
    if choice==1:
        print("You took: rock ")
    elif choice==2:
        print("You took: paper ")
    elif choice==3:
        print("You took: sissor ")
    else:
        print("Invalid choice....")

def result(choice, system_choice):
    ''' This function is to show results '''
    global system_score
    global user_score


    if choice==1 and system_choice=='rock':
        print("********** Game is Tie *********\n")

    elif choice==1 and system_choice=='paper':
        print("********** System Won *********\n")
        system_score+=1
    elif choice==1 and system_choice=='sissor':
        print("********** You Won *********\n")
        user_score+=1
    elif choice==2 and system_choice=='paper':
        print("********** Game is Tie *********\n")

    elif choice==2 and system_choice=='rock':
        print("********** You Won *********\n")
        user_score+=1
    elif choice==2 and system_choice=='sissor':
        print("********** System Won *********\n")
        system_score+=1
    elif choice==3 and system_choice=='sissor':
        print("********** Game is Tie *********\n")

    elif choice==3 and system_choice=='paper':
        print("********** You Won *********\n")
        user_score+=1
    elif choice==3 and system_choice=='rock':
        print("********** System won *********\n")
        system_score+=1
    else:
        print("No result\n")

    if system_score>user_score:
        return system_score
    else:
        return user_score





######################## main program #####################

for i in range(0,3):

    print("What you want to select 1, 2 or 3?\n1.) rock\n2.) paper\n3.) sissor\n")
    choice=int(input("\nEnter your choice 1, 2 or 3: "))
    print("\n")
    user_choice(choice)

    system_choice=randumgen()
    print("System took: ",system_choice,"\n")


    score=result(choice,system_choice)
    print("system score is",system_score)
    print("your score is",user_score)
    print("\n\n\n\n----------------------------------TRY AGAIN--------------------------------------------\n")
    time.sleep(5)

print("          *************** SCORE CARD ***************            ")
if system_score>user_score:
    print(f"system score is :{system_score}\nyour score is :  {user_score}\n\n ### The system won ###\n ")
elif system_score<user_score:
    print(f"system score is :{system_score}\nyour score is :  {user_score}\n\n ### you won ###\n ")
else:
    print(f"system score is :{system_score}\nyour score is :  {user_score}\n\n ### Game is Tie ###\n ")

print("###########################################   GAME OVER    ###################################################\n")
