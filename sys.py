from var import HALFHEIGHT, HALFWIDTH
# MAKE THE GAME WORK  
"""
Precondition: Program ends
Postcondition: Prints in the console to define the end of the program.
"""
def program_end_screen():
    print("__________________________________________________________________")
    print("                         PROGRAM ENDED")
    print("__________________________________________________________________")

"""
Precondition: The program redirects the user to this function by the user's choice after adding a variety of items.
Postcondition: The program lists all of the items the user has given and their prices, along with the user's comission and how much the final outfit costed.
"""
def palbo_simulation_ending_calculation():
    global ph_present, pm_present, pw_present, pws_present, pb_present, pec_present, pt_present, pg_present, ph_price, pm_price, pw_price, pws_price, pb_price, pec_price, pt_price, pg_price
    psec_cost = 0
    print("__________________________________________________________________")
    print("You have sold the following items:")
    if ph_present == 1:
        psec_cost = psec_cost + ph_price
        print(f'A hat for ${ph_price}')
    if pm_present == 1:
        psec_cost = psec_cost + pm_price
        print(f'A monacle for ${pm_price}')
    if pw_present == 1:
        psec_cost = psec_cost + pw_price
        print(f'A watch for ${pw_price}')
    if pws_present == 1:
        psec_cost = psec_cost + pws_price
        print(f'A walking stick for ${pws_price}')
    if pb_present == 1:
        psec_cost = psec_cost + pb_price
        print(f'A body for ${pb_price}')
    if pec_present == 1:
        psec_cost = psec_cost + pec_price
        print(f'A family estate crest for ${pec_price}')
    if pt_present == 1:
        psec_cost = psec_cost + pt_price
        print(f'A tie for ${pt_price}')
    if pg_present == 1:
        psec_cost = psec_cost + pg_price
        print(f'Glasses for ${pg_price}')
    if psec_cost == 0 and pb_present == 0:
        print("Nothing")
    else:
        psec_comission = psec_cost * comission
    print(f"\nGreat job! Mr. Palbo is very appreciative of your work. From the sales of the items, Mr. Palbo has paid ${psec_cost} and you have earned ${psec_comission} from a commision rate of ${comission} per $1.")
    program_end_screen()

"""
Precondition: The program redirects the user to this function to add an additional item
Postcondition: The user will have successfully added another item and its visibility would have been updated.
"""
def palbo_cont_edit():
    global ph_present, pm_present, pw_present, pws_present, pb_present, pec_present, pt_present, pg_present
    ph_txt = "1. Hat"
    pm_txt = "2. Monacle"
    pw_txt = "3. Watch"
    pws_txt = "4. Walking Stick"
    pb_txt = "5. Body"
    pec_txt = "6. Palbo Family Estate Crest"
    pt_txt = "7. Tie"
    pg_txt = "8. Glasses"
    pcs_txt = ""
    if ph_present == 0:
        pcs_txt = pcs_txt + "\n" + ph_txt
    if pm_present == 0:
        pcs_txt = pcs_txt + "\n" + pm_txt
    if pw_present == 0:
        pcs_txt = pcs_txt + "\n" + pw_txt
    if pws_present == 0:
        pcs_txt = pcs_txt + "\n" + pws_txt
    if pb_present == 0:
        pcs_txt = pcs_txt + "\n" + pb_txt
    if pec_present == 0:
        pcs_txt = pcs_txt + "\n" + pec_txt
    if pt_present == 0:
        pcs_txt = pcs_txt + "\n" + pt_txt
    if pg_present == 0:
        pcs_txt = pcs_txt + "\n" + pg_txt
    pce_item = int(input(f'What other item would you like to add to Mr. Palbo?\n{pcs_txt}'))
    if pce_item == 1:
        if ph_present == 0:
            ph_present = 1
            palbo_hat()
            print("__________________________________________________________________")
            print("User has chosen to add a hat.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 2:
        if pm_present == 0:
            pm_present = 1
            palbo_monacle()
            print("__________________________________________________________________")
            print("User has chosen to add a monacle.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 3:
        if pw_present == 0:
            pw_present = 1
            palbo_watch()
            print("__________________________________________________________________")
            print("User has chosen to add a watch.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 4:
        if pws_present == 0:
            pws_present = 1
            palbo_walking_stick()
            print("__________________________________________________________________")
            print("User has chosen to add a walking stick.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 5:
        if pb_present == 0:
            pb_present = 1
            palbo_body()
            print("__________________________________________________________________")
            print("User has chosen to add a body.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 6:
        if pec_present == 0:
            pec_present = 1
            palbo_estate_crest()
            print("__________________________________________________________________")
            print("User has chosen to add the estate crest.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 7:
        if pt_present == 0:
            pt_present = 1
            palbo_tie()
            print("__________________________________________________________________")
            print("User has chosen to add a tie.")
            palbo_continue()
        else:
            palbo_cont_edit()
    elif pce_item == 8:
        if pg_present == 0:
            pg_present = 1
            palbo_glasses()
            print("__________________________________________________________________")
            print("User has chosen to add glasses.")
            palbo_continue()
        else:
            palbo_cont_edit()
    else:
        palbo_cont_edit()
    
"""
Precondition: The program has sent the user to this function to add their first item.
Postcondition: The user will have successfully added their first item of choice and its visibility has been updated.
"""
def palbo_edit_beginning():
    global ph_present, pm_present, pw_present, pws_present, pb_present, pec_present, pt_present, pg_present
    peb_item = int(input("Mr. Palbo wants to try out a new fit today. Chose which item you want to add to his fit.\n\n1. Hat\n2. Monacle\n3. Watch\n4. Walking Stick\n5. Body\n6. Palbo Family Estate Crest\n7. Tie\n8. Glasses"))
    if peb_item == 1:
        ph_present = 1
        palbo_hat()
        print("__________________________________________________________________")
        print("User has chosen to add a hat.")
    elif peb_item == 2:
        pm_present = 1
        palbo_monacle()
        print("__________________________________________________________________")
        print("User has chosen to add a monacle.")
    elif peb_item == 3:
        pw_present = 1
        palbo_watch()
        print("__________________________________________________________________")
        print("User has chosen to add a watch.")
    elif peb_item == 4:
        pws_present = 1
        palbo_walking_stick()
        print("__________________________________________________________________")
        print("User has chosen to add a walking stick.")
    elif peb_item == 5:
        pb_present = 1
        palbo_body()
        print("__________________________________________________________________")
        print("User has chosen to add the body.")
    elif peb_item == 6:
        pec_present = 1
        palbo_estate_crest()
        print("__________________________________________________________________")
        print("User has chosen to add the estate crest.")
    elif peb_item == 7:
        pt_present = 1
        palbo_tie()
        print("__________________________________________________________________")
        print("User has chosen to add a tie.")
    elif peb_item == 8:
        pg_present = 1
        palbo_glasses()
        print("__________________________________________________________________")
        print("User has chosen to add glasses.")
    else:
        palbo_edit_beginning()

"""
Precondition: The program has sent the user to this function after adding an item
Postcondition: If the user has added all 8 items, then they will be sent to a function to end the program and the user will find out whatever and how much they have sold and how much commision they have earned. If the user decides to go and add an aditional item, they will be sent to such function to go add an item. If the user decides that they want to stop the program, they will be sent to a function to end the program and the user will find out whatever and how much they have sold and how much commision they have earned.
"""
def palbo_continue():
    if ph_present == 1 and pm_present == 1 and pw_present == 1 and pws_present == 1 and pb_present == 1 and pec_present == 1 and pt_present == 1 and pg_present == 1:
        palbo_simulation_ending_calculation()
    else:
        pc_continue = int(input("Would you like to continue?\n\n1. Yes\n2. No"))
        if pc_continue == 1:
            print("__________________________________________________________________")
            print("User has chosen to continue the simulaton.")
            palbo_cont_edit()
        else:
            print("__________________________________________________________________")
            print("User has chosen to end the simulation.")       
            palbo_simulation_ending_calculation()
    
