import random
from termcolor import colored as c


print(c("""
--------Game info----------
--How luck are you ?--

choose a number between 1 and 4 
if you try it 3 try and you did not win
that mean you are not lucky :( 

# if you win one time you are lucky
# if you win two times you are very lucky
# if you win three times you are the luckiest ever
""","cyan"))

while 1:
    num = random.randrange(1, 4)
    try:
        user_num = int(input(c("Enter a number between 1 and 4 >>>> ","yellow")))
        if user_num >= 1 and user_num <=4:
            if user_num == num:
                print(c("congratulation, you won :) \n","blue"))
            else:
                print(c("false , good luck next time !!!!\n","red"))
        #elif user_num == "":
        else:
            print(c("!!!!!!!!! Please choose a number between 1 - 4 !!!!!!!!!!\n","magenta"))

    except:
        print(c("warning!!!!, enter just a number between 1 - 4\n ","grey"))
