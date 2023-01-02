from tkinter import *
from tkinter import messagebox
import customtkinter
from random import choice as CompChoice
# pyinstaller --add-data "C:/Users/<user_name>/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/" -i icon.ico program.py (Example)

SingalPlayers = True

def ChooseNumber():# For Computer
    global mySecondStep
    
    """
    The work of this function
    1. Find the Winner (When Condition True)
    2. This function evaluates to the correct answer.
    
    Return a Correct Answer
    
    Note: Read all comments in this function for more information
    """

    len_AvailableNumbers = len(AvailableNumbers)
    
    # First Decision When First Move/chance of Computer
    if len_AvailableNumbers == 9:
        print("My First Move")
        mySecondStep = Nooks+(five,)
        return CompChoice(list(set(mySecondStep).intersection(AvailableNumbers)))
    
    
    
    # First Step of Computer this Condition True only first Time (when user enter only one input)
    # Make First Decision
    if len_AvailableNumbers == 8:
        print("***** First Dicision *****")
        if userinput == five:
            mySecondStep = Nooks
            return CompChoice(Nooks)
            
        elif userinput in Midway:
        
            mySecondStep = Nooks
            return five
        elif userinput in Nooks:
            
            mySecondStep = Midway
            return five
            
        return CompChoice(AvailableNumbers) # use module 'from random import choice'


    '''
    *URDU: Loop Information:
    1. agr computer ka symbol 1 line ma 2 mrtaba ho ga
        to ya os line ke tesare jaga ma apna symbol put kr da ga
    2. jab user ka symbol 1 line ma 2 mrtaba ho ga 
        to ya os line ke tesare jaga ma apna symbol put kr da ga
        '''
    # Evaluates to the correct answer
    # And Return a Box Number
    upgradeLines()
    def FindEmpty(_line):
        # Helps the function to evaluate the correct answer

        for idx, i in enumerate(_line):

            if i == 0:
                return idx

    # Others Choices When the 'Computer' or 'User' is near Completion
    # evaluates to the correct answer
    # MPT_Idx == Empty Index in One line
    for equSum in (20, 6):
        
        # Check rows 
        if sum(_row1) == equSum:
            MPT_Idx = FindEmpty(_row1)
            return MPT_Idx+1
        
        elif sum(_row2) == equSum:
            MPT_Idx = FindEmpty(_row2)
            return MPT_Idx+4
        
        elif sum(_row3) == equSum:
            MPT_Idx = FindEmpty(_row3)
            return MPT_Idx+7
        

        # Check Columns
        if sum(_col1) == equSum:
            MPT_Idx = FindEmpty(_col1)
            if MPT_Idx == 0: return 1
            if MPT_Idx == 1: return 4
            if MPT_Idx == 2: return 7
        elif sum(_col2) == equSum:
            MPT_Idx = FindEmpty(_col2)
            if MPT_Idx == 0: return 2
            if MPT_Idx == 1: return 5
            if MPT_Idx == 2: return 8
        elif sum(_col3) == equSum:
            MPT_Idx = FindEmpty(_col3)
            if MPT_Idx == 0: return 3
            if MPT_Idx == 1: return 6
            if MPT_Idx == 2: return 9

        # Check Others Lines
        if sum(_linex) == equSum:
            MPT_Idx = FindEmpty(_linex)
            if MPT_Idx == 0: return 1
            if MPT_Idx == 1: return 5
            if MPT_Idx == 2: return 9
        elif sum(_liney) == equSum:
            MPT_Idx = FindEmpty(_liney)
            if MPT_Idx == 0: return 3
            if MPT_Idx == 1: return 5
            if MPT_Idx == 2: return 7





    # My Second Step/Dicision
    if mySecondStep:
        if len_AvailableNumbers == 6:
            _mySecondStep = CompChoice(list(set(mySecondStep).intersection(AvailableNumbers)))
            mySecondStep = tuple()
            print("***** Second Dicision *****")
            return _mySecondStep
        else:
            print("Canceling second step")
            mySecondStep = tuple()
    print("Finally Random Choice")
    return CompChoice(AvailableNumbers)

    

def upgradeLines():
    # For Computer to Choose a Number and Check Winner
    
    print("Upgrading Lines...")
    global _row1, _row2, _row3, _col1, _col2, _col3, _linex, _liney

    #* Manage
    _MainList =[
        btnDict[1].cget("text"), btnDict[2].cget("text"), btnDict[3].cget("text"),
        btnDict[4].cget("text"), btnDict[5].cget("text"), btnDict[6].cget("text"),
        btnDict[7].cget("text"), btnDict[8].cget("text"), btnDict[9].cget("text")]
    
    
    # Convert List-elements to integer for evaluates the correct answer
    for idx in range(9):

        if _MainList[idx] == CompSymbol:
            _MainList[idx] = 10
            
        elif _MainList[idx] == default_str:
            _MainList[idx] = 0         
        elif _MainList[idx] == userSymbol:
            _MainList[idx] = 3


    # divide list in to Lines (rows, columns and cross lines)        
    _row1 = [_MainList[0], _MainList[1], _MainList[2]]
    _row2 = [_MainList[3], _MainList[4], _MainList[5]]
    _row3 = [_MainList[6], _MainList[7], _MainList[8]]

    _col1 = [_MainList[0], _MainList[3], _MainList[6]]
    _col2 = [_MainList[1], _MainList[4], _MainList[7]]
    _col3 = [_MainList[2], _MainList[5], _MainList[8]]
    
    _linex = [_MainList[0], _MainList[4], _MainList[8]]
    _liney = [_MainList[2], _MainList[4], _MainList[6]]
    

def FindingWinner():

    #* Find the Winner
    # Condition True, When User Enter 3 times Input (and computer Enter 2 times) (uncomplete)
    len_AvailableNumbers = len(AvailableNumbers)
    
    if len_AvailableNumbers <= 4:
        print("Finding Winner...")
        

        upgradeLines()
        
        def Change_BTN_Color(_btnList):
            for _btnNum in _btnList:
                btnDict[_btnNum].configure(fg_color="#800000")

        


        def _FindWinner(*args):
            
            def AssigningWiner(_Name, _Symbol=""):
                
                # printBoard()
                print(f"'{_Name}' WON the Match!")
                messagebox.showinfo(GameTitle, f"'{_Name}' WON the Match!")
                ResetGame()
                
            if equSum % 10 == 0:
                AssigningWiner(NamePlayer2)
            elif equSum % 3 == 0: 
                AssigningWiner(NamePlayer1)

        for equSum in (30, 9):
            
            # _FindWinner -> None , Change_BTN_Color -> None
            if sum(_row1) == equSum : return _FindWinner(Change_BTN_Color(row1)) 
            elif sum(_row2) == equSum : return _FindWinner(Change_BTN_Color(row2))
            elif sum(_row3) == equSum : return _FindWinner(Change_BTN_Color(row3))
                
            if sum(_col1) == equSum : return _FindWinner(Change_BTN_Color(col1))
            elif sum(_col2) == equSum : return _FindWinner(Change_BTN_Color(col2))
            elif sum(_col3) == equSum : return _FindWinner(Change_BTN_Color(col3))
                
            if sum(_linex) == equSum : return _FindWinner(Change_BTN_Color(linex))
            elif sum(_liney) == equSum : return _FindWinner(Change_BTN_Color(liney))
    
        # Game Over
        if len_AvailableNumbers == 0:

            # printBoard()
            print("*** Game Over ***")
            Change_BTN_Color(row1+row2+row3)
            messagebox.showinfo(GameTitle, "Game Over!")
            ResetGame()


def GlobalVars(): # Global Variables
    global Clicker, five, btnwidth, btnheight, userinput, AvailableNumbers, Nooks, Midway, mySecondStep, userSymbol, CompSymbol, default_str, heightPX, widthPX, btnDict, GameTitle, row1, row2, row3, col1, col2, col3, linex, liney, NamePlayer1


    Clicker = 1 # 1 == User , 0 == Computer
    five = 5
    btnwidth = 100
    btnheight = 100
    heightPX = 330
    widthPX = 330
    GameTitle = "Tic Tac Toe by immi"
    NamePlayer1 = "User 1"

    
    userinput = int()
    
    row1 = (1, 2, 3)
    row2 = (4, 5, 6)
    row3 = (7, 8, 9)
    col1 = (1, 4, 7)
    col2 = (2, 5, 8)
    col3 = (3, 6, 9)
    linex = (1, 5, 9)
    liney = (3, 5, 7)
    
    AvailableNumbers = list(row1+row2+row3)
    Nooks = (1, 3, 7, 9)
    Midway = (2, 4, 6, 8)
    mySecondStep = tuple()
    userSymbol = "X"
    CompSymbol = "O"
    
    default_str = ' '
    

def ResetGame(askfromuser= False):
    # global btnDict
    print("ResetGame")
    if askfromuser:
        isResetGame = messagebox.askokcancel(GameTitle, "Reset Game?")
        if not isResetGame:
            return None
    
    
    def ResetButtons():
        for btnN in range(1, 10):
            print("Reset Button")
            btnDict[btnN].configure(text=" ", state="normal", fg_color="#1f538d")

    print("Reseting Game")
    ResetButtons()
    GlobalVars()


def Change_BTN_txtState(btnN,_txt):
    """Change Buttons Text and Disable the Button When User or Computer Slect a Button"""
    btnDict[btnN].configure(text=_txt, state="disable")


def QuitGame():
    Quit = messagebox.askyesno("Exit", "Quit Game?")
    if Quit:
        exit()

def MultiPlayers(SwapButton=True):
    """
    1. Create First Time 'Play 2 Players' Menu Buttton
    2. Swap Buttons When User Click 'Play 2 Players' or 'Single Player'
    and Control 'Computer' or 'User 2'
    """
    global SingalPlayers, NamePlayer2
    
    # For Swaping Menu Buttons
    # Condition False When First Loop of Game
    if SwapButton:
        SingalPlayers = not SingalPlayers
        myMenu.delete(2)
        ResetGame()

    # Swap Menu Buttons (and Create Menu Button only first time)
    if SingalPlayers:
        myMenu.add_command(label= "Play 2 Players", command=MultiPlayers)
        NamePlayer2 = "Computer"
    else:
        myMenu.add_command(label= "Single Player", command=MultiPlayers)
        NamePlayer2 = "User 2"
        

def btn_click(btnN):
    """Main Button Controler Function
    When User Click any Button 1-9"""
    
    # Clicker == 'Swap User 1 or User 2', userinput == ''
    global Clicker, userinput
    
    
    
    if btnN in AvailableNumbers:

        if Clicker:
            # User1 Entry
            Change_BTN_txtState(btnN, "X")
            AvailableNumbers.remove(btnN)
            FindingWinner()
            print(f"User 1 Input: {btnN} \nAvailableNumbers: {AvailableNumbers}")
            Clicker = 0
        else:
            # User2 Entry
            Change_BTN_txtState(btnN, "O")
            AvailableNumbers.remove(btnN)
            FindingWinner()
            print(f"User 2 Input: {btnN} \nAvailableNumbers: {AvailableNumbers}")
            Clicker = 1
            
        
        if SingalPlayers:
            # Computer Entry
            userinput = btnN
            Computer_Num = ChooseNumber()
            Change_BTN_txtState(Computer_Num, "O")
            AvailableNumbers.remove(Computer_Num)
            FindingWinner()
            Clicker = 1
        
    else:
        print("\aClick Another Button")
        messagebox.showerror(title=GameTitle, message="Hey! That box has already been selected \nPlease Choose Another Box...")
        # messagebox.askyesno(message="Yes or No")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# GUI Loop
FirstTime = True
root = customtkinter.CTk()
if FirstTime:
    FirstTime = False
    GlobalVars()


try:#GUI Information
    root.title(GameTitle)
    root.iconbitmap("tictactoe3.ico")
    root.geometry(f"{heightPX}x{widthPX}")
    root.minsize(widthPX, heightPX)
    root.maxsize(widthPX, heightPX)
except Exception as error:
    print(error)



try:# Buttons
    
    btnDict = dict()
    
    btnDict[1] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(1))
    btnDict[2] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(2))
    btnDict[3] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(3))
    btnDict[4] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(4))
    btnDict[5] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(5))
    btnDict[6] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(6))
    btnDict[7] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(7))
    btnDict[8] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(8))
    btnDict[9] = customtkinter.CTkButton(master=root, text=" ", width=btnwidth, height=btnheight, font=("Arial Rounded MT Bold", 70), command=lambda:btn_click(9))
    
    root.bind('1',lambda event:btn_click(1))
    root.bind('2',lambda event:btn_click(2))
    root.bind('3',lambda event:btn_click(3))
    root.bind('4',lambda event:btn_click(4))
    root.bind('5',lambda event:btn_click(5))
    root.bind('6',lambda event:btn_click(6))
    root.bind('7',lambda event:btn_click(7))
    root.bind('8',lambda event:btn_click(8))
    root.bind('9',lambda event:btn_click(9))
    root.bind('<Escape>',lambda event:QuitGame())
    
    
    btnDict[1].grid(row=0, column=0, padx=five, pady=five)
    btnDict[2].grid(row=0, column=1, padx=five, pady=five)
    btnDict[3].grid(row=0, column=2, padx=five, pady=five)
    btnDict[4].grid(row=1, column=0, padx=five, pady=five)
    btnDict[5].grid(row=1, column=1, padx=five, pady=five)
    btnDict[6].grid(row=1, column=2, padx=five, pady=five)
    btnDict[7].grid(row=2, column=0, padx=five, pady=five)
    btnDict[8].grid(row=2, column=1, padx=five, pady=five)
    btnDict[9].grid(row=2, column=2, padx=five, pady=five)

except Exception as error:
    print(error)


try:# Menu
    # Create Menu
    myMenu = Menu(root)
    root.configure(menu= myMenu)
    OptionsMenu = Menu(myMenu, tearoff=False)
    # myMenu.add_cascade(label="Option", menu=myMenu)
    myMenu.add_command(label="Reset Game", command=lambda:ResetGame(True))
    
    # myMenu.add_command(label= "Play 2 Players", command=MultiPlayers)
    MultiPlayers(False)
    
except Exception as error:
    print(error)

root.mainloop()