import os

import functions
import menufunctions


while True:
    # Clear the screen
    os.system("clear")
    functions.displaymenu()
    
    
    
    choice = str(input("Choose numbers from the menu so we get to work! -->  "))
    menufunctions.get_audio()

    
      

    if choice == "1":
        functions.maximum_num()
    
    elif choice == "2":
        functions.childsname()

    elif choice =="3":
        functions.swimmer()
    elif choice =="4":
        functions.Allergic()
    elif choice == "5":
        functions.Bedwetters()
    elif choice == "6":
        functions.morethan1event()
    elif choice =="7":
        functions.badges()
    elif choice =="8":
        functions.Endprogram()
