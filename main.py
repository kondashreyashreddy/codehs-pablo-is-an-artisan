# GAME OUTPUT
print("__________________________________________________________________")
print("                     Pablo is an Artisan Console")
print("Program Started.")
start = int(input("Good afternoon, user. Today you will act as a fellow artisan named Pablo who is infamous in the art community. Your goal is to design a nice outfit for Mr. Palbo to get cash.\n\nWould You Like to Continue?\n1. Yes\n2. No"))
if start == 1:
    palbo_default()
    print("__________________________________________________________________")
    print("User has started the simulation.")
    palbo_edit_beginning()
    palbo_continue()
else:
    program_end_screen()
  
