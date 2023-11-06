"""functions that will diaplay when called in main.py or other files"""
#import menufunctions
from asyncio import events
import sys



def displaymenu():
    #this function will display the menu to user
    print("       SUMMER HOLIDAY CAMP! ")
    
    print("Type or speak to choose number from the menu")
    print("If you want to choose to answer with audio choose 0 ")
    print("**********************************************************")

    print("0)--> To answer with audio ")
    print("1)--> To put the maximum amount of children that will be registered ")
    print("2)--> To register childs name ")
    print("3)--> To register children that can swim ")
    print("4)--> to register children with allergies ")
    print("5)--> To register children that can wet the bed ")
    print("6)--> To register children that will attend other ”events”")
    print("7)--> To register children that want or already have badges ")

    
    print("8.-->  To quit the program!")
    print("**********************************************************")

def childsname():
    asking_4_name =input("What your childs name? ")

    input("Press Enter to continue .... ")
    



 
def maximum_num():
    #This function requests for child name and counts the maximum of children tha can be registered 
    num_of_kids = []
    #num_of_kids = num_of_kids[:30]
    the_maximun_amount = int(input("what is the maximum number of kids attending? "))
    #childsname = input("Enter the child's name: ")
    the_sum = len(num_of_kids) #count the lenght of the list
    if the_sum <= the_maximun_amount: #as long as the sum of the list doesn't exceed the users wish
        num_of_kids.append(childsname()) #add childs name to the list.
        new_sum = len(num_of_kids)
        print(f"{childsname()} has been registered ")
        print(f"There are {new_sum} number of kids registered and the maximum is {the_maximun_amount}")
    else:
        print("Sorry Summer holiday camp tickets are outsold")
    input("Press Enter to continue .... ")



def yes_or_no(the_question):
    
    if the_question == "yes":
        addtoyeslist = []
        addtoyeslist.append(the_question)
        print("you answered yes ")

    elif the_question == "no":
        addtonolist = []
        addtonolist.append(the_question)
        print("you answered no ")
    else:
        raise ValueError 
        print("Wrong answer! Try answering wit yes or no ")
    input("Press Enter to continue .... ")



def swimmer():
    can_swim= input("Can the child swim? answer yes or no: ")
    if can_swim == "yes":
        swimmerslist = []
        swimmerslist.append(can_swim)
        print("Child has been added to swimmers list")

    elif can_swim == "no":
        cantswimlist = []
        cantswimlist.append(can_swim)
        print("child won't attend swimming events")
    else:
        print("Wrong answer! Try answering wit yes or no: ")
    input("Press Enter to continue .... ")



def favoritemeal():
    meal_list =[]
    meal =input("Whats childs favorite food ")
    meal_list.append(meal)
    print(f"{meal} has been registered as favorite meal")
    input("Press Enter to continue .... ")



def Allergic():
   is_allergic = input("Is the child allergic? say yes or no: ")
   yes_or_no(is_allergic)

    

def Bedwetters():
    is_bedwetter = input("Do they bedwet? ")
    yes_or_no(is_bedwetter)
    input("Press Enter to continue .... ")

def morethan1event():
    attending =input("what other events will the child attend?: ")
    theevents =[]
    theevents.extend(attending)
    print(f"{attending} event has been registered")

    input("Press Enter to continue .... ")


def badges():
    haveabadge = input("Do the child have a badge?: ")
    if haveabadge == "No":
        print("Child will be given a badge")
    else:
        print("Child already has a badge")


def Endprogram():
    print("Bye bye You quit the program")
    sys.exit()

    


